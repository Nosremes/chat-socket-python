import socket,threading,time

def recv_msg(sock) -> None: 
    """
        Recebe as mensagens dos outros clientes através do servidor 

        Args:
            sock : socket do cliente
    """
    connection = sock
    try:
        while True:
            data = connection.recv(2000)
            if data:
                print(data.decode())
    except Exception as e:
        raise e 

def client(host = "localhost", port=6969) -> None:
    """
        Processo principal, são definidas as características do socket,
        ele é iniciado, fica recebendo as mensagens do servidor e enviando
        mensagens para o servidor

        Args:
            host (srt): ip do servidor
            port (int): porta que deve ser usada
    """

    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_address = (host, port)

    try: 
        sock.connect(server_address)
        print("CONENCTED!")
        recive_msg = threading.Thread(target=recv_msg,args=[sock])
        recive_msg.start()
        
        while True:
            t = time.strftime("%H:%M:%S",time.localtime())
            msg = f"<{t}> {input()}"
            sock.send(msg.encode())

        sock.close()

    except Exception as e:
        print("Houve um problema: ",e)

            
client()

