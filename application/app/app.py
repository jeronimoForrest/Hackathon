from bottle import Bottle, static_file, get, post, request
import sqlite3

app = Bottle()
db = sqlite3.connect('users.db')
cursor = db.cursor()

# Handle main page and static
@app.route('/index.html')
def main_page():
    return static_file('index.html', root='./')

# Handle training page
@app.route('/assets/<filepath:path>')
def server_static(filepath):
    return static_file(filepath, root='./assets/')

# Login
@app.route('/assets/login', methods=['GET','POST'])
def login():
    form = Login()
    if form.validate():
        login=request.form['login']
        password=request.form['password'] 
        c = cursor.execute("SELECT login from users where login = (?)", [login])
        userexists = c.fetchone()
        if userexists:
            c = cursor.execute("SELECT password from users where password = (?)", [password])
            passwcorrect = c.fetchone()
            if passwcorrect:
                flash("logged in")
            return static_file('/assets/login.html', root='./')