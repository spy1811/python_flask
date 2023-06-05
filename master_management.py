from flask import Flask
from flask import render_template,request,redirect,session
import pymysql
from models import *
from flask_session import Session

def master_management_display():
    try:
        display = branch_master.query.all()
        username = session.get("name_type")
        print(username)
        return render_template('master_management_display.html', display = display,username=username)
        
    except Exception as msg:
        return "<b>Error : </b>"+str(msg)

def master_management_insert():
    try:
        username = session.get("name_type")
        staff_display = staff.query.all()
        if request.method == 'GET': 
            return render_template('master_management_insert.html',username=username,staff_display=staff_display)
        
        if request.method == 'POST':
            branch_name = request.form['bname']
            hod_id = request.form['hid']

            branch_master_insert_table = branch_master(bname=branch_name,hod_id=hod_id) 
            db.session.add(branch_master_insert_table)
            staff_update = staff.query.filter_by(id=hod_id).first()
            user_update_table = user.query.filter_by(uemail=staff_update.semail).first()
            user_update_table.user_type="HOD"
            db.session.commit()
            return redirect('/master_management_display')

        return render_template('master_management_insert.html',username=username)
    
    except Exception as msg:
        return "<b>Error : </b>"+str(msg)

def master_management_update(id):
    master_update_table = branch_master.query.filter_by(id=id).first()
    staff_display = staff.query.all()
    try:
        if request.method == 'GET':
            username = session.get("name_type")
            return render_template('master_management_update.html',master_update_table=master_update_table,username=username,staff_display=staff_display)

        if request.method == 'POST':
            if master_update_table:
                # db.session.delete(master_update_table)
                # db.session.commit()

                branch_name = request.form['bname']
                hod_id = request.form['hid']

                staff_update = staff.query.filter_by(id=hod_id).first()

                print(staff_update)

                master_update_table.bname = branch_name
                master_update_table.hod_id = hod_id

                # master_update_table = branch_master.update(dict(bname=branch_name,hod_id=hod_id))
                user_update_table = user.query.filter_by(uemail=staff_update.semail).first()
                user_update_table.user_type="HOD"
                # print(user_update_table)
                # db.session.add(master_update_table)
                # db.session.add(user_update_table)
                db.session.commit()
                return redirect(f'/master_management_update/{id}')

    except Exception as msg:
        return "<b>Error:</b>{}".format(str(msg))

def master_management_delete(id):
    try:
        master_delete_table = branch_master.query.filter_by(id=id).first()
        if request.method == 'GET':
            if master_delete_table:
                db.session.delete(master_delete_table)
                db.session.commit()
                return redirect('/master_management_display')

    except Exception as msg:
        return "<b>Error:</b>{}".format(str(msg))