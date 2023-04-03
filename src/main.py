from flask import Flask, render_template, redirect, request
from flask_sqlalchemy import SQLAlchemy
# from flask_script import Manager

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///coordenate.db'
db = SQLAlchemy(app)
class Coordenate(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    x = db.Column(db.Integer)
    y = db.Column(db.Integer)
    z = db.Column(db.Integer)
    r = db.Column(db.Integer)
@app.cli.command()
def createdb():
    db.create_all()

@app.route('/')
def index():
    Coordenates = Coordenate.query.all()
    return render_template('index.html', Coordenates=Coordenates)

@app.route('/coord', methods=['POST'])
def coord():
    coord = Coordenate(
        x = request.form['x'],
        y = request.form['y'],
        z = request.form['z'],
        r = request.form['r']
    )
    db.session.add(coord)
    db.session.commit()
    return redirect('/')

# manager = Manager(app)

if __name__ == '__main__':
    # manager.run()
    app.run(host='0.0.0.0', port=3000, debug=True)