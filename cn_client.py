import socket
print("""\
 _       __     __                             
| |     / /__  / /________  ____ ___  ___      
| | /| / / _ \/ / ___/ __ \/ __ `__ \/ _ \     
| |/ |/ /  __/ / /__/ /_/ / / / / / /  __/     
|__/|__/\___/_/\___/\____/_/ /_/ /_/\___/      
          / /_____                             
         / __/ __ \                            
        / /_/ /_/ /                            
       _\__/\____/          __                 
      / ____/ (_)__  ____  / /_                
     / /   / / / _ \/ __ \/ __/                
    / /___/ / /  __/ / / / /_                  
    \____/_/_/\___/_/ /_/\__/                  
                                                                                                                           

""")
#local host
host = "127.0.0.1" 
#get the port you want to connect to
port = int(input("ENTER THE PORT YOU WANT TO CONNECT TO:  "))

# We create a socket for the clitent
# AF_INET is an address family that is used to designate the type 
# of addresses that your socket can communicate with (in this case, Internet Protocol v4 addresses).
# TCP (SOCK_STREAM) is a connection-based protocol. 
#The connection is established and the two parties have a conversation until the connection is terminated by one of the parties or by a network error.
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)


try:
    # connect() is used to connect to a remote [server] address
    client.connect((host, port))
    print("Connected to the SERVER!")
except socket.error as e:
    print(str(e))


while True:
    command = input("CLIENT >>> ")
    if command == "STOP CLIENT":
        client.close()
    client.send(command.encode())
    response = client.recv(1024)
    print(response.decode())

