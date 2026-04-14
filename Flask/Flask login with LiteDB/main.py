from flask import Flask, render_template, request
import sqlite3

app = Flask(__name__)

# DATABASE CONNECTION
def get_db_connection():
    conn = sqlite3.connect('database.db')
    conn.row_factory = sqlite3.Row
    return conn

# HOME
@app.route('/')
def home():
    return render_template("login.html", msg="")

# LOGIN
@app.route('/login', methods=['GET', 'POST'])
def login():
    msg = ''

    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        conn = get_db_connection()
        cursor = conn.cursor()

        cursor.execute(
            "SELECT * FROM users WHERE username=? AND password=?",
            (username, password)
        )
        account = cursor.fetchone()
        conn.close()

        if account:
            msg = 'Logged in Successfully'
            return render_template('welcome.html', name=account['username'], msg=msg)
        else:
            msg = 'Incorrect credentials. Kindly check'

    return render_template('login.html', msg=msg)

# REGISTER
@app.route('/register', methods=['GET', 'POST'])
def register():
    msg = ''

    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        email = request.form['email']

        conn = get_db_connection()
        cursor = conn.cursor()

        cursor.execute(
            "INSERT INTO users (username, password, email) VALUES (?, ?, ?)",
            (username, password, email)
        )
        conn.commit()
        conn.close()

        msg = 'Registration successful! You can now login.'

    return render_template("register.html", msg=msg)

# LOGOUT
@app.route('/logout')
def logout():
    msg = 'Logged out successfully'
    return render_template('login.html', msg=msg)


if __name__ == "__main__":
    app.run(debug=True)
