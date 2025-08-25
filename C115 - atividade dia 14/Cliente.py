# Alunas: Clara de Lima Azevedo e Maria Eduarda de Oliveira

import socket
import pickle

cliente = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
cliente.connect(('localhost', 5000))

perguntas = pickle.loads(cliente.recv(1024))
respostas = []

for p in perguntas:
    print(p["pergunta"])
    for idx, opcao in enumerate(p["opcoes"]):
        print(f"{idx}. {opcao}")
    resp = int(input("Digite a opção correta: "))
    respostas.append(resp)

cliente.send(pickle.dumps(respostas))
resultado = pickle.loads(cliente.recv(1024))
print(f"Você acertou {resultado['acertos']} questões.")
for d in resultado['detalhes']:
    print(f"{d['pergunta']} - {'Acertou' if d['correto'] else 'Errou'}")
cliente.close()
