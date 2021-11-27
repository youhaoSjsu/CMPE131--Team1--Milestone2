# Give Hint page

### Give hint function

This is an add-on function inside the "View flash card" function. We will add 4 buttons which are "Show Description", "Hide Description", " Show Hint", "Hide Hint"

In routes.py, we added the view flashcard function

```python
@app_Obj.route('/view-flashcards')
def view_flashCards():
    title = 'View Flash Cards'
    flashcards = FlashCards.query.all()
    return render_template('view_flashcards.html',flashcards=flashcards, title=title)
```

### Updated models.py

Add flashCard_hint

```python
class FlashCards(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key = True)
    flashCard_name = db.Column(db.String(256))
    flashCard_description = db.Column(db.String(512))
    flashCard_hint = db.Column(db.String(64))

    def __repr__(self):
        return f'<FlashCard {self.id} : {self.flashCard_name}>'

```

### Updated forms.py

Add flash_hint

```python
class create_FlashCardsForm(FlaskForm):
    flashcard_name = StringField('Flash Card Name', validators = [DataRequired()])
    flashcard_description = StringField('Flash Card Description', validators = [DataRequired()], widget=TextArea() ,render_kw={'style': 'width: 500px'},)
    flashcard_hint = StringField('Flash Card Hint', validators = [DataRequired()])
    save_flashCard = SubmitField('Save Flash Card')
```

### HTML page

This is an updated version of update_flashcard.html

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
