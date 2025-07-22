#-*- coding :utf-8 -*-
#caracteres especiales

from flask import Flask, jsonify, request

app = Flask(__name__)

@app.route ('/',methods=['GET'])
def unida():
    return 'Hola desde la Unida'

if __name__ == '__main__':
    app.run(debug=True,port=5000, host='0.0.0.0')
    '''
    El 0.0.0.0  es una dirección IP especial que permite que la aplicación 
    Flask sea accesible desde cualquier dirección IP en la red local. 
    Esto es útil para pruebas y desarrollo, ya que permite que otros 
    dispositivos en la misma red accedan a la aplicación.
    '''