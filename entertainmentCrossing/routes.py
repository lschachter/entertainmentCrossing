from flask import (
	render_template, redirect, url_for, 
	flash, current_app, jsonify, request
)
from entertainmentCrossing.forms import EntertainerForm

import entertainmentCrossing.imdbCompare

@current_app.route('/', methods=['POST'])
def see_crossing():
	entertainer1 = request.form['entertainer1']
	entertainer2 = request.form['entertainer2']
	flash(f'Finding the career crossing of {entertainer1} and {entertainer2}...', 'success')
	overlap_dict = entertainmentCrossing.imdbCompare.run_queries(entertainer1, entertainer2)
	if type(overlap_dict) == str:
		flash(f'{overlap_dict}', 'danger')	
	else:
		overlap = jsonify(
			crossing=overlap_dict,
			e1=entertainer1,
			e2=entertainer2
			)
		return overlap
	

	
@current_app.route('/', methods=['GET'])
def index():
	form = EntertainerForm()
	return render_template('find_crossing.html', form=form)