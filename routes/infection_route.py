import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from flask import render_template, request, Blueprint
import d0208_project_mini04.model.infection.service as isv

ksv = isv.KoreaService()
ssv = isv.SeoulService()
rsv = isv.RegionService()

bp = Blueprint('infection', __name__, url_prefix='/infection')


@bp.route('/main', methods=['GET'])
def main():
    return render_template('infection/main.html')


@bp.route('/location', methods=['GET', 'POST'])
def location():
    start = request.form['start']
    end = request.form['end']
    date = request.form['date']
    date = date.replace('-', '.')+'.00'

    plt.rcParams['font.family'] = 'Malgun Gothic'
    plt.rcParams['axes.unicode_minus'] = False

    type = request.form['location']
    if type == 'k':
        res = ksv.getKoreaInfo(start, end)
        val = []
        index = []
        colum = ['총확진', '추가확진', '치료중', '총퇴원', '사망']
        for i in res:
            val.append([int(i.T_HJ), int(i.N_HJ), int(i.TY_CARE), int(i.RECOVER), int(i.DEATH)])
            index.append(i.T_DT.replace('.', '-')[2:10])

        value = np.array(val)
        table = pd.DataFrame(value, index, colum)
        table.plot()
        plt.xlabel('날짜')
        plt.ylabel('인구수(*10만)')
        plt.title('전국 코로나 감염 현황')
        plt.savefig('static/graph/chartK.png')
        return render_template('infection/korea.html', res=res)

    if type == 's':
        res = ssv.getSeoulInfo(start, end)
        val = []
        index = []
        colum = ['총확진', '추가확진', '치료중', '총퇴원', '추가퇴원', '사망']
        for i in res:
            val.append([int(i.S_HJ), int(i.SN_HJ), int(i.S_CARE), int(i.S_RECOVER), int(i.SN_RECOVER), int(i.S_DEATH)])
            index.append(i.S_DT.replace('.', '-')[2:10])

        value = np.array(val)
        table = pd.DataFrame(value, index, colum)
        table.plot()
        plt.xlabel('날짜')
        plt.ylabel('인구수')
        plt.title('서울 코로나 감염 현황')
        plt.savefig('static/graph/chartS.png')
        return render_template('infection/seoul.html', res=res)

    if type == 'r':
        res = rsv.getRegionInfo(date)
        return render_template('infection/region.html', res=res)


@bp.route('/case')
def case():
    return render_template('infection/test.html')


# @bp.route('/graph')
# def graph():
#     img_path = 'static/graph/my_plot.png'
#
#     x = [1, 2, 3, 4]
#     y = [3, 8, 5, 6]
#     fig, ax = plt.subplots()
#     plt.plot(x, y)
#     fig.savefig(img_path)
#     img_path = '/' + img_path
#     return render_template('test.html', img_path=img_path)
