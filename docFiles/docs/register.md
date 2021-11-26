# Register page

### Register function

Import flask library, data from database, and form

```python
from WebsiteApp import app_Obj, db, mail
from WebsiteApp.forms import (LoginForm, RegisterForm, SettingsForm, ToDoListForm, create_FlashCardsForm , pomorodoTimerForm )
from WebsiteApp.models import FlashCards, ToDoList, User
```

Register function in roustes.py which asks users to enter email, password, username.

```python
@app_Obj.route('/')
@app_Obj.route('/home')
def homePage():
    return render_template('home.html')

@app_Obj.route("/register", methods= ['GET', 'POST'])
def registerPage():
    title = "Registration Page"
    form = RegisterForm()
    user = User.query.filter_by(email=form.email.data).first()
    if user is not None:
        flash('Email already exists!')
        return redirect ('/register')
    if form.validate_on_submit():
        if not request.form ['email'] or not request.form ['username']:
            flash('Please enter your username or email')
        if request.form['password'] != request.form['confirmPassword']:
            flash('Password do not match!')
        else:
            hashed_password = generate_password_hash(form.password.data, 'sha256')
            new_user = User(username = form.username.data, email = form.email.data, password=hashed_password)
            db.session.add(new_user)
            db.session.commit()
            flash('New member was successfully added')
            return redirect ('/login')
    return render_template ("register.html", form = form,title=title)
```

### Register form

```python
class RegisterForm(FlaskForm):
    username = StringField ('Username', validators = [DataRequired()])
    email = StringField('Email', validators=[DataRequired()])
    password = PasswordField('Password',validators = [DataRequired()])
    confirmPassword = PasswordField ('Confirm Password',validators = [DataRequired()])
    register_button = SubmitField('Register')
```

### HTML page

```
{% extends "base.html" %}

{% block content %}
<!DOCTYPE html>
<body>
	<div class="text-center mx-auto d-block" style="max-width: 700px; margin-top: 10%; background-color: transparent; color: white;" id='loginBlock'>
		<div class="col-md-8 mx-auto d-block">
			<div class="card-body" style="color: black;">
				<h1><strong>Registration</strong></h1>
				<h6>Please fill your information below</h6>
				<form method="POST" novalidate>
					{{ form.hidden_tag() }}

					<p> {{ form.username.label }} <br>
					{{ form.username(size=32) }}</p>

					<p> {{ form.email.label }} <br>
					{{ form.email(size=32) }}</p>

					<p> {{ form.password.label }} <br>
					{{ form.password(size=32) }}</p>

					<p> {{ form.confirmPassword.label }} <br>
						{{ form.confirmPassword(size=32) }}</p>

					<p> {{ form.register_button() }}</p>
				</form>
			</div>
		</div>
	</div>
</body>
{% endblock %}

```
