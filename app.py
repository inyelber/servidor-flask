from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/', methods=['GET'])
def home():
    return "🚀 API activa y lista para recibir datos del ESP"

@app.route('/datos', methods=['POST'])
def recibir_datos():
    data = request.get_json()
    print("📥 Datos recibidos:", data)
    return jsonify({"status": "ok", "mensaje": "Datos recibidos correctamente"}), 200

if __name__ == '__main__':
    app.run()
