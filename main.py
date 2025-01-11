import http.client
from flask import Flask, jsonify, request

app = Flask(__name__)

@app.route('/')
def home():
    return 'API ATIVA!'


@app.route('/imovel/<codeImovel>')
def requestImovel(codeImovel):
    conn = http.client.HTTPSConnection("api.imoview.com.br")
    payload = ""
    headers = {
        'accept': "application/json",
        'chave': "b5cd4a280cce768cee6027ec5c82c8be"
    }

    urlSite = f"/Imovel/RetornarDetalhesImovelDisponivel?codigoImovel={codeImovel}"
    method = "GET"

    try:
        conn.request(method, urlSite, payload, headers)
        res = conn.getresponse()
        data = res.read()
        conn.close()

        # Converte a resposta para JSON, se possível
        response_json = data.decode("utf-8")
        return jsonify(response_json)
    except Exception as e:
        conn.close()
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)