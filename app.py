from flask import Flask, jsonify, request
from flask_cors import CORS
import firebase_admin
from firebase_admin import credentials, firestore
import os 
import json
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)
CORS(app)

#Pega a variável de ambiente e converte para json
FB_KEY = json.loads(os.getenv('CONFIG_FIREBASE'))

cred = credentials.Certificate(FB_KEY)
firebase_admin.initialize_app(cred)

#Conectando com o firestore da Firebase
db = firestore.client()

#*Rota principal de teste*
@app.route('/', methods = ['GET'])
def index():
    return 'API está ligada!'
    

#Listar charadas
@app.route('/clientes', methods=['GET'])
def clientes_lista():
    clientes = []
    lista = db.collection('cadastro').stream()
    for item in lista:
        clientes.append(item.to_dict()) #Transforma em dicionário cada charada do firebase

    if clientes:
        return jsonify(clientes), 200
    
    else:
        return jsonify({'Mensagem': 'Erro! Nenhuma charada encontrada.'}), 404

@app.route('/clientes/<cpf>', methods=['GET'])
def busca_por_cpf(cpf):
    clientes_ref = db.collection('cadastro')
    query = clientes_ref.where('cpf', '==', cpf).limit(1) # Busca o primeiro cliente com esse CPF
    resultados = query.get()

    if resultados:
        for doc in resultados:
            return jsonify(doc.to_dict()), 200
    else:
        return jsonify({'mensagem': 'Erro! Cliente não encontrado.'}), 404
    
#Rota método POST, adicionar charada
@app.route('/clientes', methods=['POST'])
def adicionar_clientes():
    dados = request.json

    if "cpf" not in dados or "nome" not in dados:
        return jsonify({'mensagem': 'Erro! Campos CPF e NOME são obrigatórios'}), 400
    
    #Contador
    contador_ref = db.collection('controle_id').document('contador')
    contador_doc = contador_ref.get().to_dict()
    ultimo_id = contador_doc.get('id')
    novo_id = int(ultimo_id) + 1
    contador_ref.update({'id': novo_id})

    db.collection('cadastro').document(str(novo_id)).set({
        "id": novo_id,
        "nome": dados['nome'],
        "cpf": dados['cpf'],
        "status": 'ativo'

    })

    return jsonify({'mensagem': 'Cadastro concluído com sucesso!'}), 201

#Rota metódo PUT, alterar cadastros
@app.route('/clientes/<id>', methods=['PUT'])
def alterar_cadastro(id):
    dados = request.json

    if "cpf" not in dados or "nome" not in dados:
        return jsonify({'mensagem': 'Erro! Campos cpf e nome são obrigatórios'}), 400
    
    doc_ref = db.collection('cadastro').document(id)
    doc = doc_ref.get()

    if doc.exists:
        atualizacao = {
            "cpf": dados['cpf'],
            "nome": dados['nome']
        }

        # Só atualiza o status se ele estiver presente no JSON recebido
        if 'status' in dados:
            atualizacao["status"] = dados["status"]

        doc_ref.update(atualizacao)
        return jsonify({'mensagem': 'Cadastro alterado com sucesso!'}), 200
    
    else:
        return jsonify({'mensagem': 'Erro! Cadastro não encontrado'}), 404

#Rota método DELETE, deletar charada
@app.route('/clientes/<id>', methods=['DELETE'])
def excluir_cliente(id):
    doc_ref = db.collection('cadastro').document(id)
    doc = doc_ref.get()

    if not doc.exists:
        return jsonify({'mensagem': 'Erro! Cliente não encontrado.'}), 404

    doc_ref.delete()
    return jsonify({'mensagem': 'Cliente excluída com sucesso!'})

@app.route('/clientes/id/<id>', methods=['GET'])
def buscar_por_id(id):
    doc_ref = db.collection('cadastro').document(id)
    doc = doc_ref.get()

    if doc.exists:
        return jsonify(doc.to_dict()), 200
    else:
        return jsonify({'mensagem': 'Erro! Cliente não encontrado.'}), 404
if __name__ == '__main__':
    app.run(host="0.0.0.0", port=8000)