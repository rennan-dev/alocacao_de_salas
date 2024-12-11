from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)


class Disciplina(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    curso = db.Column(db.String(100), nullable=False)
    disciplina = db.Column(db.String(100), nullable=False)
    coordenador = db.Column(db.String(100), nullable=False)
    periodo = db.Column(db.String(10), nullable=False)
    turma = db.Column(db.Integer, nullable=False)
    numero_alunos = db.Column(db.Integer, nullable=False)

    def __repr__(self):
        return f'<Disciplina {self.disciplina}>'

with app.app_context():
    db.create_all()

@app.route('/')
def index():
    disciplinas = Disciplina.query.all()
    return render_template('index.html', disciplinas=disciplinas)

@app.route('/adicionar', methods=['POST'])
def adicionar():
    if request.method == 'POST':
        curso = request.form['curso']
        disciplina = request.form['disciplina']
        coordenador = request.form['coordenador']
        periodo = request.form['periodo']
        turma = request.form['turma']
        numero_alunos = request.form['numero_alunos']
        
        nova_disciplina = Disciplina(
            curso=curso,
            disciplina=disciplina,
            coordenador=coordenador,
            periodo=periodo,
            turma=turma,
            numero_alunos=numero_alunos
        )
        
        db.session.add(nova_disciplina)
        db.session.commit()
        return redirect('/')

@app.route('/editar/<int:id>', methods=['GET', 'POST'])
def editar(id):
    disciplina = Disciplina.query.get(id)
    
    if request.method == 'POST':
        disciplina.curso = request.form['curso']
        disciplina.disciplina = request.form['disciplina']
        disciplina.coordenador = request.form['coordenador']
        disciplina.periodo = request.form['periodo']
        disciplina.turma = request.form['turma']
        disciplina.numero_alunos = request.form['numero_alunos']
        
        db.session.commit()
        return redirect('/')
    
    return render_template('editar.html', disciplina=disciplina)

@app.route('/excluir/<int:id>', methods=['POST'])
def excluir(id):
    disciplina = Disciplina.query.get(id)
    db.session.delete(disciplina)
    db.session.commit()
    return redirect('/')

if __name__ == "__main__":
    app.run(debug=True)
