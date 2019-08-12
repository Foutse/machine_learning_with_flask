import os
from flask import Flask, render_template, request
from werkzeug import secure_filename
app = Flask(__name__)

UPLOAD_FOLDER='Path_to/uploader/'

@app.route('/')
def upload():
	return render_template('upload.html')

	
@app.route('/uploader', methods = ['GET', 'POST'])
def uploader():
	if request.method == 'POST':
		f = request.files['file']
		absolute_file = os.path.abspath(UPLOAD_FOLDER + f.filename)		
		f.save(absolute_file)
		
	
	return absolute_file
	
		
if __name__ == '__main__':
	app.run(port=6003, debug = True)
