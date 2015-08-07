import sqlite3

#create db
db = sqlite3.connect('users.db')


cursor = db.cursor()
login = 'abladablada'
email = 'user@electric-cloud.com'
password = 'Q!W@e3r4'


# Get a cursor object
cursor.execute('''CREATE TABLE users(id INTEGER PRIMARY KEY, login TEXT,
                       email TEXT unique, password TEXT)''')

# Insert user
cursor.execute('''INSERT INTO users(login, email, password)
                  VALUES(:login,:email, :password)''',
                  {'login':login, 'email':email, 'password':password})
print('The user is inserted')

# Get a cursor object
db.commit()

