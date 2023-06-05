from flask import Flask
from flask import render_template,request,redirect,abort
import pymysql
from models import *

def user_master_display():
    try:
        username = session.get("name_type")
        display = user.query.all()
        return render_template('user_management_display.html',display=display,username=username)
    except Exception as msg:
        return "<b>Error :<b>{}".format(str(msg))

def user_master_insert():
    try:
        if request.method == 'GET':
            username = session.get("name_type")
            return render_template('user_management_insert.html',username=username)

        if request.method == 'POST':
            email = request.form['email']
            password = request.form['password']
            user_type = request.form['user_type']
            status = request.form['status']

            user_master_insert_table = user(uemail=email,upassword=password,user_type=user_type,status=status)
            db.session.add(user_master_insert_table)
            db.session.commit()
            return redirect('/user_management_display')

    except Exception as msg:
        return "<b>Error :<b>{}".format(str(msg))

def user_master_update(id):
    user_master_update_table = user.query.filter_by(id=id).first()
    username = session.get("name_type")
    try: 
        if request.method == 'GET':
            return render_template('user_management_update.html',user_master_update_table=user_master_update_table,username=username)

        if request.method == 'POST':
            if user_master_update_table:
                db.session.delete(user_master_update_table)
                db.session.commit()

                sname = request.form['sname']
                semail = request.form['semail']
                sphone = request.form['sphone']
                spost = request.form['spost']

                user_master_update_table = user(sname=sname,semail=semail,sphone=sphone,spost=spost)
                db.session.add(user_master_update_table)
                db.session.commit()
                return redirect(f'/user_management_update/{id}')

    except Exception as msg:
        return "<b>Error:</b>{}".format(str(msg))

def user_master_delete(id):
    try:
        user_master_delete_table = user.query.filter_by(id=id).first()
        if request.method == 'GET':
            if user_master_delete_table:
                db.session.delete(user_master_delete_table)
                db.session.commit()
                return redirect('/user_management_display')

    except Exception as msg:
        return "<b>Error:</b>{}".format(str(msg))