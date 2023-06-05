from flask import Flask
from flask import render_template,request,redirect,abort
import pymysql
from models import *

def leave_display():
    try:
        username = session.get("name_type")
        display = leave.query.all()
        # leave_id = leave_master.query.all().first()
        # staff_display = staff.query.all().first() 

        # leaves_display = staff.query.join(leave).add_columns(staff.id,staff.sname,staff.semail,staff.sphone,staff.spost,leave.id,leave.leave_id,leave.staff_id,leave.approve_level).join(leave_master).add_columns(leave_master.id,leave_master.type_name,leave_master.count,leave_master.status).filter(leave.id == leave_master.id)
        
        con = pymysql.connect(host='localhost',user='root',password='Rohit007#',db='leave_management')
        cursor = con.cursor()
        sql="""select * from leaves as lv join staff_master as sm on lv.staff_id = sm.id join leave_master as lm on lv.leave_id = lm.id where lv.status='Pending'"""
        if(username == "Admin"):
            sql="""select * from leaves as lv join staff_master as sm on lv.staff_id = sm.id join leave_master as lm on lv.leave_id = lm.id where lv.approve_level='Principle'"""
        elif(username == "Principle"):
            sql="""select * from leaves as lv join staff_master as sm on lv.staff_id = sm.id join leave_master as lm on lv.leave_id = lm.id where lv.approve_level='HOD'"""

        # sql="""select * from leaves as lv join staff_master as sm on lv.staff_id = sm.id join leave_master as lm on lv.leave_id = lm.id"""
        cursor.execute(sql)
        dis = cursor.fetchall()
        con.commit()

        return render_template('leave_display.html',username=username,display=display,dis=dis)

    except Exception as msg:
        return "<b>Error :<b>{}".format(str(msg))

def leave_insert():
    try:
        username = session.get('name_type')
        email = session.get('user_email')
        if request.method == 'GET':
            leaves_display = leave_master.query.all()
            staff_display = staff.query.filter_by(semail=email).first()

            return render_template('leave_insert.html',username=username,leaves_display=leaves_display,staff_display=staff_display)

        if request.method == 'POST':
            user_email = session.get('user_email')
            usr = user.query.filter_by(uemail=username).first()

            leave_id = request.form['leave_id']
            staff_id = request.form['staff_id']
            # approve_level = request.form['approve_level']
            approve_level = "NULL"
            applied_date = request.form['applied_date']
            # status = request.form['Status']
            status = "Pending"
            remark = request.form['remark']


            leave_insert_table = leave(leave_id=leave_id,staff_id=staff_id,approve_level=approve_level,applied_date=applied_date,status=status,remark=remark)
            db.session.add(leave_insert_table)
            db.session.commit()
            return redirect('/leave_display')

    except Exception as msg:
        return "<b>Error :<b>{}".format(str(msg))
    
def leave_update(id):
    leave_update_table = leave.query.filter_by(id=id).first()
    try:
        username = session.get('name_type')
        email = session.get('user_email')
        if request.method == 'GET':
            leaves_display = leave_master.query.all()
            staff_display = staff.query.filter_by(semail=email).first()
            username = session.get("name_type")
            return render_template('leave_update.html',leave_update_table=leave_update_table,username=username,leaves_display=leaves_display,staff_display=staff_display)
        
        if request.method == 'POST':
            if leave_update_table :
                db.session.delete(leave_update_table)
                db.session.commit()

                leave_id = request.form['leave_id']
                staff_id = request.form['staff_id']
                # approve_level = request.form['approve_level']
                approve_level = "NULL"
                applied_date = request.form['applied_date']
                # status = request.form['Status']
                status = "Pending"
                remark = request.form['remark']

                leave_update_table = leave(leave_id=leave_id,staff_id=staff_id,approve_level=approve_level,applied_date=applied_date,status=status,remark=remark)
                db.session.add(leave_update_table)
                db.session.commit()
                return redirect(f'/leave_update/{id}')


    except Exception as msg:
        return "<b>Error :<b>{}".format(str(msg))
    
def leave_delete(id):
    try:
        leave_delete_table = leave.query.filter_by(id=id).first()
        if request.method == 'GET':
            if leave_delete_table:
                db.session.delete(leave_delete_table)
                db.session.commit()
                return redirect('/leave_display')

    except Exception as msg:
        return "<b>Error:</b>{}".format(str(msg))

def leave_approve():
    try:
        if request.method=='POST':
            username = session.get('name_type')
            id = request.form['id']

            leave_display = leave.query.filter_by(id=id).first()
            leave_display.approve_level = username
            if(username == 'Admin'):
                leave_display.status='approved'
            db.session.commit()
            return redirect('/leave_display')

    except Exception as msg:
        return "<b>Error :<b>{}".format(str(msg))       

def reports():
    try:
        username = session.get('name_type')
        if request.method=='GET':
            con = pymysql.connect(host='localhost',user='root',password='Rohit007#',db='leave_management')
            cursor = con.cursor()
            # sql="""select * from leaves as lv join staff_master as sm on lv.staff_id = sm.id join leave_master as lm on lv.leave_id = lm.id where lv.status='%s'"""%(type)

            sql="""select * from leaves as lv join leave_track as lt on lv.staff_id = lt.id join leave_master as lm on lv.leave_id = lm.id"""
            cursor.execute(sql)
            dis = cursor.fetchall()
            con.commit()
            return render_template('reportdisplay.html',dis=dis,username=username)

    except Exception as msg:
        return "<b>Error :<b>{}".format(str(msg))