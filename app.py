from flask import Flask, request, jsonify

app = Flask(__name__)

# Variable para almacenar el último dato recibido
ultimo_dato = {}

@app.route('/')
def index():
    return "Servidor Flask activo 🚀"

# Ruta para recibir datos POST JSON desde ESP32
@app.route('/datos', methods=['POST'])
def recibir_datos():
    global ultimo_dato

    if not request.is_json:
        return jsonify({"error": "Se esperaba JSON"}), 400

    data = request.get_json()
    ultimo_dato = data  # Guardamos el dato recibido

    print(f"Datos recibidos: {data}")  # Mostrar en consola

    return jsonify({"mensaje": "Datos recibidos correctamente", "datos": data}), 200

# Ruta para ver el último dato recibido (GET)
@app.route('/ultimo', methods=['GET'])
def ver_ultimo():
    if ultimo_dato:
        return jsonify({"ultimo_dato": ultimo_dato})
    else:
        return jsonify({"mensaje": "No se han recibido datos aún"}), 404

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

