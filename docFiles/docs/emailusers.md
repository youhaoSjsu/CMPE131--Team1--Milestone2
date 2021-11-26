# Email Users page

### Email users function

```python
@app_Obj.route('/send_message', methods=['GET', 'POST'])
def send_message():
    title = 'Send an Email'
    if  request.method == "POST":
        try:
            email = str(request.form['email'])
            subject = str(request.form['subject'])
            msg_body = str(request.form['message'])

            message = Message(subject, sender="teamonecmpe131@gmail.com", recipients=[email])
            message.body = msg_body
            mail.send(message) #Sends email
            flash("Email Sent!")
            return redirect('/')

        except ConnectionRefusedError as connectionRefusedError_:
            return "Failed to send Email. Please try again later!"
    else:
        return render_template("email.html",title=title)
```

### Update **init**.py file

Before

```python
import os
import flask
from flask_login import LoginManager
from flask_sqlalchemy import SQLAlchemy
from flask_mail import Mail, Message

basedir = os.path.abspath(os.path.dirname(__file__))

app_Obj = flask.Flask(__name__)
app_Obj.config.from_mapping (
    SECRET_KEY = 'it-dont-matter',
    SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'app.db'),
    SQLALCHEMY_TRACK_MODIFICATIONS = False
)

db = SQLAlchemy(app_Obj)
login = LoginManager(app_Obj)
login.login_view = 'loginPage'

from WebsiteApp import routes, models
```

After

```python
import os
import flask
from flask_login import LoginManager
from flask_sqlalchemy import SQLAlchemy
from flask_mail import Mail, Message

basedir = os.path.abspath(os.path.dirname(__file__))

app_Obj = flask.Flask(__name__)

app_Obj.config['MAIL_SERVER'] = 'smtp.gmail.com'
app_Obj.config['MAIL_PORT'] = 465
app_Obj.config['MAIL_USERNAME'] = "teamonecmpe131@gmail.com" #Email goes here
app_Obj.config['MAIL_PASSWORD'] = "Testing69$" # Password goes here (Check discord!)
app_Obj.config["MAIL_USE_TLS"] = False
app_Obj.config['MAIL_USE_SSL'] = True

mail = Mail(app_Obj)

app_Obj.config.from_mapping (
    SECRET_KEY = 'it-dont-matter',
    SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'app.db'),
    SQLALCHEMY_TRACK_MODIFICATIONS = False
)

db = SQLAlchemy(app_Obj)
login = LoginManager(app_Obj)
login.login_view = 'loginPage'

from WebsiteApp import routes, models
```

### HTML page

```
{% extends "base.html" %}

{% block content %}
<!DOCTYPE html>
<body>
    <div class="text-center mx-auto d-block">
        <div class="col-md-8 mx-auto d-block">
            <div class="card-body col-md-8 mx-auto d-block">
                <h3 style='color:black' class="card-title text-center">Send Email</h3>
                <form action="/send_message" method="POST">
                    <label style='color:black' class="text-center"> Recipient Email Address </label>
                    <input type="email" class="form-control" placeholder="Please enter recipient email!" name="email"></input>

                    <label style='color:black' class="text-center"> Subject </label>
                    <input type="text" class="form-control" placeholder="Please enter email Subject!" name="subject"></input>

                    <label style='color:black' class="text-center"> Email Body </label></br>
                    <textarea class='col-md-8 mx-auto d-block' name="email" name="message" placeholder="Message Body" required rows="10"></textarea></br>
                    <input class="btn btn-success" type="submit" style="margin-top: 15px; margin-bottom: 15px; margin-right: 15px;" value="Send Email" name="message">
                </form>
            </div>
        </div>
    </div>
</body>
</html>
{% endblock %}
```
