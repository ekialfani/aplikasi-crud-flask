from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
  return "hello world"

# routing
# statis
@app.route('/nama')
def nama():
  return "halaman nama"

# dinamis
@app.route('/nama/<string:nama>')
def getNama(nama):
  return "nama anda adalah: {}".format(nama);


# auto reload
# jalankan perintah ini di terminal/cmd
# export FLASK_ENV=development (Untuk Linux)
# set FLASK_ENV=development (Set Windows)


# render html
@app.route('/mahasiswa')
def getMahasiswa():
  return "<h1>Data Mahasiswa</h1>"


# template
# jinja template
# {% ... %} untuk Pernyataan seperti IF dan FOR
# {{ ... }} untuk mencetak variabel/ekspresi ke template
# {# ... #} untuk Komentar yang tidak disertakan 

@app.route('/templates')
def templateMahasiswa():
  kelas = "IF-4201"
  return render_template('mahasiswa.html', kelas=kelas)

@app.route('/dosen')
def getDosen():
  hobbies = ['membaca', 'jalan-jalan', 'nonton']
  return render_template('dosen.html', hobbies=hobbies)



if __name__ == '__main__':
  app.run(debug=True)