# API de Usuários - Flask com SQLite

Esta é uma API simples de gerenciamento de usuários que utiliza Flask e SQLite. A API permite cadastrar, listar e deletar usuários, e está documentada utilizando o Swagger.

## 1. Instalação

### Requisitos:

- **Python 3.x** instalado no seu ambiente.
- Um ambiente virtual configurado (opcional, mas recomendado).

### Passos para instalação:

1. Clone o repositório para o seu ambiente local:
   ```bash
   git clone <URL_DO_REPOSITORIO>
   cd <PASTA_DO_REPOSITORIO>
   ```

2. Crie um ambiente virtual (opcional, mas recomendado):
   ```bash
   python -m venv venv
   source venv/bin/activate  # No Windows, use: venv\Scripts\activate
   ```

3. Instale as dependências:
   ```bash
   pip install pysqlite3
   pip install -r requirements.txt
   ```

4. Inicie o servidor Flask:
   ```bash
   python app.py
   ```

5. Acesse a documentação Swagger:
   - Abra o navegador e vá até `http://localhost:5000/apidocs` para acessar a documentação interativa da API.

---

## 2. Endpoints

### Abaixo estão os endpoints disponíveis na API e exemplos de como fazer requisições utilizando **cURL**:

---

### 2.1. Cadastrar Usuário

- **Descrição**: Cadastra um novo usuário.
- **Método**: `POST`
- **URL**: `/cadastrar_usuario`
- **Corpo (JSON)**:
  - `nome`: Nome do usuário (string)
  - `email`: Email do usuário (string)

#### Exemplo cURL:
```bash
curl -X POST http://localhost:5000/cadastrar_usuario \
-H "Content-Type: application/json" \
-d '{
  "nome": "João Silva",
  "email": "joao.silva@example.com"
}'
```

#### Resposta (Exemplo):
```json
{
  "message": "Usuário cadastrado com sucesso"
}
```

---

### 2.2. Listar Usuários

- **Descrição**: Retorna todos os usuários cadastrados.
- **Método**: `GET`
- **URL**: `/buscar_usuario`

#### Exemplo cURL:
```bash
curl -X GET http://localhost:5000/buscar_usuario
```

#### Resposta (Exemplo):
```json
[
  {
    "id": 1,
    "nome": "João Silva",
    "email": "joao.silva@example.com"
  },
  {
    "id": 2,
    "nome": "Maria Souza",
    "email": "maria.souza@example.com"
  }
]
```

---

### 2.3. Deletar Usuário

- **Descrição**: Deleta um usuário específico pelo seu ID.
- **Método**: `DELETE`
- **URL**: `/deletar_usuario/<id>`
- **Parâmetro**: `id` - O ID do usuário a ser deletado (inteiro)

#### Exemplo cURL:
```bash
curl -X DELETE http://localhost:5000/deletar_usuario/1
```

#### Resposta (Exemplo):
```json
{
  "message": "Usuário deletado com sucesso"
}
```

---

## 3. Estrutura do Projeto

```
backend/
│
├── app.py                   # Código principal da API
├── database.db              # Arquivo do banco de dados SQLite
├── requirements.txt         # Dependências do projeto
├── README.md                # Instruções de execução e documentação
└── swagger.yaml             # Especificação OpenAPI
```

## 4. Executando Testes (cURL)

Você pode testar os endpoints usando as instruções `cURL` fornecidas acima. Certifique-se de que a API está rodando no `http://localhost:5000` antes de executar os comandos.

---

### Observações

- Certifique-se de que o banco de dados SQLite (`database.db`) é criado corretamente ao rodar o servidor pela primeira vez.
- Se precisar reiniciar o banco de dados, delete o arquivo `database.db` e reinicie o servidor, que recriará a tabela de usuários.

* [URL Repositorio frontend](https://github.com/fgfrigo/MVP_FrontEnd)

---

@ffrigo 2024
