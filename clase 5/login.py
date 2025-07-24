from  flask import Blueprint, Flask, jsonify, request


login= Blueprint('login', __name__)

@login.route('/login', methods=['POST'])

def llamarServicioSet():
    user= request.json.get('user')
    password= request.json.get('password')
    print ("User enviado: ", user, "Password enviado:", password)
