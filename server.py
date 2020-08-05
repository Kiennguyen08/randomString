from flask import Flask, render_template, request, send_from_directory, redirect, url_for
from werkzeug.utils import secure_filename
import json
import os
from io import StringIO
import randomString

UPLOAD_FOLDER = '/Users/kiennguyen/uploads'

# Khởi tạo flask app
app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER



@app.route("/", methods=["GET"])
def _hello_world():
	return "Hello world"

@app.route('/upload',methods=["GET"])
def upload_file():
    return render_template("upload.html")

@app.route('/getfile', methods=['GET','POST'])
def getfile():
    if request.method == 'POST':
        file = request.files['file']
        filename = secure_filename(file.filename)
        myfile = file.read()
        # file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
        randomStr = randomString.main(myfile.decode("utf-8"))
        return randomStr

if __name__ == "__main__":
	print("App run!")
	# Load model
	app.run(debug=False, host="127.0.0.1")
