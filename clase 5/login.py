from  flask import Blueprint, Flask, jsonify, request


login= Blueprint('login', __name__)

@login.route('/login', methods=['POST'])

def llamarServicioSet():
    user= request.json.get('user')
    password= request.json.get('password')
    print ("User enviado: ", user, "Password enviado:", password)   

    codRes, msgRes, accion, rol = iniciarvariables(user, password)


    salida = {
        'codRes': codRes,
        'menRes': msgRes,
        'usuario': user,
        'accion': accion,
        'rol': rol
    }

    return  jsonify(salida), 200

def iniciarvariables(user, password):
    codRes = 'SIN ERROR'
    menRes = 'OK'
    accion = 'login exitoso'
    rol = 'admin'  
    userlocal = 'magabeni'
    passwordlocal = 'unida123'

    try:
        if user == userlocal and password == passwordlocal:
            print("Login exitoso")
            accion = 'login exitoso'
        else:
            codRes = 'ERROR'
            menRes = 'Usuario o contraseña incorrectos' 
            accion = 'login fallido'
            rol = 'ninguno'
            user = 'ninguno'
    
    except Exception as e:
        print("Error en el login:", e)
        codRes = 'ERROR'
        menRes = 'Error en el login'
        accion = 'error en el login'
        rol = 'ninguno'
        user = 'ninguno'
        return codRes, menRes, accion, rol, user
    


    return codRes, menRes, accion, rol