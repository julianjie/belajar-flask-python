from flask import Flask,render_template,redirect,url_for

app = Flask(__name__)

@app.route('/')
def admin():
    return 'Hello, world!'
@app.route('/hello/<user>')
def home(user):
    return  render_template("index.html",nama_user=user)

@app.route('/fakultas')
def fakultas():
    fakultas = ["FIKR","FEB"];
    return  render_template("fakultas.html",fakultas=fakultas)
@app.route('/prodi')
def prodi():
    prodi = [
        {"nama": "Informatika", "fakultas": "FIKR"},
        {"nama": "Sistem Informasi", "fakultas": "FIKR"},
        {"nama": "Manajemen", "fakultas": "FEB"}
    ]
    return  render_template("prodi.html", prodi=prodi)
@app.route('/contact')
def contact():
    return  render_template("contact.html")

if __name__ == '__main__':
    app.run(debug=True)