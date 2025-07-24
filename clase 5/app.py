#-*- coding :utf-8 -*-
#caracteres especiales

from flask import Flask, jsonify, request
from login import login

app = Flask(__name__)

#Se expone login
app.register_blueprint(login)

@app.route('/', methods=['GET'])
def unida():
    return 'Server flask is running on port 500'

if __name__ == '__main__':
    app.run(debug=True,port=5000, host='0.0.0.0')
    '''
    El 0.0.0.0  es una dirección IP especial que permite que la aplicación 
    Flask sea accesible desde cualquier dirección IP en la red local. 
    Esto es útil para pruebas y desarrollo, ya que permite que otros 
    dispositivos en la misma red accedan a la aplicación.
    '''