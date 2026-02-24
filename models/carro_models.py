from db import db # importa DB de DB para gerenciar o banco de dados

class Carro(db.Model): # Definição da classe
    __tablename__ = 'carros' # Define o nome da tabela

    id = db.Column(db.Integer, primary_key=True) # Cria a coluna id
    modelo = db.Column(db.String(80), nullable=False) # Cria a coluna modelo
    marca = db.Column(db.String(80), nullable=False) # Cria a coluna marca
    ano = db.Column(db.Integer, nullable=False) # Cria a coluna ano

    def json(self):
        return {
            'id': self.id, # rtorna o ID do carro
            'modelo': self.modelo, # etorna o MODELO do carro
            'marca': self.marca, # retorna a MARCA do carro
            'ano': self.ano # retorna o ANO do carro
        }
