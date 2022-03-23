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

host = "127.0.0.1"
port = int(input("ENTER THE PORT YOU WANT TO CONNECT TO:  "))
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# connect() is used to connect to a remote [server] address
try:
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

