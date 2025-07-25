
from flask import Flask, jsonify, request
from cliente import cliente

app = Flask(__name__)

#Se expone cliente
app.register_blueprint(cliente)

@app.route('/', methods=['GET'])
def iniciar():
    return 'Server flask is running on port 500'

if __name__ == '__main__':
    app.run(debug=True,port=5000, host='0.0.0.0')