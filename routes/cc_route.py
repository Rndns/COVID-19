from flask import render_template, request, Blueprint
import covid19.centerCheck.cc_service as cc_service

service = cc_service.centerCheckService()

bp = Blueprint('covid19', __name__, url_prefix='/covid19') #라우트 등록 객체

@bp.route('/list', methods=['GET', 'POST'])
def list():
    centers = service.getCenterByList()
    return render_template('covid19/list.html', centers=centers)

@bp.route('/detail/<int:id>', methods=['GET'])
def detail(id):
    c = service.getCenterById(id)
    return render_template('covid19/detail.html', c=c)

