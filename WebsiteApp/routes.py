from flask import * #Imports all the functions at once (render_template,flash,etc.)

from WebsiteApp import db, app_Obj


@app_Obj.route('/')
@app_Obj.route('/home')
def homePage():
    return render_template('home.html')

@app_Obj.route('/register')
def registerPage():
    return 'Register Page'

@app_Obj.route('/login')
def loginPage():
    return 'Login Page'