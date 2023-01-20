# url_for untuk handel URL dan redirect untuk mengarahkan ke route tertentu
from flask import Flask, render_template, url_for, redirect, request

app = Flask(__name__)

@app.route('/login', methods=['GET', 'POST'])
def login():
  if request.method == 'POST':
    return redirect(url_for('dosen'))
  return render_template('login.html')

@app.route('/dosen')
def dosen():
  return render_template('dosen.html')

if __name__ == '__main__':
  app.run(debug=True)