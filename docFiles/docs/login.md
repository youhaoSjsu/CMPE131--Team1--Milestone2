# Login page

### Login Function

Firstly, do not forget to import Flask library

```python
from flask import *  # Imports all the functions at once
from flask_login import current_user, login_required, login_user, logout_user
from flask_mail import Message
from werkzeug.security import generate_password_hash
from werkzeug.wrappers import response
```

In our routes.py, we created loginPage function which ask users to enter their username, and check whether this user registered or not

```python
@app_Obj.route("/login", methods=['GET', 'POST'])
def loginPage():
    title = "Login Page"
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if user is None or not user.check_password(form.password.data):
            flash('Login invalid username or password!')
            return redirect('/login')

        login_user(user, remember=form.remember_me.data)
        flash(f'Successfull Login for requested user {form.username.data}')
        return redirect('/')

    return render_template("login.html", form=form,title=title)
```

Logout function's also included below

```python
@app_Obj.route("/logout", methods=['GET', 'POST'])
@login_required
def logoutPage():
    logout_user()
    flash('You have successfully logged out!')
    return redirect('/login')
```

### Create a database for user information

```python
from datetime import datetime

from flask_login import UserMixin
from werkzeug.security import check_password_hash, generate_password_hash

from WebsiteApp import db, login


class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), unique=True, index=True)
    email = db.Column(db.String(128), unique=True)
    password  = db.Column(db.String(128))

    def set_password(self, password):
        self.password = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password, password)

    def __repr__(self):
        return f'<User {self.id}: {self.username}>'

@login.user_loader
def load_user(id):
    return User.query.get(int(id))
```

### Create a login form in forms.py

```python
from flask.helpers import flash
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField, IntegerField
from wtforms.validators import DataRequired, EqualTo
from wtforms.widgets.core import TextArea

class LoginForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    password = PasswordField('Password')
    remember_me = BooleanField('Remember me')
    submit = SubmitField('Sign in')
```

### HTML file

```
{% extends "base.html" %}

{% block content %}

<!DOCTYPE html>
<body>
    <div class="text-center mx-auto d-block" style="max-width: 700px; margin-top: 10%; background-color: transparent; color: white;" id='loginBlock'>
        <div class="col-md-8 mx-auto d-block">
            <div class="card-body" style="color: black;">
                <h1><strong>Sign In</strong></h1>
                <form method="POST" novalidate>
                    {{ form.hidden_tag() }}

                    <p> {{ form.username.label }} <br>
                    {{ form.username(size=32) }}</p>

                    <p> {{ form.password.label }} <br>
                    {{ form.password(size=32) }}</p>

                    <p> {{ form.remember_me() }} {{ form.remember_me.label }} </p>

                    <p> {{ form.submit() }}</p>
                </form>
            </div>
        </div>
    </div>
</body>
```
