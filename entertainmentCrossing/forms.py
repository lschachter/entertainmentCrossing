from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired

class EntertainerForm(FlaskForm):
	entertainer1 = StringField('Entertainer 1', 
		validators=[DataRequired()])

	entertainer2 = StringField('Entertainer 2', 
		validators=[DataRequired()])

	submit = SubmitField('Submit')
