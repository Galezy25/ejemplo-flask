from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def bienvenida():
    saludo = 'Bienvenido a la app de Flask'
    return saludo

@app.route('/hola')
def hola():
    saludo = 'Hola mundo!'
    return saludo

@app.route('/hola/alguien')
def hola_alguien():
    saludo = 'Hola alguien!'
    return saludo

@app.route('/hola/plantilla')
def hola_plantilla():
    return render_template('indice.html')

@app.route('/dinamico/saludo')
def dinamico_saludo():
    saludo = 'Hola mundo!'
    suma = 3 + 4
    lista = ['A', 34, 'hola', 3.33, 'Flask', 'etc...']
    return render_template('saludo.html', datos=saludo, suma=suma, lista=lista)

@app.route('/formulario', methods=['GET', 'POST'])
def formulario():
    if request.method == 'POST':
        return request.form['entrada']
    elif request.method == 'GET':
        return render_template('formulario.html')

if __name__ == "__main__":
    app.run()
