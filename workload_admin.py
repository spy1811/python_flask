from flask import Flask
from flask import render_template,request,redirect,abort,session
import pymysql
from models import *
from datetime import datetime

def workload_admin_display():
    days = ["Monday","Tuesday","Wednesday","Thursday","Friday","Saturday","Sunday"]
    if request.method == 'GET':
        try:
            username = session.get("name_type")
            display = []#workload_report.query.all()
            display_1 = staff.query.all()
            print("------------------",display_1)
            return render_template('workload_admin_display.html',display=display,days=days,username=username,display_1=display_1)
        except Exception as msg:
            return "<b>Error : </b>{}".format(str(msg))
    else:
        try:
            id = request.form['id']
            print('sid',id)
            username = session.get("name_type")
            display = workload_report.query.filter_by(staff_id=id).all()
            print("&&&&&&&&&&&&&&&&&&&&&&&&&",display)
            display_1 = staff.query.all()
            print("------------------",display_1)
            return render_template('workload_admin_display.html',display=display,days=days,username=username,display_1=display_1)
        except Exception as msg:
            return "<b>Error : </b>{}".format(str(msg))