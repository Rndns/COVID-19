from flask import render_template, request, Blueprint
import d0208_project_mini04.model.hosp.service as hservice

service = hservice.HospService()

bp = Blueprint('hosp', __name__, url_prefix='/hosp')

@bp.route('', methods=['GET'])
def hinfo():
    hinfo = service.getHosp()
    return render_template('hosp/hospInfo.html', hinfo=hinfo)

@bp.route('/getbyname/<string:yadmNm>')
def getbyname(yadmNm):
    hlist = service.getByName(yadmNm)
    return render_template('hosp/hospInfo.html', hinfo=hlist)

@bp.route('/getbyaddr/<string:addr>')
def getbyaddr(addr):
    hlist = service.getByAddr(addr)
    return render_template('hosp/hospInfo.html', hinfo=hlist)