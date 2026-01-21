from flask import Flask, request, jsonify
import joblib
import pandas as pd

app = Flask(__name__)

# Carregar modelo treinado
modelo = joblib.load("modelos/modelo_pms.pkl")

@app.route("/")
def home():
    return "API de Predição de Mudança de Software está rodando!"

@app.route("/predicao", methods=["POST"])
def predicao():
    dados = request.json
    df = pd.DataFrame([dados])
    pred = modelo.predict(df)
    return jsonify({"mudanca_prevista": int(pred[0])})

if __name__ == "__main__":
    app.run(debug=True)
