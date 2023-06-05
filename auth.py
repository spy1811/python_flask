from flask import Flask
from flask import session
from datetime import timedelta
from flask import render_template,request,redirect,session,flash
from flask_session import Session
from models import *
from sqlalchemy import *

def LoginPage():
        error = None
        try:
            if request.method == 'POST':
                username = request.form['username']
                password =request.form['password']
                print("username",username)
                print("password",password)


                usr = user.query.filter_by(uemail=username).first()
                if((not usr)):
                    username = ''
                    session["name_type"] = username
                    session['user_email'] = ''
                    error = 'Credentials not exists. Please try again.'      
                
                elif(usr.upassword != password or (not usr)):
                    username = usr.user_type
                    session["name_type"] = username
                    session['user_email'] = usr.uemail
                    error = 'Invalid Credentials. Please try again.'
                else:
                    username = usr.user_type
                    session["name_type"] = username
                    session['user_email'] = usr.uemail
                    return redirect('/index')

            flash('Wrong email or password')
            return render_template('login.html',error=error)

        except Exception as msg:
            return "<b> Error : </b>"+str(msg)
        
def LogOut():
     try:
          username = session.pop("name_type")
          email = session.pop("user_email")
          return redirect("/")
     except Exception as msg:
            return "<b> Error : </b>"+str(msg)   