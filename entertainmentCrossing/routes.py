from flask import (
	render_template, redirect, url_for, 
	flash, current_app, jsonify, request
)
from entertainmentCrossing.forms import EntertainerForm

import entertainmentCrossing.imdbCompare

@current_app.route('/', methods=['GET', 'POST'])
def see_crossing():
	form = EntertainerForm()
	if request.method == 'POST':
		entertainer1 = request.form['entertainer1']
		entertainer2 = request.form['entertainer2']
		flash(f'Finding the career crossing of {entertainer1} and {entertainer2}...')
		overlapSet = entertainmentCrossing.imdbCompare.run_queries(entertainer1, entertainer2)
		if "Error" in overlapSet:
			flash(f'{overlapSet}', 'error')
			return None
		else:
			overlap = jsonify(
				crossing=list(overlapSet),
				entertainer1=entertainer1,
				entertainer2=entertainer2
				)
			return overlap
	return render_template('find_crossing.html', form=form, overlap=None)

	
	