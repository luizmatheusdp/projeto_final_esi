import requests

# URL da API Flask rodando localmente
url = "http://127.0.0.1:5000/predicao"

# Exemplo de dados para teste (substitua pelos nomes das colunas do seu modelo)
dados_teste = {
    "adicoes": 10,
    "remocoes": 2,
    "num_commits": 5
}


try:
    resposta = requests.post(url, json=dados_teste)
    print("Status code:", resposta.status_code)
    if resposta.status_code == 200:
        print("Resultado:", resposta.json())
    else:
        print("Erro:", resposta.text)
except Exception as e:
    print("Erro ao chamar a API:", e)
