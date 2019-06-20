from flask import render_template, flash, current_app
from entertainmentCrossing.forms import EntertainerForm

import entertainmentCrossing.imdbCompare

@current_app.route('/', methods=['GET', 'POST'])
def findOverlap():
  form = EntertainerForm()
  if form.validate_on_submit():
  	entertainer1 = form.entertainer1.data
  	entertainer2 = form.entertainer2.data
  	flash(f'Finding the career overlap of {entertainer1} and {entertainer2}! Please allow 10 seconds before clicking again.', 'success')
  	overlap = entertainmentCrossing.imdbCompare.run_queries(entertainer1, entertainer2)
  	if "Error" in overlap:
  		flash(f'{overlap}', 'error')
  	else:
  		flash(f'{overlap}', 'success')
  return render_template('findOverlap.html', form=form)
