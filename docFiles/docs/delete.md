# Delete Account

### Delete Account function

Delete function in routes.py will ask users to confirm their statement in oder to delete account.

```python
@app_Obj.route("/settings", methods=['GET', 'POST'])
@login_required
def user_SettingsPage():
    title = "Setting Page"
    form = SettingsForm()
    if form.validate_on_submit():
        if(form.delete_account.data != f'Confirm Delete Account {current_user.email}'):
            flash('Unable to delete account')
        else:
            userID = User.query.filter_by(id=current_user.id).first()
            db.session.delete(userID)
            db.session.commit()
            flash('Deleted account. We hope to see you soon!')
            return redirect('/login')
    return render_template('settings.html',form=form,title=title)
```

### Setting form

```python
class SettingsForm(FlaskForm):
    delete_account = StringField('Delete Account',validators = [DataRequired()])
    submit = SubmitField('Delete Account')
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
				<h1><strong>User Settings</strong></h1>
				<h5>Type "Confirm Delete Account {{current_user.email}}" to DELETE account!</h5>
				<form method="POST" novalidate>
					{{ form.hidden_tag() }}
					<p> {{ form.delete_account.label }} <br>
						{{ form.delete_account(size=32) }}</p>

					<p> {{ form.submit() }}</p>
				</form>
			</div>
		</div>
	</div>
</body>
{% endblock %}
```
