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
mysql = pymysql.connect(host=host,user=user,password=password,db=db,)

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
  cursor = mysql.cursor()
  cursor.execute(''' SELECT * FROM dosen ''')
  dosen = cursor.fetchall()
  cursor.close()
  return render_template('dosen.html', dosen=dosen)


@app.route('/dosen/tambah', methods=['GET', 'POST'])
def tambahDosen():
  if request.method == 'GET':
    return render_template('dosen/add.html')
  else:
    nama = request.form['nama']
    univ = request.form['univ']
    jurusan = request.form['jurusan']

    cursor = mysql.cursor()
    cursor.execute(''' INSERT INTO dosen(nama, univ, jurusan) VALUES(%s,%s,%s) ''',(nama,univ,jurusan))
    mysql.commit()
    cursor.close()
    flash('Data added successfully', 'success')
    return redirect(url_for('dosen'))
  return render_template('dosen.html')


@app.route('/dosen/edit/<int:id>', methods=['GET', 'POST'])
def editdosen(id):
  if request.method == 'GET':  
    cursor = mysql.cursor()
    cursor.execute('''
    SELECT * 
    FROM dosen 
    WHERE dosen_id=%s''', (id, ))
    dosen = cursor.fetchone()
    cursor.close()

    return render_template('dosen/edit.html', dosen=dosen)
  else:
    nama = request.form['nama']
    univ = request.form['univ']
    jurusan = request.form['jurusan']

    cursor = mysql.cursor()
    cursor.execute(''' 
    UPDATE dosen 
    SET 
        nama = %s,
        univ = %s,
        jurusan = %s
    WHERE
        dosen_id = %s;
    ''',(nama,univ,jurusan,id))
    
    mysql.commit()
    cursor.close()
    flash('Data updated successfully','success')
    return redirect(url_for('dosen'))

  return render_template('dosen.html')


@app.route('/dosen/delete/<int:id>', methods=['GET'])
def deletedosen(id):
  if request.method == 'GET':
    cursor = mysql.cursor()
    cursor.execute('''
    DELETE 
    FROM dosen 
    WHERE dosen_id=%s''', (id, ))
    mysql.commit()
    cursor.close()

    return redirect(url_for('dosen'))

  return render_template('dosen.html')


if __name__ == '__main__':
  app.run(debug=True)