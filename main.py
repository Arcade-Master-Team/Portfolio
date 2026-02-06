# Import
from flask import Flask, render_template,request, redirect
from flask_sqlalchemy import SQLAlchemy



app = Flask(__name__)
app.secret_key = 'my_top_secret_123'
# Estableciendo conexión SQLite
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///diary.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# Página de contenidos en ejecución
@app.route('/')
def index():
    return render_template('index.html')

class Comment(db.Model):
    # Estableciendo los campos de enrada
    # id
    id = db.Column(db.Integer, primary_key=True)
    # Texto
    text = db.Column(db.Text, nullable=False)
    # El correo electrónico del propietario de la tarjeta.
    user_email = db.Column(db.String(100), nullable=False)

    # Objeto de salida y su ID
    def __repr__(self):
        return f'<Comment {self.id}>'

# Habilidades dinámicas
@app.route('/', methods=['POST'])
def process_form():
    button_python = request.form.get('button_python')
    text =  request.form['text']
    email = request.form['email']
    comment = Comment(text=text, user_email=email)

    db.session.add(comment)
    db.session.commit()
    return render_template('index.html', button_python=button_python)


if __name__ == "__main__":
    app.run(debug=True)
