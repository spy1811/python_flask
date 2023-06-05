from flask import Flask
from flask import render_template,request,redirect,abort
import pymysql
from models import *

def notice_board_display():
    username = session.get("name_type")
    try:
        display = notice_board.query.all()
        return render_template('notice_board_display.html',display=display,username=username)
    except Exception as msg:
        return "<b>Error :<b>{}".format(str(msg))
    
def notice_board_insert():
    try:
        username = session.get("name_type")
        if request.method == 'GET':
            return render_template('notice_board_insert.html',username=username)

        if request.method == 'POST':
            board_name = request.form['board_name']
            board_content = request.form['board_content']

            notice_board_insert_table = notice_board(notice_name=board_name, notice_content=board_content)
            db.session.add(notice_board_insert_table)
            db.session.commit()
            return redirect('/notice_board_display')

    except Exception as msg:
        return "<b>Error :<b>{}".format(str(msg))
    
def notice_board_update(id):
    notice_board_update_table = notice_board.query.filter_by(id=id).first()
    try: 
        if request.method == 'GET':
            username = session.get("name_type")
            return render_template('notice_board_update.html',username=username,notice_board_update_table=notice_board_update_table)

        if request.method == 'POST':
            if notice_board_update_table:
                db.session.delete(notice_board_update_table)
                db.session.commit()

                board_name = request.form['board_name']
                board_content = request.form['board_content']

                notice_board_update_table = notice_board(notice_name=board_name, notice_content=board_content)
                db.session.add(notice_board_update_table)
                db.session.commit()
                return redirect(f'/notice_board_update/{id}')

    except Exception as msg:
        return "<b>Error:</b>{}".format(str(msg))
    
def notice_board_delete(id):
    try:
        notice_board_delete_table = notice_board.query.filter_by(id=id).first()
        if request.method == 'GET':
            if notice_board_delete_table:
                db.session.delete(notice_board_delete_table)
                db.session.commit()
                return redirect('/notice_board_display')

    except Exception as msg:
        return "<b>Error:</b>{}".format(str(msg))