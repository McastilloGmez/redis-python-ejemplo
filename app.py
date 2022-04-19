import requests, redis, json
from flask import Flask, jsonify

redis_cli = redis.Redis(host="192.168.1.234", port=6379, decode_responses=True, encoding="utf-8")

app = Flask(__name__)

api = "https://jsonplaceholder.typicode.com/users"

@app.route("/")
def home():
    return jsonify("Ejemplo Redis Cachin-Python")

@app.route("/users")
def getUsers():
    responseApi = requests.get(api)
    print('Usuarios recolectados desde la API')
    return jsonify(responseApi.json())

@app.route("/cached-users")
def cachedUsers():
    data = redis_cli.get("users")

    if (data):
        print('Usuarios recolectados desde Redis')
        return jsonify(json.loads(data))
    else:
        apiResponse = requests.get(api)
        print('Usuarios recolectados desde la API')
        redis_cli.set("users", json.dumps(apiResponse.json()))
        return jsonify(apiResponse.json())

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5000)