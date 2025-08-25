# Alunas: Clara de Lima Azevedo e Maria Eduarda de Oliveira

# Crie um programa cliente servidor que envia duas questões em sequência de múltipla escolha para um cliente
# após este se conectar, o cliente deve responder às questões e o servidor retornar com quantas questões acertou,
# mostrando em uma lista o acerto/erro de cada.

import socket
import pickle

perguntas = [
    {"pergunta": "Qual o maior planeta do sistema solar?", "opcoes": [
        "Júpiter", "Saturno", "Terra", "Marte"], "resposta": 0},
    {"pergunta": "Qual planeta é conhecido como o planeta vermelho?", "opcoes": [
        "Mercúrio", "Vênus", "Terra", "Marte"], "resposta": 3}
]

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(('localhost', 5000))
server.listen(1)
print("Servidor aguardando conexão...")
conn, addr = server.accept()
print(f"Conectado a {addr}")

conn.send(pickle.dumps(perguntas))
respostas_cliente = pickle.loads(conn.recv(1024))

resultados = []
acertos = 0
for i, resp in enumerate(respostas_cliente):
    correto = resp == perguntas[i]["resposta"]
    resultados.append(
        {"pergunta": perguntas[i]["pergunta"], "correto": correto})
    if correto:
        acertos += 1

conn.send(pickle.dumps({"acertos": acertos, "detalhes": resultados}))
conn.close()
