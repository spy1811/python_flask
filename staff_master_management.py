from flask import Flask
from flask import render_template,request,redirect,abort
import pymysql
from models import *

def staff_master_display():
    username = session.get("name_type")
    try:
        display = staff.query.all()
        return render_template('staff_management_display.html',display=display,username=username)
    except Exception as msg:
        return "<b>Error :<b>{}".format(str(msg))

def staff_master_insert():
    try:
        username = session.get("name_type")
        if request.method == 'GET':
            return render_template('staff_management_insert.html',username=username)

        if request.method == 'POST':
            sname = request.form['sname']
            semail = request.form['semail']
            sphone = request.form['sphone']
            spost = request.form['spost']
            apassword = request.form['apassword']
            user_type = request.form['user_type']

            staff_master_insert_table = staff(sname=sname,semail=semail,sphone=sphone,spost=spost)
            user_master_insert_table = user(uemail=semail,upassword=apassword,user_type=user_type,status='Active')
            db.session.add(staff_master_insert_table)
            db.session.add(user_master_insert_table)
            db.session.commit()
            return redirect('/staff_management_display')

    except Exception as msg:
        return "<b>Error :<b>{}".format(str(msg))

def staff_master_update(id):
    staff_master_update_table = staff.query.filter_by(id=id).first()
    user_master_update_table = user.query.filter_by(uemail=staff_master_update_table.semail).first()
    try: 
        if request.method == 'GET':
            username = session.get("name_type")
            return render_template('staff_management_update.html',staff_master_update_table=staff_master_update_table,username=username,user_master_update_table=user_master_update_table)

        if request.method == 'POST':
            if staff_master_update_table:
                db.session.delete(staff_master_update_table)
                db.session.commit()

                sname = request.form['sname']
                semail = request.form['semail']
                sphone = request.form['sphone']
                spost = request.form['spost']
                apassword = request.form['apassword']
                user_type = request.form['user_type']

                staff_master_update_table = staff(sname=sname,semail=semail,sphone=sphone,spost=spost)
                user_master_update_table = user(uemail=semail,upassword=apassword,user_type=user_type,status='Active')
                db.session.add(staff_master_update_table)
                db.session.add(user_master_update_table)
                db.session.commit()
                return redirect(f'/staff_management_update/{id}')

    except Exception as msg:
        return "<b>Error:</b>{}".format(str(msg))

def staff_master_delete(id):
    try:
        staff_master_delete_table = staff.query.filter_by(id=id).first()
        user_master_delete_table = user.query.filter_by(uemail=staff_master_delete_table.semail).first()
        if request.method == 'GET':
            if staff_master_delete_table:
                db.session.delete(staff_master_delete_table)
                db.session.delete(user_master_delete_table)
                db.session.commit()
                return redirect('/staff_management_display')

    except Exception as msg:
        return "<b>Error:</b>{}".format(str(msg))