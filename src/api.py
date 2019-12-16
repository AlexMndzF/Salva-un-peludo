from bottle import route, run, get, post, request, template, static_file
import os

#Funcion para usar el archivo estatico de CSS:
@route('/style.css')
def server_static(path='style.css'):
    return static_file(path, root='static/')




#API:
@get('/')
def main():
    return template('home')
@route('/photo')
def upload():
    return template('upload')

@get('/up')
def up():
    return template('up')

@route('/upload', method='POST')
def do_login():
    upload     = request.files.get('upload')
    name, ext = os.path.splitext(upload.filename)
    '''if ext not in ('png','jpg','jpeg'):
        return 'File extension not allowed.'''
    upload.save(f'{name}.jpg') # appends upload.filename automatically
    return 'OK'




#Conexion:
port = int(os.getenv('PORT', 8080))
host = os.getenv('IP','0.0.0.0')
run(host=host, port=port, debug=True)
#run(host='0.0.0.0', port=8080)