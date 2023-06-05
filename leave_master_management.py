from flask import Flask
from flask import render_template,request,redirect,abort
import pymysql
from models import *

def leave_master_display():
    try:
        username = session.get("name_type")
        display = leave_master.query.all()
        return render_template('leave_management_display.html',display=display,username=username)
    except Exception as msg:
        return "<b>Error :<b>{}".format(str(msg))

def leave_master_insert():
    try:
        username = session.get("name_type")
        if request.method == 'GET':
            return render_template('leave_management_insert.html',username=username)

        if request.method == 'POST':
            type_name = request.form['type_name']
            count = request.form['count']
            status = request.form['status']

            leave_master_insert_table = leave_master(type_name=type_name,count=count,status=status)
            db.session.add(leave_master_insert_table)
            db.session.commit()
            return redirect('/master_leave_management_display')

    except Exception as msg:
        return "<b>Error :<b>{}".format(str(msg))        

def leave_master_update(id):
    leave_master_update_table = leave_master.query.filter_by(id=id).first()
    username = session.get("name_type")
    try: 
        if request.method == 'GET':
            return render_template('leave_management_update.html',leave_master_update_table=leave_master_update_table,username=username)

        if request.method == 'POST':
            if leave_master_update_table:
                db.session.delete(leave_master_update_table)
                db.session.commit()

                type_name = request.form['type_name']
                count = request.form['count']
                status = request.form['status']

                leave_master_update_table = leave_master(type_name=type_name,count=count,status=status)
                db.session.add(leave_master_update_table)
                db.session.commit()
                return redirect(f'/master_leave_management_update/{id}')

    except Exception as msg:
        return "<b>Error:</b>{}".format(str(msg))

def leave_master_delete(id):
    try:
        leave_master_delete_table = leave_master.query.filter_by(id=id).first()
        if request.method == 'GET':
            if leave_master_delete_table:
                db.session.delete(leave_master_delete_table)
                db.session.commit()
                return redirect('/master_leave_management_display')

    except Exception as msg:
        return "<b>Error:</b>{}".format(str(msg))