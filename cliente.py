from socket import *
import subprocess

try:
    with socket(AF_INET, SOCK_STREAM) as client:  # Protocolos: IPV4 E TCP
        ipAndress = "127.0.0.1"  # IP que será conectado
        portAndress = 5000  # porta sera conectada

        # Abrindo a porta referente ao IP
        client.bind((ipAndress, portAndress))

        # quantidade de pessoas que podem ouvir e se conectar a essa maquina
        client.listen(1)

        # variavel que vai receber a conexao e aceita-la
        conection, address = client.accept()
        print("Conexão Efetuada com sucesso!")

        while True:
            cmdSnd = input("Digite o comando que será enviado: ").encode()
            conection.sendall(cmdSnd)
            responseCmd = conection.recv(5120).decode()
            print(responseCmd)


except TimeoutError as err:
    print("Não foi possível conectar ao servidor:", err)
except ConnectionResetError as err:
    print("A conexão foi fechada inesperadamente:", err)
except Exception as err:
    print("Ocorreu um erro:", err)
