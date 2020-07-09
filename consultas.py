from pymongo import MongoClient

cliente = MongoClient('localhost', 27017)
#db = cliente.ejemplo_pymongo
#coleccion = db.prueba
db = cliente['ejemplo']
#db = cliente.ejemplo
coleccion = db.test

def obtener_todo():
    cursor = coleccion.find()
    return list(cursor)

def obtener_uno(titulo):
    resultado = coleccion.find_one({'nombre': titulo})
    return resultado

def insertar_uno(datos):
    id = coleccion.insert_one(datos)
    return id

def editar_uno(nombre, datos):
    resultado = coleccion.update_one({'nombre': nombre}, 
        {'$set': {'correo': datos['correo']}})
    return str(resultado.modified_count)