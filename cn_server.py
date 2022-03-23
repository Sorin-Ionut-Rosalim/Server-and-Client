import socket
from _thread import *
print("""\
 _       __     __                             
| |     / /__  / /________  ____ ___  ___      
| | /| / / _ \/ / ___/ __ \/ __ `__ \/ _ \     
| |/ |/ /  __/ / /__/ /_/ / / / / / /  __/     
|__/|__/\___/_/\___/\____/_/ /_/ /_/\___/      
          / /_____                             
         / __/ __ \                            
        / /_/ /_/ /                            
       _\__/\____/                             
      / ___/___  ______   _____  _____         
      \__ \/ _ \/ ___/ | / / _ \/ ___/         
     ___/ /  __/ /   | |/ /  __/ /             
    /____/\___/_/    |___/\___/_/              
                                                                                                                       
                    """)




host = "127.0.0.1"
port = int(input("ENTER THE PORT YOU WANT TO OPEN:  "))
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server:
    # Here I am creating the socket,
    #socket describes the comunication between two IP entities (end poitns)
    #        IPV4 - AF_INET (host, port)
    #        TCP - SOCK_STREAM

    def threaded_client(connection):
        """
            * Function that handles multiple clients
            * The function connects to each client on the different address given by the server
        """

        while True:
            data = connection.recv(1024)
            raw_data = data.decode()
            if raw_data == "STOP SERVER":
                server.close()
            if raw_data == "STOP":
                break
            else:
                reply = "SERVER >>> " + raw_data
            if not data:
                break
            print(f"CLIENT >>> {raw_data}")
            connection.sendall((reply).encode())
        connection.close()

    # bind() = associates the socket with its local address
    try:
        server.bind((host, port))
    except socket.error as e:
        print(str(e))

    #listen() = listen for socket connections and limit the queue of incoming connections
    #also set server in listen mode
    print('Waiting for a Client..')
    server.listen()

    while True:
        # Establish connection with client.
        #wakes up when a connection from a client is establish
        connection, addr = server.accept()
        print("Connected to {}".format(addr))
        #start a new thread for each client
        start_new_thread(threaded_client, (connection, ))


