from flask import Flask, jsonify, request

app = Flask(__name__)

#Importar los datos 
from Usuarios import Usuario

#Rutas, sirve para verificar el servidor (si este responde)
@app.route('/ping')
def ping():
    return jsonify({'mensaje': 'Primera API creada por Angel Sosa Gonzalez'})

#NOTA: las rutas inician por predeterminado con el metodo GET
"""Las API de tipo REST usan el protocolo HTML que se usa para el envio de 
archivos Json, las sentencias usadas en este protocolo son:
- GET
- POST
- DELETE
- PUT 
Entre otras mas pero estas son las pirncipales, este protocolo se usa mucho
para el envio de datos (en este caso son en tipo Json) por medio de internet"""

#Nueva ruta pero ahora usando los metodos para los Json
@app.route('/Usu')
def GETususarios():
    return jsonify(Usuario)
#NOTA para el programador, si usaras metodo GET no lo escribas, este ya esta por determinado
#Si lo escribes te saldra ERROR 

#Ruta para devolver un solo ususario
@app.route('/Usu/<string:Usuario_name>')
def GETususario(Usuario_name):
    UsuarioDatos = [Usuario for Usuario in Usuario
    if Usuario['name'] == Usuario_name]
    #***********************************************
    #Solucionando el error de objetos no encontrados
    if (len(UsuarioDatos) > 0):
        return jsonify({'Usuario': UsuarioDatos[0]})
    #***********************************************
    return jsonify({'Mensaje': 'Vaya, vaya, no sabes que usuarios hay o eres estupido?'})

#Ruta para crear datos
@app.route('/Usu', methods = ['POST'])
def POSTusuario():
    NuevoUsuario = {
        "name": request.json['name'],
        "Edad": request.json['Edad'],
        "Sexo": request.json['Sexo']
    }
    
    #Actualizar la lista
    Usuario.append(NuevoUsuario)
    return jsonify({"Mensaje": "Un nuevo ususario se agrego satisfactoriamente", "Usuario": Usuario})

#Editar una lista Json
@app.route('/Usu/<string:Usuario_name>', methods = ['PUT'])
def PUTusuario(Usuario_name):
    UsuarioEdit = [Usuario for Usuario in Usuario
    if Usuario['name'] == Usuario_name]
    if (len(UsuarioEdit) > 0):
        UsuarioEdit[0]['name'] = request.json['name']
        UsuarioEdit[0]['Edad'] = request.json['Edad']
        UsuarioEdit[0]['Sexo'] = request.json['Sexo']
        return({
            "Mensaje": "Mira se actualizo un nuevo ususario",
            "Usuario": UsuarioEdit[0]
        })
    return ({
            "Mensaje": "Mira no se actualizo un nuevo ususario"
    })

#Ruta para elminar una lista
@app.route('/Usu/<string:Usuario_name>', methods = ['DELETE'])
def DELETEusuario(Usuario_name):
    UsuarioDelete = [Usuario for Usuario in Usuario
    if Usuario['name'] == Usuario_name]
    if (len(UsuarioDelete) > 0):
        Usuario.remove(UsuarioDelete[0])
        return jsonify({
            "Mensaje": "Que hiciste, eliminaste a un usuario",
            "Usuarios": Usuario
        })
    return jsonify({
            "Mensaje": "Haha, tonto ni sabes los nombres de los usuarios",
            "Usuarios": Usuario
        })

#Iniciando la aplcacion
if __name__ == "__main__":
    #Para el desarrollo de este proyecto se usara el puerto 4000
    app.run(debug = True, port = 4000)

