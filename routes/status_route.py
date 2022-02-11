from flask import render_template, Blueprint
import d0208_project_mini04.model.vaccine.service as v_service

service = v_service.vaccineService()

bp = Blueprint('corona_vaccine', __name__, url_prefix='/corona_vaccine') #라우트 등록 객체

@bp.route('/status', methods=['GET', 'POST'])
def status():
    status = service.getVaccineStatDaily()
    return render_template('corona_seoul/status.html', status=status)


