from flask_wtf import FlaskForm
from wtforms import Form, FieldList, FormField, StringField, SubmitField
from wtforms.validators import DataRequired


class EntertainerForm(Form):
	entertainer = StringField('Entertainer Name', 
		validators=[DataRequired()])


class EntertainersForm(FlaskForm):
	"""Parent form with dynamic # of entertainers"""
	entertainers = FieldList(
		FormField(EntertainerForm),
		min_entries=2,
		max_entries=5
	)
	submit = SubmitField('Submit')
