from flask import Flask

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

if __name__ == '__main__':
  app.run(debug=True)