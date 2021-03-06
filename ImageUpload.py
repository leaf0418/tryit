import os
from flask import Flask, flash, request, redirect, url_for, render_template, session, Response
from werkzeug.utils import secure_filename
from flask import send_from_directory
import ImageProcess, ImageMasaic
from datetime import datetime

UPLOAD_FOLDER = './static'
ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'gif'}

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER


def allowed_file(filename):
	return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


@app.route('/', methods=['GET', 'POST'])
def upload_file():
	# global patch_size
	if request.method == 'POST':
		# check if the post request has the file part
		if 'file' not in request.files:
			# flash('No file part')
			return redirect(request.url)
		file = request.files['file']
		patch_size = request.form.get('patch')
		# if user does not select file, browser also
		# submit an empty part without filename
		if file.filename == '':
			# flash('No selected file')
			return redirect(request.url)
		if file and allowed_file(file.filename):
			filename = secure_filename(file.filename)
			filename = '{}.jpg'.format(str(datetime.now()))
			fpath = os.path.join(app.config['UPLOAD_FOLDER'], filename).replace('\\', '/')
			file.save(fpath)
			return redirect(url_for('showfile', filename=filename, patch=patch_size))
	return render_template('upload.html', pagetitle="Upload page")


@app.route('/show/<filename>/<patch>')
def showfile(filename, patch):
	# global patch_size
	fpath = os.path.join(app.config['UPLOAD_FOLDER'], filename).replace('\\', '/')
	ImageMasaic.do_Mosaic(fpath, patch=patch)
	fname = filename.rsplit('.', 1)
	newfile = fname[0] + "_q." + ''.join(fname[1:])
	print(newfile)
	return render_template('image.html', pagetitle="Show image", fn=newfile)
	# return render_template('image.html', pagetitle="Show image", fn=filename)


if __name__ == '__main__':
	app.run(host='0.0.0.0', debug=True)