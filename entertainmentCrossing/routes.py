from flask import (
	render_template, redirect, url_for, 
	flash, current_app, jsonify, request
)
from entertainmentCrossing.forms import EntertainersForm
import entertainmentCrossing.imdbCompare

@current_app.route('/', methods=['POST'])
def see_crossing():
	try:
		form = EntertainersForm()
		if not form.validate_on_submit():
			return jsonify(success=0, error_msg="the form request is invalid")
		entertainers = [e["entertainer"] for e in form.entertainers.data]
		compare_pages = entertainmentCrossing.imdbCompare.ComparePages()
		overlap_dict = compare_pages.run_queries(entertainers)
		if overlap_dict.get('error_msg'):
			overlap_dict["success"] = 0
		else:
			overlap_dict["success"] = 1
		overlap = jsonify(overlap_dict)
		return overlap
	except Exception as e:
		return jsonify(success=0, error_msg=str(e))
	
	
@current_app.route('/', methods=['GET'])
def index():
	form = EntertainersForm()
	return render_template('find_crossing.html', form=form)
	