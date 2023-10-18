from flask import Flask, render_template,request,session,redirect,url_for
import mysql.connector

connection = mysql.connector.connect(host='localhost', port='3306', database='logindb', user='root',password='')


cursor = connection.cursor()
app = Flask(__name__)
app.secret_key = "seper secret key"

@app.route("/")
def index():
    return render_template("login.html")

@app.route("/home")
def home():
    return render_template('home.html', email=session['email'])

@app.route('/login',methods=['GET','POST'])
def login():
    msg=''
    if request.method=='POST':
        firstname = request.form['firstname']
        lastname = request.form['lastname']
        email = request.form['email']
        password = request.form['password']

        cursor = cursor.cursor(dictionary=True)

        cursor.execute('SELECT * FROM user WHERE email = %s AND password = %s', (email,password))
        account=cursor.fetchone()

        if account:
            session['loggein']= True
            session['email']= account[1]
            return redirect(url_for('home'))
        else:
            msg='Incorrect email/password. Try again!'
    return render_template('index.html', msg =msg)
