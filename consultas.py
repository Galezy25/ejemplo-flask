from pymongo import MongoClient

cliente = MongoClient('localhost', 27017)
#db = cliente.ejemplo_pymongo
#coleccion = db.prueba
db = cliente['test-inventory']
coleccion = db.test

def obtener_todo():
    cursor = coleccion.find()
    return list(cursor)

def obtener_uno(titulo):
    resultado = coleccion.find_one({'title': titulo})
    return resultado

def insertar_uno(datos):
    id = coleccion.insert_one(datos)
    return id

def editar_uno(titulo, datos):
    resultado = coleccion.update_one({'title': titulo}, 
        {'$set': {'description': datos['description']}})
    return str(resultado.modified_count)