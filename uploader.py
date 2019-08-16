import os
from flask import Flask, render_template, request
#from sklearn.externals import joblib
import traceback
import pandas as pd
import numpy as np
from werkzeug import secure_filename
import	playsound as playsound
from playsound import playsound

app = Flask(__name__)

UPLOAD_FOLDER='uploader/'

@app.route('/')
def upload():
	return render_template('upload.html')

#Upload file from the web interface	
@app.route('/uploader', methods = ['GET', 'POST'])
def uploader():
	if request.method == 'POST':
		audio = request.files['audio']
		absolute_file = os.path.abspath(UPLOAD_FOLDER + audio.filename)		
		audio.save(absolute_file)
		playsound(absolute_file)
	
	return absolute_file

"""
@app.route('/predict')
def predict():
	audio=uploader()
	if audio:
		try:
			playsound(audio)
		except SoundError:
			return("Not an audio file! Please upload an audio file")
		
	return 0
"""

if __name__ == '__main__':
	app.run(port=10000, debug = True)
