from flask import Flask, render_template, request, jsonify, session, redirect, url_for, send_from_directory
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager
from werkzeug.utils import secure_filename
import csv
import os
from forms import UploadCSVForm
import sqlite3
from werkzeug.security import check_password_hash
from datetime import datetime, timedelta, timezone
from flask_migrate import Migrate


app = Flask(__name__)
app.secret_key = 'verysecretkey'
bcrypt = Bcrypt(app)
app.config['UPLOAD_FOLDER'] = 'uploads'
app.config['ALLOWED_EXTENSIONS'] = {'csv'}
class Config:
    SQLALCHEMY_DATABASE_URI = 'sqlite:///users.db'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in app.config['ALLOWED_EXTENSIONS']

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/patversmju')
def patversmju():
    return render_template('index1.html')

@app.route('/majdzivnieks')
def majdzivnieks():
    return render_template('index2.html')

@app.route('/kopsana')
def kopsana():
    return render_template('index3.html')

@app.route('/registeraccount')
def registeraccount():
    return render_template('registration.html')

@app.route('/loginaccount')
def loginaccount():
    return render_template('login.html')

@app.route('/users')
def view_users():
    conn = sqlite3.connect('database.db')
    c = conn.cursor()
    users = c.fetchall()
    conn.close()
    users = User.query.all() 
    return render_template('users.html', users=users)

@app.route('/users/<username>')
def get_user(username):
    user = User.query.filter_by(username=username).first()
    if user:
        return {'username': user.username}
    return {'message': 'User not found'}, 404

def init_db():
    conn = sqlite3.connect('example.db')
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS users (id INTEGER PRIMARY KEY, name TEXT)''')
    conn.commit()
    conn.close()

@app.route('/add', methods=['POST'])
def add_user():
    name = request.form['name']
    conn = sqlite3.connect('database.db')
    c = conn.cursor()
    c.execute('INSERT INTO users (name) VALUES (?)', (name,))
    conn.commit()
    conn.close()
    return 'Liegtne pievienota!'

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.db' 
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

UPLOAD_FOLDER = 'uploads'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['ALLOWED_EXTENSIONS'] = {'csv'}

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in app.config['ALLOWED_EXTENSIONS']

@app.route('/upload')
def upload():
    return render_template('upload.html')

@app.route('/upload', methods=['POST'])
def upload_file():
    if 'file' not in request.files:
        return redirect(request.url)
    file = request.files['file']
    if file and allowed_file(file.filename):
        filename = os.path.join(app.config['UPLOAD_FOLDER'], file.filename)
        file.save(filename)

        with open(filename, newline='') as csvfile:
            reader = csv.reader(csvfile)
            data = list(reader) 

        return render_template('upload.html', filename=file.filename, data=data)

    return redirect(url_for('upload'))

db = SQLAlchemy(app)
migrate = Migrate(app, db)

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    password = db.Column(db.String(128), nullable=False)
    last_login = db.Column(db.DateTime, nullable=True)
    age = db.Column(db.Integer, nullable=True)  

with app.app_context():
    db.create_all()

@app.route('/register', methods=['POST'])
def register():
    data = request.json 
    username = data.get('username')
    password = data.get('password')

    if User.query.filter_by(username=username).first():
        return jsonify({'message': 'Lietotājs jau ir reģistrēts'}), 400

    hashed_password = bcrypt.generate_password_hash(password).decode('utf-8')

    new_user = User(username=username, password=hashed_password)
    db.session.add(new_user)
    db.session.commit()

    return jsonify({'message': 'Reģistrācija veiksmīga!'}), 201

@app.route('/')
def home():
    return render_template('login.html')

@app.route('/login', methods=['POST'])
def login():
    username = request.form['username']
    password = request.form['password']
    
    user = User.query.filter_by(username=username).first()
    if user and bcrypt.check_password_hash(user.password, password):
        User.last_login = datetime.now(timezone.utc)
        db.session.commit()
        return redirect(url_for('dashboard'))
    else:
        return redirect(url_for('errorror'))
    
@app.route('/delete_inactive_users')
def delete_inactive_users():
    two_day_ago = datetime.now(timezone.utc) - timedelta(days=2)
    inactive_users = User.query.filter(User.last_login < two_day_ago).all()
    
    for user in inactive_users:
        db.session.delete(user)
    
    db.session.commit()
    return f'{len(inactive_users)} lietotāji dzēsti!'
    
@app.route('/errorror')
def errorror():
    return render_template('errorror.html')

@app.route('/dashboard')
def dashboard():
    return render_template('success.html')

@app.route('/age_verification', methods=['GET', 'POST'])
def age_verification():
    if request.method == 'POST':
        age = request.form.get('age')
        if age and age.isdigit() and int(age) >= 16:
            session['is_sixteen_or_older'] = True
            return redirect(url_for('index'))
        else:
            return render_template('age_restricted.html')
    return render_template('age_verification.html')

@app.before_request
def check_age():
    allowed_routes = ['age_verification', 'static']
    if 'is_sixteen_or_older' not in session and request.endpoint not in allowed_routes:
        return redirect(url_for('age_verification'))

if __name__ == "__main__":
    app.run(debug=True)