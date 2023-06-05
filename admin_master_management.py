from flask import Flask
from flask import render_template,request,redirect,abort,session
import pymysql
from models import *

def admin_master_display():
    try:
        username = session.get("name_type")
        display = admin.query.all()
        return render_template('admin_management_display.html',display=display,username=username)
    except Exception as msg:
        return "<b>Error : </b>{}".format(str(msg))

def admin_master_insert():
    try:
        username = session.get("name_type")
        if request.method == 'GET':
            return render_template('admin_management_insert.html',username=username)

        if request.method == 'POST':
            aname = request.form['aname']
            aemail = request.form['aemail']
            aphone = request.form['aphone']
            apassword = request.form['apassword']
            user_type = request.form['user_type']

            admin_master_insert_table = admin(aname=aname,aemail=aemail,aphone=aphone)
            user_master_insert_table = user(uemail=aemail,upassword=apassword,user_type=user_type,status='Active')
            db.session.add(admin_master_insert_table)
            db.session.add(user_master_insert_table)
            db.session.commit()
            return redirect('/admin_management_display')

    except Exception as msg:
        return "<b>Error:</b>{}".format(str(msg))

def admin_master_update(id):
    admin_master_update_table = admin.query.filter_by(id=id).first()
    user_master_update_table = user.query.filter_by(uemail=admin_master_update_table.aemail).first()
    print(user_master_update_table)
    username = session.get("name_type")
    try:
        if request.method == 'GET':
            return render_template('admin_management_update.html',admin_master_update_table=admin_master_update_table,username=username,user_master_update_table=user_master_update_table)

        if request.method == 'POST':
            if admin_master_update_table:
                db.session.delete(admin_master_update_table)
                db.session.commit()

                aname = request.form['aname']
                aemail = request.form['aemail']
                aphone = request.form['aphone']
                apassword = request.form['apassword']
                user_type = request.form['user_type']

                admin_master_update_table = admin(aname=aname,aemail=aemail,aphone=aphone)
                user_master_update_table = user(uemail=aemail,upassword=apassword,user_type=user_type,status='Active')
                db.session.add(admin_master_update_table)
                db.session.add(user_master_update_table)
                db.session.commit()
                return redirect(f'/admin_management_update/{id}') 

    except Exception as msg:
        return "<b>Error:</b>{}".format(str(msg))

def admin_management_delete(id):
    try:
        username = session.get("name_type")
        admin_master_delete_table = admin.query.filter_by(id=id).first()
        user_master_delete_table = user.query.filter_by(uemail=admin_master_delete_table.aemail).first()
        if request.method == 'GET':
            if admin_master_delete_table and user_master_delete_table:
                db.session.delete(admin_master_delete_table)
                db.session.delete(user_master_delete_table)
                db.session.commit()
                return redirect('/admin_management_display')

    except Exception as msg:
        return "<b>Error:</b>{}".format(str(msg))