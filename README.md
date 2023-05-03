## Backdoor.py

Esse projeto é um exemplo de backdoor simples, que permite a comunicação remota entre duas máquinas, uma como cliente e outra como servidor.

`Por se tratar de uma ferramenta com potencial malicioso, é importante ressaltar que seu uso é estritamente responsabilidade do usuário, e que a utilização deste código para qualquer atividade suspeita ou criminosa é estritamente proibida e pode acarretar em consequências legais.`

Para utilizar esse projeto, é necessário ter conhecimento básico de programação em Python e redes de computadores.

O projeto é composto por dois arquivos: cliente.py e servidor.py. O cliente.py deve ser executado na máquina que deseja enviar os comandos para a máquina do servidor, e o servidor.py deve ser executado na máquina que receberá e executará os comandos enviados pelo cliente.

O primeiro passo é executar o servidor.py na máquina do servidor, que ficará aguardando a conexão do cliente. Para isso, é necessário modificar o IP e a porta na linha 9 do arquivo servidor.py, caso necessário. É importante manter o servidor.py em execução enquanto o cliente.py estiver sendo utilizado.

Em seguida, na máquina do cliente, é necessário executar o arquivo cliente.py, que irá se conectar ao servidor. Para isso, também é necessário modificar o IP e a porta na linha 9 do arquivo cliente.py, caso necessário.

Com a conexão estabelecida, é possível enviar comandos para a máquina do servidor utilizando o prompt do cliente.py. Basta digitar o comando que deseja executar e pressionar Enter.

É importante ressaltar que o projeto é uma ferramenta educativa e não deve ser utilizado para fins maliciosos. Caso tenha dúvidas sobre a legalidade do uso dessa ferramenta, recomenda-se que consulte um advogado antes de utilizá-la.