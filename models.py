from flask import Flask,session
from flask_migrate import Migrate
from flask_sqlalchemy import *
import MySQLdb
from flask_session import Session
import hashlib

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:Rohit007#@localhost:3306/leave_management'
app.config['SQLALCHEMY_TRACK_MODIFICATION'] = True
app.config['extend_existing'] = True

app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
app.secret_key = "abc"  
Session(app)

db = SQLAlchemy()

migrate = Migrate(app,db)

db.init_app(app)

class branch_master(db.Model):

    #Create table branch_master.
    __tablename__ = 'branch_master'

    #Column Initialization.
    id = db.Column(db.Integer, primary_key=True,autoincrement=True)
    bname  = db.Column(db.String(50), index=True)
    hod_id = db.Column(db.Integer, primary_key=True)

    def __init__(self,bname,hod_id):
        # self.id = id
        self.bname = bname
        self.hod_id = hod_id

    def __repr__(self):
        return '<Branch Master: {}>'.format(self.bname)

class staff(db.Model):

    #Create table staff.
    __tablename__ = 'staff_master'

    #Column Initilization.
    id = db.Column(db.Integer,primary_key=True,autoincrement=True)
    sname = db.Column(db.String(50),index=True)
    semail = db.Column(db.String(50), index=True)
    sphone = db.Column(db.String(50), index=True)
    spost = db.Column(db.String(50), index=True)

    def __init__(self,sname,semail,sphone,spost):
        # self.id = id
        self.sname = sname
        self.semail = semail
        self.sphone = sphone
        self.spost = spost

    def __repr__(self):
        return '<Staff Master : {}>'.format(self.sname)

class principle(db.Model):

    #Create table Principle
    __tablename__ = 'principle'

    #Column Initilization
    id = db.Column(db.Integer, primary_key=True)
    pname = db.Column(db.String(50), index=True)
    pemail = db.Column(db.String(50), index=True)
    pphone = db.Column(db.String(50), index=True)

    def __init__(self,pname,pemail,pphone):
        # self.id = id
        self.pname = pname 
        self.pemail = pemail
        self.pphone = pphone

    def __repr__(self):
        return '<Staff Master>: {}'.format(self.pname)

class admin(db.Model):

    #Create table Admin
    __table__name = 'admin'

    #Column Initilization   
    id = db.Column(db.Integer, primary_key=True)
    aname = db.Column(db.String(50), index=True)
    aemail = db.Column(db.String(50), index=True)
    aphone = db.Column(db.String(50), index=True)


    def __init__(self,aname,aemail,aphone):
        self.aname = aname 
        self.aemail = aemail
        self.aphone = aphone

    def __repr__(self):
        return '<Admin Master>: {}'.format(self.aname)

class user(db.Model):

    #Create table user
    __tablename__ = 'user'

    #Column Initilization
    id = db.Column(db.Integer, primary_key=True)
    uemail = db.Column(db.String(50), index=True)
    upassword = db.Column(db.String(50), index=True)
    user_type = db.Column(db.String(50), index=True)
    status = db.Column(db.String(50), index=True)

    def __init__(self,uemail,upassword,user_type,status):
        self.uemail = uemail
        self.upassword = upassword
        self.user_type = user_type
        self.status = status

    def __repr__(self):
        return '<User Type>:{}'.format(self.user_type)

class leave_master(db.Model):

    #Create table leave_master
    __tablename__ = 'leave_master'

    #Column Intialization.
    id = db.Column(db.Integer, primary_key=True)
    type_name = db.Column(db.String(50), index=True)
    count = db.Column(db.Integer, index=True)
    status = db.Column(db.String(50), index=True)

    def __init__(self,type_name,count,status):
        self.type_name = type_name
        self.count = count
        self.status = status

    def __repr__(self):
        return '<Leave Master Type name:>{}'.format(self.type_name)

class leave(db.Model):

    #Create table leave
    __tablename__ = 'leaves'

    #Create column
    id = db.Column(db.Integer, primary_key=True,autoincrement=True)
    leave_id = db.Column(db.Integer, primary_key=True)
    staff_id = db.Column(db.Integer, primary_key=True)
    approve_level = db.Column(db.String(50), index=True)
    applied_date = db.Column(db.String(50), index=True)
    status = db.Column(db.String(50), index=True)
    remark = db.Column(db.String(50), index=True)

    def __init__(self,leave_id,staff_id,approve_level,applied_date,status,remark):
        # self.id = id
        self.leave_id = leave_id
        self.staff_id = staff_id
        self.approve_level = approve_level
        self.applied_date = applied_date
        self.status = status
        self.remark = remark

    def __repr__(self):
        return '<Leave Id>:{}'.format(self.leave_id)

class leave_track(db.Model):

    #Create table
    __tablename__ = 'leave_track'

    #Column Intilization
    id = db.Column(db.Integer, primary_key=True)
    leave_id = db.Column(db.Integer, primary_key=True)
    uid = db.Column(db.Integer, primary_key =True)
    approve_date = db.Column(db.String(50), index=True)
    remark = db.Column(db.String(50), index=True)

    def __init__(self,leave_id,uid,approve_date,remark):
        self.leave_id = leave_id
        self.uid = uid
        self.approve_date = approve_date
        self.remark = remark

    def __repr__(self):
        return '<Leave Id>: {}'.format(self.leave_id)
    

class notice_board(db.Model):

    #Create table
    __tablename__ = 'notice_board'

    #Column Intilization
    id = db.Column(db.Integer, primary_key=True)
    notice_name = db.Column(db.String(50), index=True)
    notice_content = db.Column(db.String(50), index=True)

    def __init__(self,notice_name,notice_content):
        self.notice_name = notice_name
        self.notice_content = notice_content

    def __repr__(self):
        return '<Notice Board Id>: {}'.format(self.id)
    
class workload_report(db.Model):

    #Create table
    __tablename__ = 'workload_report'

    #Column Intilization
    id = db.Column(db.Integer, primary_key=True)
    monday = db.Column(db.String(50), index=True)
    tuesday = db.Column(db.String(50), index=True)
    wednesday = db.Column(db.String(50), index=True)
    thursday = db.Column(db.String(50), index=True)
    friday = db.Column(db.String(50), index=True)
    saturday = db.Column(db.String(50), index=True)
    sunday = db.Column(db.String(50), index=True)
    date_time = db.Column(db.String(50), index=True)
    staff_id = db.Column(db.Integer,index=True)

    def __init__(self,monday,tuesday,wednesday,thrusday,friday,saturday,sunday,date_time,staff_id):
        self.monday = monday
        self.tuesday = tuesday
        self.wednesday = wednesday
        self.thursday = thrusday
        self.friday = friday
        self.saturday = saturday
        self.sunday = sunday
        self.date_time = date_time
        self.staff_id = staff_id

    def __repr__(self):
        return '<Workload Board Id>: {}'.format(self.id)
    
with app.app_context(): 
    db.create_all()