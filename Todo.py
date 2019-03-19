from flask import Flask,render_template,session,redirect,request
from flask_sqlalchemy import SQLAlchemy
# from src.models import User

HOST = '127.0.0.1'
USERNAME = 'root'
PASSWORD = '123456'
DATABASE = 'flaskdb'  #数据库名
PORT = 3306
DB_URI = 'mysql://{}:{}@{}:{}/{}'.format(USERNAME,PASSWORD,HOST,PORT,DATABASE)

app = Flask(__name__)

# 格式为mysql://{用户名}:{密码}@{host}:{端口}/{数据库名}
app.config['SQLALCHEMY_DATABASE_URI'] = DB_URI
#'mysql+mysqlconnector://root:123456@localhost:3306/flaskdb'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS']='true'

@app.route('/')
def hello_world():
    return render_template('index.html')

@app.route('/login')
def login():
    return render_template('login.html')

@app.route('/login_action', methods=['POST'])
def login_action():
    form = request.form
    username = form.get('username')
    password = form.get('password')
    print(username)
    print(password)
    for a in session:
        print(a)

    session.pop('username', 0)
    return redirect('/')

@app.route('/backLogin')
def back_login():
    session.pop('username',0)
    return redirect('login')


# for session
app.secret_key = '123456'

if __name__ == '__main__':
    app.run(debug=True)
