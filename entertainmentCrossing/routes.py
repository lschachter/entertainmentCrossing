from flask import (
	render_template, redirect, url_for, 
	flash, current_app, jsonify, request
)
from entertainmentCrossing.forms import EntertainerForm
import entertainmentCrossing.imdbCompare

@current_app.route('/', methods=['POST'])
def see_crossing():
	try:
		entertainer1 = request.form['entertainer1']
		entertainer2 = request.form['entertainer2']
		overlap_dict = entertainmentCrossing.imdbCompare.run_queries(entertainer1, entertainer2)
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
	form = EntertainerForm()
	return render_template('find_crossing.html', form=form)
	