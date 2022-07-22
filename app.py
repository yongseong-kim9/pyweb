from inspect import Attribute
from werkzeug.utils import secure_filename
from dataclasses import dataclass
from datetime import date
from email.mime import image
from flask import Flask, redirect,render_template, request
from werkzeug.utils import secure_filename
import zzz
# app = Flask(__name__)
# app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024 
#파일 업로드 용량 제한 단위:바이트


app = Flask(__name__)



@app.route('/')
def hellow():
    return render_template('main.html')

@app.route('/upload')
def upload_file():
    inputId = request.args["id"]
    print(inputId)
    # url ="http://127.0.0.1:5500/templates/upload.html?data="+inputId
    # # url ="http://127.0.0.1:5500/templates/upload.html"
    # return redirect(url)
    return render_template('upload.html',data = inputId)

@app.route('/uploader', methods=['GET', 'POST'])
def uploader_file(): 
    inputId = request.args["data"]
    print(inputId)
    
    f = request.files['files1']
    c = request.form['select2']
    mt = request.form['select']
    i = request.form['itme']
    # f.save(os.path.join(app.config['UPLOAD_FOLDER'], f.filename))
    f.save(secure_filename(f.filename))
    # f.save('./img/python.jpg','jpg')
    zzz.ocr(f,c,mt,i,inputId)
    return render_template('check.html')

# if __name__ == "__main__":
#    app.debug = True
#    app.run(host='0.0.0.0')
if __name__ == '__main__':
    app.jinja_env.auto_reload = True
    app.config["TEMPLATES_AUTO_RELOAD"] = True
    app.run(debug=True, host='0.0.0.0')