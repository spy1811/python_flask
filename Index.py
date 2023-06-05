from flask import Flask
from flask import render_template,request,sessions
from flask_session import Session
from models import *
from auth import *
from master_management import *
from admin_master_management import *
from leave_master_management import *
from staff_master_management import *
from principle_master_management import *
from user_master_management import *
from leave import *
from notice_board import *  
from workload import *
from workload_admin import *

#-----------------Index------------------------------------------

@app.route('/',methods=['GET','POST'])
def login():
    return LoginPage()

@app.route('/index')
def index():
    try:
        username = session.get("name_type")
        username = session.get("name_type")
        display = leave_master.query.all()
        return render_template('index.html',username=username,display=display)
    except Exception as msg:
        return redirect("/")

@app.route('/logout')
def logout():
    return LogOut()

#-----------------Branch Management-------------------------------

@app.route('/master_management_display')
def Master_Management_Display():
    return master_management_display()

@app.route('/master_management_insert',methods=['GET','POST'])
def Master_Management_Insert():
    return master_management_insert()

@app.route('/master_management_update/<int:id>',methods=['GET','POST'])
def Master_Management_Update(id):
    return master_management_update(id=id)

@app.route('/master_management_delete/<int:id>',methods=['GET','POST'])
def Masters_Management_Delete(id):
    return master_management_delete(id=id)
    
#-----------------Leaves Master Management-------------------------

@app.route('/master_leave_management_display')
def Master_Leave_Management_Display():
    return leave_master_display()

@app.route('/master_leave_management_insert',methods=['GET','POST'])
def Master_Leave_Management_Insert():
    return leave_master_insert()

@app.route('/master_leave_management_update/<int:id>',methods=['GET','POST'])
def Master_Leave_Management_Update(id):
    return leave_master_update(id=id)

@app.route('/master_leave_managemment_delete/<int:id>',methods=['GET','POST'])
def Master_Management_Delete(id):
    return leave_master_delete(id=id)

#-----------------Admin Management-----------------------------------

@app.route('/admin_management_display')
def Admin_Management_Display():
    return admin_master_display()

@app.route('/admin_management_insert',methods=['GET','POST'])
def Admin_Management_Insert():
    return admin_master_insert()

@app.route('/admin_management_update/<int:id>',methods=['GET','POST'])
def Admin_Management_Update(id):
    return admin_master_update(id=id)

@app.route('/admin_managemment_delete/<int:id>',methods=['GET','POST'])
def Admin_Management_Delete(id):
    return admin_management_delete(id=id)

#-----------------Staff Management-----------------------------------

@app.route('/staff_management_display')
def Staff_Management_Display():
    return staff_master_display()

@app.route('/staff_management_insert',methods=['GET','POST'])
def Staff_Management_Insert():
    return staff_master_insert()

@app.route('/staff_management_update/<int:id>',methods=['GET','POST'])
def Staff_Management_Update(id):
    return staff_master_update(id=id)

@app.route('/staff_management_delete/<int:id>',methods=['GET','POST'])
def staff_Management_Delete(id):
    return staff_master_delete(id=id)

#-----------------Principle Management-----------------------------------

@app.route('/principle_management_display')
def Principle_Management_Display():
    return principle_master_display()

@app.route('/principle_management_insert',methods=['GET','POST'])
def Principle_Management_Insert():
    return principle_master_insert()

@app.route('/principle_management_update/<int:id>',methods=['GET','POST'])
def Principle_Management_Update(id):
    return principle_master_update(id=id)

@app.route('/principle_management_delete/<int:id>',methods=['GET','POST'])
def Principle_Management_Delete(id):
    return principle_master_delete(id=id)

#-----------------User Management-----------------------------------

@app.route('/user_management_display')
def User_Management_Display():
    return user_master_display()

@app.route('/user_management_insert',methods=['GET','POST'])
def User_Management_Insert():
    return user_master_insert()

@app.route('/user_management_update/<int:id>',methods=['GET','POST'])
def User_Management_Update(id):
    return user_master_update(id=id)

@app.route('/user_management_delete/<int:id>',methods=['GET','POST'])
def User_Management_Delete(id):
    return user_master_delete(id=id)

#-----------------Leaves-------------------------------------------

@app.route('/leave_display')
def Leaves_Display():
    return leave_display()

@app.route('/leave_insert',methods=['GET','POST'])
def Leaves_Insert():
    return leave_insert()

@app.route('/leave_update/<int:id>',methods=['GET','POST'])
def Leave_Update(id):
    return leave_update(id=id)

@app.route('/leave_delete/<int:id>',methods=['GET','POST'])
def Leave_Delete(id):
    return leave_delete(id=id)

@app.route('/approve',methods=['POST','GET'])
def Leave_Approve():
    return leave_approve()

@app.route('/reports',methods=['GET'])
def Reports():
    return reports()

#-----------------Notice Board-------------------------------------------

@app.route('/notice_board_display')
def Notice_Board_Display():
    return notice_board_display()

@app.route('/notice_board_insert',methods=['GET','POST'])
def Notice_Board_Insert():
    return notice_board_insert()

@app.route('/notice_board_update/<int:id>',methods=['GET','POST'])
def Notice_Board_Update(id):
    return notice_board_update(id=id)

@app.route('/notice_board_delete/<int:id>',methods=['GET','POST'])
def Notice_Board_Delete(id):
    return notice_board_delete(id=id)

#------------------------Workload-----------------------------------------

@app.route('/workload_display')
def Workload_Display():
    return workload_display()

@app.route('/workload_insert',methods=['GET','POST'])
def Workload_Insert():
    return workload_insert()

@app.route('/workload_update/<int:id>',methods=['GET','POST'])
def Workload_Update(id):
    return workload_update(id=id)

@app.route('/workload_delete/<int:id>',methods=['GET','POST'])
def Workload_Delete(id):
    return workload_delete(id=id)

@app.route('/workload_admin_display',methods=['GET','POST'])
def Workload_Admin_Display():
    return workload_admin_display()