#from bottle import route, run, get, post, request, template, static_file
import os
from flask import Flask,render_template, url_for, request, session, redirect
from src.photo import uploadimg
from src.database import get_vectors_names, cleandir
from src.recomender import recomender
from src.database import load_database
from src.mongo import mongo_add,users
import bcrypt

api = Flask(__name__)

api.config["SECRET_KEY"]
cloud_url = os.getenv('CLOUDINARY_URL')
os.environ['CLOUDINARY_URL'] = cloud_url

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
    print(f'===============>{img_path}<===============')
    if img_path == 'Error':
        return render_template('error_invalid_Format.html')
    elif img_path == 'Error no image':
        return render_template('error_no_image.html')
    vector,names = get_vectors_names()
    result, name = recomender(vector,names)
    image = result
    cleandir('test/*')
    return render_template('uploaded.html', image=image, name=name[0], aso=name[1] )

@api.route('/asoc', methods=['POST', 'GET'])
def upload_database():
    print('=========>Upload Function<=========')
    image_not_save = []
    if request.method == 'POST': #and 'photo' in request.files
        print('=========>Method POST found<=========')
        for image in request.files.getlist('photos'):
            name, ext = os.path.splitext(image.filename)
            if ext in ('.png','.jpg','.jpeg'):
                image.save(f'database/{image.filename}')
                print(f'=========>{image.filename} Upload!<=========')
            else:
                image_not_save.append(image.filename)
        list_pictures = load_database('database/')
        mongo_add(list_pictures)
        cleandir('database/*')
        return render_template('private_uploaded.html')
    return render_template('private_upload.html')

#LOGIN:
@api.route('/log')
def log():
    if 'username' in session:
        return 'You are logged in as ' + session['username']

    return render_template('login.html')

@api.route('/login', methods=['POST'])
def login():
    login_user = users.find_one({'name' : request.form['username']})
    print('========>',request.form['pass'].encode('utf-8'))
    print('========>',login_user['password'])
    if login_user:
        if bcrypt.hashpw(request.form['pass'].encode('utf-8'), login_user['password']) == login_user['password']:
            session['username'] = request.form['username']
            return render_template('private_upload.html')
            
    return 'Invalid username/password combination'

@api.route('/register', methods=['POST', 'GET'])
def register():
    if request.method == 'POST':
        existing_user = users.find_one({'name' : request.form['username']})

        if existing_user is None:
            hashpass = bcrypt.hashpw(request.form['pass'].encode('utf-8'), bcrypt.gensalt())
            users.insert({'name' : request.form['username'], 'password' : hashpass})
            session['username'] = request.form['username']
            return render_template('login.html')
        
        return 'That username already exists!'

    return render_template('register.html')
@api.route("/logout")
def logout():
    session.pop('username')
    return render_template('home.html')

if __name__ == '__main__':
    api.secret_key = 'mysecret'
    api.run(debug=True)