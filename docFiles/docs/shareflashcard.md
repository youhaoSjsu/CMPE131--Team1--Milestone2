# Share Flash Card

### Share Flash Card function

Create a flashcard

```python
@app_Obj.route('/create-edit-flashcards', methods = ['GET', 'POST'])
def create_flashcards():
    form = create_FlashCardsForm()
    title = "Create-Edit Flash Cards"

    if form.validate_on_submit():
        new_flashCard = FlashCards(flashCard_name = form.flashcard_name.data, flashCard_description = form.flashcard_description.data)
        try:
            db.session.add(new_flashCard)
            db.session.commit()
            return redirect('/create-edit-flashcards')
        except:
            return flash ('Error: Unable to save Flash Card!')
    else:
        flashcards = FlashCards.query.all()
        return render_template('flashcard.html',form=form, flashcards=flashcards,title=title)

```

Delete a flashcard

```python
@app_Obj.route('/delete-flashcard/<int:id>')
def delete_flashCard(id):
    delete_flashCard = FlashCards.query.get_or_404(id)
    try:
        db.session.delete(delete_flashCard)
        db.session.commit()
        return redirect ('/create-edit-flashcards')
    except:
        return flash ('Error: Unable to delete Flash Card!')

```

Update a flashcard

```python
@app_Obj.route('/edit-flashcard/<int:id>', methods = ['GET', 'POST'])
def edit_flashCard(id):
    update_flashCard = FlashCards.query.get_or_404(id)
    title = "Update Flash Card"
    if request.method == 'POST':
        update_flashCard.flashCard_name = request.form['flashCard_name']
        update_flashCard.flashCard_description = request.form['flashCard_description']
        try:
            db.session.commit()
            return redirect ('/create-edit-flashcards')
        except:
            return flash('Error: could not update a flashcard')
    else:
        return render_template('update_flashcard.html', update_flashCard = update_flashCard, title=title)
```

View flashcard

```python
@app_Obj.route('/view-flashcards')
def view_flashCards():
    title = 'View Flash Cards'
    flashcards = FlashCards.query.all()
    return render_template('view_flashcards.html',flashcards=flashcards, title=title)

```

Share flashcard

```python
@app_Obj.route('/share-flashcards', methods=['POST'])
def share_flashCards():
    flashcards = FlashCards.query.all()
    if request.method == "POST":
        try:
            email = str(request.form['email'])
            subject = 'Flash Cards'
            message = Message(subject, sender="teamonecmpe131@gmail.com", recipients=[email])
            message.body = render_template("share_flashcards.html",flashcards=flashcards)
            message.html = render_template("share_flashcards.html",flashcards=flashcards)
            message.attach = render_template("share_flashcards.html",flashcards=flashcards)
            mail.send(message) #Sends email
            flash("Flashcards Email Sent!")
            return redirect('/')

        except ConnectionRefusedError as connectionRefusedError_:
            return "Failed to send Email. Please try again later!"
    else:
        return render_template("view_flashcards.html")
```

### Create and Update database

```python
class FlashCards(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key = True)
    flashCard_name = db.Column(db.String(256))
    flashCard_description = db.Column(db.String(512))

    def __repr__(self):
        return f'<FlashCard {self.id} : {self.flashCard_name}>'
```

### Share Flash Card form

```python
class create_FlashCardsForm(FlaskForm):
    flashcard_name = StringField('Flash Card Name', validators = [DataRequired()])
    flashcard_description = StringField('Flash Card Description', validators = [DataRequired()], widget=TextArea() ,render_kw={'style': 'width: 500px'},)
    save_flashCard = SubmitField('Save Flash Card')
```

### HTML page

```

{% extends 'base.html'%}
{% block content %}
{% block body %}

<div class="container">
	<div class="card-columns d-flex justify-content-center">
		<div class="card-body">
			<div class="card border-danger mb-3">
				<div class="card-header bg-transparent border-danger" style="color: red;">Old Flash Card Data</div>
				<div class="card-body text-danger">
					<h5 class="card-title"> Title: {{update_flashCard.flashCard_name}} </h5>
					<p class="card-text"> Description: {{update_flashCard.flashCard_description}} </p>
				</div>
			</div>
		</div>
		<div class="card-body">
			<div class="card border-success mb-3" style="max-width: 18rem;">
				<div class="card-header bg-transparent border-success" style="color: green;"> New Flash Card Data</div>
				<div class="card-body text-success">
					<form action = "/edit-flashcard/{{update_flashCard.id}}" method = "POST">
						<h5 class="card-title">
							Title: <input type = "text" name = "flashCard_name" id ="flashCard_name" required>
						</h5>
						<h5 class="card-text">
							Description: <textarea type = "text" name = "flashCard_description" id ="flashCard_description" style="height: 200px; width: 225px;" required></textarea>
						</h5>
						<input class="btn btn-success" type="submit" value="Update">
					</form>
				</div>
			</div>
		</div>
	</div>
</div>
{% endblock %}
{% endblock %}
```
