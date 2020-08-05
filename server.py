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
    data = {"success": False}
    # if 'file' not in request.files:
    #     flash('No file part')
    # if request.files.get("file"):
    #     text = request.files["file"].read()
    #     data["result"] = text
    #     data["success"] = True
    # return json.dumps(data)
    if request.method == 'POST':
        file = request.files['file']
        # f.save(secure_filename(f.filename))       
        # data["result"] = 'hey'
        # data["success"] = True
        # # return 'file uploaded successfully'
        # return json.dumps(data)
            # file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
        # text = f.read()
        # print(StringIO.StringIO(text))
        # return 'file uploaded successfully'
        filename = secure_filename(file.filename)
        myfile = file.read()
        file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
        # file.stream.seek(0) # seek to the beginning of file
        # myfile = file.file 
        # print(myfile)
        # return redirect(url_for('uploaded_file',
        #                         filename=filename))
        randomStr = randomString.main(myfile.decode("utf-8"))
        # print(myfile.decode("utf-8")) 
        return randomStr

# @app.route('/uploads/<filename>')
# def uploaded_file(filename):
#     return send_from_directory(app.config['UPLOAD_FOLDER'],
#                                filename)
    
if __name__ == "__main__":
	print("App run!")
	# Load model
	app.run(debug=False, host="127.0.0.1")
