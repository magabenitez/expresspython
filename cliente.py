
from  flask import Blueprint, Flask, jsonify, request


app= Flask (__name__)

cliente= Blueprint('cliente', __name__)
cliente = {
    "5749765": {
        "Nombre": "Magali",
        "Apellidos": "Benitez Vazquez"
    }
}

@cliente.route('/cliente', methods=['POST'])

def Buscarcliente():
 data = request.get_json()
ci= data.get("ci")
if ci in clientes:
    return jsonify({
        "accion": "Success",
        "codRest": "SIN_ERROR",
        "menRes": "OK",
        "ci": 5749765,
        "Nombre": cliente "Magali",
        "Apellidos": "Benitez Vazquez"

    })
else:
    return jsonify ({
        "accion": "Cliente no esta en el sistema",
        "codRes": "ERROR",
        "menRes": "Error cliente",
        "ci":"5749765"
    })