from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Disciplina(db.Model):
    __tablename__ = 'disciplinas'
    
    id = db.Column(db.Integer, primary_key=True)
    curso = db.Column(db.String(100), nullable=False)
    disciplina = db.Column(db.String(100), nullable=False)
    coordenador = db.Column(db.String(100), nullable=False)
    periodo = db.Column(db.String(10), nullable=False)
    turma = db.Column(db.Integer, nullable=False)
    numero_alunos = db.Column(db.Integer, nullable=False)

    def __repr__(self):
        return f'<Disciplina {self.disciplina}>'
