# Implementando um Banco de Dados NoSQL com PyMongo

import pymongo

# Conectando ao MongoDB Atlas
client = pymongo.MongoClient(
    "mongodb+srv://harmonia:<password>@cluster0.2efxeaz.mongodb.net/")
db = client.test

# Definindo a coleção 'bank' para os documentos de clientes
bank_collection = db.bank

# Inserindo documentos de exemplo
cliente1_doc = {
    "nome": "João",
    "contas": [
        {"numero": "123", "saldo": 1000},
        {"numero": "789", "saldo": 1500}
    ]
}

cliente2_doc = {
    "nome": "Maria",
    "contas": [
        {"numero": "456", "saldo": 2000},
        {"numero": "987", "saldo": 2500}
    ]
}

bank_collection.insert_many([cliente1_doc, cliente2_doc])

# Recuperando informações com base nos pares de chave e valor
for cliente_doc in bank_collection.find():
    print("Cliente:", cliente_doc['nome'])
    for conta in cliente_doc['contas']:
        print("Conta:", conta['numero'], "Saldo:", conta['saldo'])
