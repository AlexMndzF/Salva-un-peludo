#from bottle import route, run, get, post, request, template, static_file
import os
from flask import Flask,render_template
from src.photo import uploadimg

api = Flask(__name__)

@api.route("/")
def main():
    return render_template('home.html')
#API:
@api.route('/photo')
def upload_view():
    return render_template('upload.html')


@api.route('/upload', methods=['POST'])
def upload_pthoto():
    img_path = uploadimg()
    if img_path == 'Error':
        print('-----------------------')
        return '<h1>File extension not allowed.<h1/>'
    return 'ok!'


if __name__ == "__main__":
    api.run(debug=True)








'''#Conexion:
port = int(os.getenv('PORT', 8080))
host = os.getenv('IP','0.0.0.0')
run(host=host, port=port, debug=True)
#run(host='0.0.0.0', port=8080)'''