from flask import Blueprint, request, jsonify

cliente = Blueprint('cliente', __name__)

@cliente.route('/cliente', methods=['POST'])
def buscar_cliente():
    data = request.get_json()
    user = data.get('user')
    ci = data.get('ci')

    if user == "magalibenitez" and ci == "5749765":
        respuesta = {
            "accion": "Success",
            "codRes": "SIN_ERROR",
            "menRes": "OK",
            "ci": ci,
            "nombre": "Magali",
            "apellidos": "Benítez"
        }
    else:
        respuesta = {
            "accion": "error de user o contraseña",
            "codRes": "ERROR",
            "menRes": "Error",
            "ci": "error de user o contraseña",
        }

    return jsonify(respuesta)
