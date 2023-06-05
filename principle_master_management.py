from flask import Flask
from flask import render_template,request,redirect,abort
import pymysql
from models import *

def principle_master_display():
    try:
        username = session.get("name_type")
        display = principle.query.all()
        return render_template('principle_management_display.html',display=display,username=username)
    except Exception as msg:
        return "<b>Error :<b>{}".format(str(msg))

def principle_master_insert():
    try:
        username = session.get("name_type")
        if request.method == 'GET':
            return render_template('principle_management_insert.html',username=username)

        if request.method == 'POST':
            pname = request.form['pname']
            pemail = request.form['pemail']
            pphone = request.form['pphone']
            apassword = request.form['apassword']
            user_type = request.form['user_type']

            principle_master_insert_table = principle(pname=pname,pemail=pemail,pphone=pphone)
            user_master_insert_table = user(uemail=pemail,upassword=apassword,user_type=user_type,status='Active')
            db.session.add(principle_master_insert_table)
            db.session.add(user_master_insert_table)
            db.session.commit()
            return redirect('/principle_management_display')

    except Exception as msg:
        return "<b>Error :<b>{}".format(str(msg))

def principle_master_update(id):
    principle_master_update_table = principle.query.filter_by(id=id).first()
    user_master_update_table = user.query.filter_by(uemail=principle_master_update_table.pemail).first()
    username = session.get("name_type")
    try: 
        if request.method == 'GET':
            return render_template('principle_management_update.html',principle_master_update_table=principle_master_update_table,username=username,user_master_update_table=user_master_update_table)

        if request.method == 'POST':
            if principle_master_update_table:
                db.session.delete(principle_master_update_table)
                db.session.commit()

                pname = request.form['spname']
                pemail = request.form['pemail']
                pphone = request.form['pphone']
                apassword = request.form['apassword']
                user_type = request.form['user_type']

                principle_master_update_table = principle(pname=pname,pemail=pemail,pphone=pphone)
                user_master_update_table = user(uemail=pemail,upassword=apassword,user_type=user_type,status='Active')
                db.session.add(principle_master_update_table)
                db.session.commit()
                return redirect(f'/principle_management_update/{id}')

    except Exception as msg:
        return "<b>Error:</b>{}".format(str(msg))

def principle_master_delete(id):
    try:
        principle_master_delete_table = principle.query.filter_by(id=id).first()
        user_master_delete_table = user.query.filter_by(uemail=principle_master_delete_table.pemail).first()
        if request.method == 'GET':
            if principle_master_delete_table:
                db.session.delete(principle_master_delete_table)
                db.session.delete(user_master_delete_table)
                db.session.commit()
                return redirect('/principle_management_display')

    except Exception as msg:
        return "<b>Error:</b>{}".format(str(msg))