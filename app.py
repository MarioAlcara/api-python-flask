from flask import Flask, jsonify

app = Flask(__name__)

# Dados de exemplo
produtos = [
    {"id": 1, "nome": "Produto A", "preco": 10.99},
    {"id": 2, "nome": "Produto B", "preco": 20.99},
    {"id": 3, "nome": "Produto C", "preco": 30.99}
]

# Rota para obter todos os produtos
@app.route('/produtos', methods=['GET'])
def get_produtos():
    return jsonify(produtos)

# Iniciar o servidor
if __name__ == '__main__':
    app.run(debug=True)
