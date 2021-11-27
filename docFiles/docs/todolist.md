# To-do List page

### To-do list function

Create a task

```python
@app_Obj.route ('/todolist', methods = ['GET', 'POST'])
def todolistPage():
    form = ToDoListForm()
    title = "To-Do-List"
    if request.method == 'POST':
        task_content = request.form['task_name']
        new_task = ToDoList(task_name = task_content)
        try:
            db.session.add (new_task)
            db.session.commit()
            return redirect('/todolist')
        except:
            return flash ('Error: could not add a task')
    else:
        tasks = ToDoList.query.all()
        return render_template ("todolist.html", tasks = tasks, form=form,title=title)


```

Update a task

```python
@app_Obj.route ('/update/<int:id>', methods = ['GET', 'POST'])
def update(id):
    form = ToDoListForm()
    title = "Update Task"
    task = ToDoList.query.get_or_404(id)
    if request.method == 'POST':
        task.task_name = request.form['task_name']
        try:
            db.session.commit()
            return redirect ('/todolist')
        except:
            return flash('Error: could not update a task')
    else:
        return render_template('update.html', task = task, form=form,title=title)

```

Delete a task

```python
@app_Obj.route('/delete/<int:id>')
def delete(id):
    delete_task = ToDoList.query.get_or_404(id)
    try:
        db.session.delete(delete_task)
        db.session.commit()
        return redirect ('/todolist')
    except:
        return flash ('Error: could not delete a task')
```

### To-do list form

```python
class ToDoListForm(FlaskForm):
    task_name = StringField ('Enter a task', validators = [DataRequired()])
    add_task_button = SubmitField('Add task')

```

### To-do list database

```python
class ToDoList(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key = True)
    task_name = db.Column(db.String(64))
    complete = db.Column(db.Boolean)

    def __repr__ (self):
        return f'<Task {self.id} : {self.task_name}>'
```

### HTML page

Create a task page todolist.html

```
{% extends "base.html" %}
{% block content %}
<div class="text-center">
	<h1 style= 'color:black'><strong>To Do List </strong></h1>
	<form method = "POST" novalidate>
		{{form.hidden_tag()}}
		<p style= 'color:black'> {{form.task_name.label}} {{form.task_name (size=64)}}
			{{form.add_task_button (size= 32)}} </p>
	<table style="margin-left: 900px;">
		<tr>
			<th style= 'color:black'> Task </th>
			<th style= 'color:black'> Actions </th>
		</tr>

		{% for task in tasks %}
		<tr>
			<td style= 'color:black;'> {{task.task_name}}</td>
			<td>
				<a href="delete/{{task.id}}" style="margin-left: 10px;">Delete</a>
				<a href="update/{{task.id}}">Update</a>
			</td>
		</tr>
		{% endfor %}
	{% block body %}
	{% endblock%}
	</table>
</div>
{% endblock %}

```

Update page update.html

```
{% extends 'base.html'%}
{% block content %}
{% block body %}
<div class = "task_name">
	<h3 style="color: black;"> <strong> Update Task </strong> </h3>
	<form action = "/update/{{task.id}}" method = "POST">
		<input type = "text" name = "task_name" id ="task_name" value = "{{task.content}}">
		<input type = "submit" value = "Update">
	</form>
</div>
{% endblock %}
{% endblock %}

```
