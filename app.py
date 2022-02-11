from flask import Flask, render_template, session
from models import db, migrate
import routes.infection_route as irt
import routes.cc_route as cr
import d0208_project_mini04.routes.hosp_route as hr
import d0208_project_mini04.routes.status_route as sr
import routes.mem_route as mr

import config


app = Flask(__name__)

app.secret_key = 'key'
app.config.from_object(config)

app.register_blueprint(irt.bp)
app.register_blueprint(cr.bp)
app.register_blueprint(hr.bp)
app.register_blueprint(sr.bp)
app.register_blueprint(mr.bp)

db.init_app(app)
migrate.init_app(app, db)


@app.route('/')
def root():
    if 'flag' not in session.keys():
        session['flag'] = False
    return render_template('index.html')


if __name__ == '__main__':
    app.run(debug=True)
    # db.run()
    # migrate.run()