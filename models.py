from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy
from flask import session

db = SQLAlchemy()
migrate = Migrate()


class Member(db.Model):
    id = db.Column(db.String(20), primary_key=True)
    pwd = db.Column(db.String(20), nullable=False)
    name = db.Column(db.String(20), nullable=False)
    tell = db.Column(db.String(20), nullable=False)


class Reserve(db.Model):
    num = db.Column(db.Integer, primary_key=True)
    visitor = db.Column(db.String(20), db.ForeignKey('member.id', ondelete='CASCADE'))
    member = db.relationship('Member', backref=db.backref('board_set'))
    hospital = db.Column(db.String(50), nullable=False)
    memo = db.Column(db.String(20), nullable=False)
    date = db.Column(db.String(20), nullable=False)


class MemService:
    def join(self, m: Member):
        db.session.add(m)
        db.session.commit()

    def login(self, id: str, pwd: str):
        m = Member.query.get(id)
        if m is not None:
            if pwd == m.pwd:
                session['login_id'] = id
                session['flag'] = True
                return True
        return False

    def myInfo(self):
        id = session['login_id']
        return Member.query.get(id)

    def editMyInfo(self, pwd:str):
        m = self.myInfo()
        m.pwd = pwd
        db.session.commit()

    def logout(self):
        session.pop('login_id')
        session['flag'] = False

    def out(self):
        m = self.myInfo()
        db.session.delete(m)
        db.session.commit()
        self.logout()


class ReserveService:
    def addReserve(self, r: Reserve):
        db.session.add(r)
        db.session.commit()

    def getReserve(self, num):
        return Reserve.query.get(num)

    def getByVisitor(self, visitor):
        v = Reserve.query.get(visitor)
        if v is not None:
            return v.Reserve_set

    def delReserve(self, num):
        r = self.getReserve(num)
        db.session.delete(r)
        db.session.commit()

