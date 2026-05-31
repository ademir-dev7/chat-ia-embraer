# Chat com IA simulado — Python puro (sem bibliotecas externas)
import json
from http.server import HTTPServer, BaseHTTPRequestHandler

# Lista para guardar o histórico da conversa
historico = []

# Função que simula uma IA respondendo
def ia_responder(mensagem):
    mensagem = mensagem.lower()

    if "oi" in mensagem or "olá" in mensagem:
        return "Olá! Sou o assistente da Embraer. Como posso ajudar?"
    elif "avião" in mensagem or "aeronave" in mensagem:
        return "Posso ajudar com informações técnicas sobre aeronaves."
    elif "erro" in mensagem or "problema" in mensagem:
        return "Entendido. Me descreva o erro com mais detalhes."
    else:
        return f"Recebi sua mensagem: '{mensagem}'. Como posso ajudar?"

# Classe que controla o servidor HTTP
class ChatHandler(BaseHTTPRequestHandler):

    # 👉 Quando abrir o navegador (GET)
    def do_GET(self):
        self.send_response(200)  # Status OK
        self.send_header('Content-Type', 'text/html')
        self.end_headers()

        # HTML + JavaScript (interface do chat)
        html = """
        <html>
        <head>
            <title>Chat IA</title>
        </head>
        <body>
            <h2>Chat com IA (Simulado)</h2>

            <input id="msg" placeholder="Digite sua mensagem">
            <button onclick="enviar()">Enviar</button>

            <div id="chat" style="margin-top:20px;"></div>

            <script>
                function enviar() {
                    const msg = document.getElementById("msg").value;

                    fetch("/", {
                        method: "POST",
                        headers: {
                            "Content-Type": "application/json"
                        },
                        body: JSON.stringify({ mensagem: msg })
                    })
                    .then(res => res.json())
                    .then(data => {
                        const chat = document.getElementById("chat");

                        chat.innerHTML += "<p><b>Você:</b> " + msg + "</p>";
                        chat.innerHTML += "<p><b>IA:</b> " + data.resposta + "</p>";
                    });
                }
            </script>
        </body>
        </html>
        """

        self.wfile.write(html.encode())

    # 👉 Quando enviar mensagem (POST)
    def do_POST(self):
        # Lê o tamanho do conteúdo enviado
        tamanho = int(self.headers['Content-Length'])

        # Lê os dados enviados
        corpo = self.rfile.read(tamanho)

        # Converte JSON para dicionário Python
        dados = json.loads(corpo)

        mensagem = dados.get("mensagem", "")

        # Chama a "IA"
        resposta = ia_responder(mensagem)

        # Salva no histórico
        historico.append({
            "pergunta": mensagem,
            "resposta": resposta
        })

        # Retorna resposta em JSON
        self.send_response(200)
        self.send_header('Content-Type', 'application/json')
        self.end_headers()

        self.wfile.write(json.dumps({"resposta": resposta}).encode())

    # 👉 Log no terminal
    def log_message(self, format, *args):
        print(f"Requisição recebida: {args[0]}")

# Inicia o servidor
print("Servidor rodando em http://localhost:8000")
print("Aperte Ctrl+C para parar")

HTTPServer(("localhost", 8000), ChatHandler).serve_forever()