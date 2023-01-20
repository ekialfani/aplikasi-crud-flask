# url_for untuk handel URL dan redirect untuk mengarahkan ke route tertentu
from flask import Flask, render_template, url_for, redirect, request, session, flash
import pymysql


app = Flask(__name__)
app.secret_key = 'asdfghjkl12345fdsa_fdsakld8rweodfds'

# mysql config
host = 'localhost'
user = 'root'
password = ''
db = 'universitas'
conn = pymysql.connect(host=host,user=user,password=password,db=db,)

@app.route('/login', methods=['GET', 'POST'])
def login():
  if request.method == 'POST':
    if request.form['username'] != 'admin' and request.form['password'] != '123':
      flash('Invalid username/password', 'danger')
    else:
      session['logged_in'] = True
      flash('Login successful', 'success')
      return redirect(url_for('dosen'))
  return render_template('login.html')

@app.route('/logout')
def logout():
  session.pop('logged_in', None)
  flash('Logout successful', 'success')
  return redirect(url_for('login'))

@app.route('/dosen')
def dosen():
  cursor = conn.cursor()
  cursor.execute(''' SELECT * FROM dosen ''')
  dosen = cursor.fetchall()
  cursor.close()
  return render_template('dosen.html', dosen=dosen)

if __name__ == '__main__':
  app.run(debug=True)