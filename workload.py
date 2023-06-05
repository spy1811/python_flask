from flask import Flask
from flask import render_template,request,redirect,abort,session
import pymysql
from models import *
from datetime import datetime

def workload_display(): 
    try:
        username = session.get("name_type")
        em = session.get('user_email')
        staff_display = staff.query.filter_by(semail=em).first()
        display = workload_report.query.filter_by(staff_id=staff_display.id)
        return render_template('workload_display.html',display=display,username=username)
    except Exception as msg:
        return "<b>Error : </b>{}".format(str(msg))
    
def workload_insert():
    try:
        username = session.get("name_type")
        if request.method == 'GET':
            return render_template('workload_insert.html',username=username)

        if request.method == 'POST':
            em = session.get('user_email')
            staff_display = staff.query.filter_by(semail=em).first()
            monday = request.form['monday']
            tuesday = request.form['tuesday']
            wednesday = request.form['wednesday']
            thursday = request.form['thursday']
            friday = request.form['friday']
            saturday = request.form['saturday']
            sunday = request.form['sunday']
            date_time = datetime.now()
            staff_id = staff_display.id

            workload_insert_table = workload_report(monday=monday,tuesday=tuesday,wednesday=wednesday,thrusday=thursday,friday=friday,saturday=saturday,sunday=sunday,date_time=date_time,staff_id=staff_id)
            db.session.add(workload_insert_table)
            db.session.commit()
            return redirect('/workload_display')

    except Exception as msg:
        return "<b>Error:</b>{}".format(str(msg))
    
def workload_update(id):
    workload_update_table = workload_report.query.filter_by(id=id).first()
    username = session.get("name_type")
    try: 
        if request.method == 'GET':
            return render_template('workload_update.html',workload_update_table=workload_update_table,username=username)

        if request.method == 'POST':
            if workload_update_table:
                db.session.delete(workload_update_table)
                db.session.commit()

                monday = request.form['monday']
                tuesday = request.form['tuesday']
                wednesday = request.form['wednesday']
                thursday = request.form['thursday']
                friday = request.form['friday']
                saturday = request.form['saturday']
                sunday = request.form['sunday']
                date_time = datetime.now()

                workload_update_table = workload_report(monday=monday,tuesday=tuesday,wednesday=wednesday,thrusday=thursday,friday=friday,saturday=saturday,sunday=sunday,date_time=date_time)
                db.session.add(workload_update_table)
                db.session.commit()
                return redirect(f'/workload_update/{id}')

    except Exception as msg:
        return "<b>Error:</b>{}".format(str(msg))
    
def workload_delete(id):
    try:
        workload_delete_table = workload_report.query.filter_by(id=id).first()
        if request.method == 'GET':
            if workload_delete_table:
                db.session.delete(workload_delete_table)
                db.session.commit()
                return redirect('/workload_display')

    except Exception as msg:
        return "<b>Error:</b>{}".format(str(msg))