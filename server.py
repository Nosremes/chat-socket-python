import socket,threading

def recv_and_broadcast(sock,clients) -> None:
    """
        Recebe a mensagem de um cliente e reflete ela 
        com os demais clientes conectados no servidor

        Args:
            sock = socket object do cliente
    """
    clients = clients
    conection_client = sock
    try:
        while True:
            msg = conection_client.recv(2000)
            if msg:
                print(sock.getsockname(),msg.decode())
                # espelhar as mensagens para os outros clientes
                for client_sock in clients:
                    if client_sock != conection_client:
                        try:
                            client_sock.send(msg)
                        except:
                            CLIENTS.remove(client_sock)

    except Exception as e:
        print("ERRO: ",e)

CLIENTS = []

def server(host="localhost",port=6969) -> None:
    """
        Processo principal, são definidas as características do socket,
        ele é iniciado, e fica recebendo as mensagens dos usuários e as 
        reflete para todos clientes

        Args:
            host (srt): ip do servidor
            port (int): porta que deve ser usada
    """

    server_address = (host,port)
    sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    sock.bind(server_address)
    print("Iniciando servidor!")
    sock.listen(2)
    try:    
        while True:
            client_socket,address = sock.accept()
            CLIENTS.append(client_socket)
            print(f"Connected: {client_socket},{address}")
            threading.Thread(target=recv_and_broadcast,args=[client_socket,CLIENTS]).start()
        
    except Exception as e:
        print("Houve um problema : ",e)
    
    finally:
        # em caso de algum problema
        for client in CLIENTS:
            sock.remove(client)
        sock.close()

            
server()
