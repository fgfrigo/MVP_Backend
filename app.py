from flask import Flask, request, jsonify
import sqlite3
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  # Habilitando CORS para permitir requisições de outras origens


# Conexão com o banco de dados SQLite
def get_db_connection():
    conn = sqlite3.connect('database.db')
    conn.row_factory = sqlite3.Row
    return conn

# Criar tabela de usuários
def init_db():
    conn = get_db_connection()
    conn.execute('''
        CREATE TABLE IF NOT EXISTS usuarios (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nome TEXT NOT NULL,
            email TEXT NOT NULL UNIQUE
        )
    ''')
    conn.commit()
    conn.close()

# Rota para cadastrar usuário
@app.route('/cadastrar_usuario', methods=['POST'])
def cadastrar_usuario():
    """
    Cadastrar Usuário
    ---
    tags:
      - Usuários
    parameters:
      - in: body
        name: body
        schema:
          type: object
          required:
            - nome
            - email
          properties:
            nome:
              type: string
            email:
              type: string
        description: Nome e email do usuário
    responses:
      201:
        description: Usuário cadastrado com sucesso
      400:
        description: Erro na requisição
    """
    data = request.get_json()
    nome = data.get('nome')
    email = data.get('email')
    if not nome or not email:
        return jsonify({"message": "Nome e email são obrigatórios"}), 400
    conn = get_db_connection()
    conn.execute('INSERT INTO usuarios (nome, email) VALUES (?, ?)', (nome, email))
    conn.commit()
    conn.close()
    return jsonify({"message": "Usuário cadastrado com sucesso"}), 201

# Rota para buscar todos os usuários
@app.route('/buscar_usuario', methods=['GET'])
def buscar_usuario():
    """
    Buscar Usuários
    ---
    tags:
      - Usuários
    responses:
      200:
        description: Lista de usuários cadastrados
        schema:
          type: array
          items:
            type: object
            properties:
              id:
                type: integer
              nome:
                type: string
              email:
                type: string
    """
    conn = get_db_connection()
    usuarios = conn.execute('SELECT * FROM usuarios').fetchall()
    conn.close()
    return jsonify([dict(usuario) for usuario in usuarios]), 200

# Rota para deletar usuário
@app.route('/deletar_usuario/<int:id>', methods=['DELETE'])
def deletar_usuario(id):
    """
    Deletar Usuário
    ---
    tags:
      - Usuários
    parameters:
      - in: path
        name: id
        type: integer
        required: true
        description: ID do usuário a ser deletado
    responses:
      200:
        description: Usuário deletado com sucesso
      404:
        description: Usuário não encontrado
    """
    conn = get_db_connection()
    result = conn.execute('DELETE FROM usuarios WHERE id = ?', (id,))
    conn.commit()
    conn.close()
    if result.rowcount == 0:
        return jsonify({"message": "Usuário não encontrado"}), 404
    return jsonify({"message": "Usuário deletado com sucesso"}), 200

if __name__ == '__main__':
    init_db()  # Inicializar o banco de dados
    app.run(debug=True)
