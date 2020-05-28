import socket
import threading
import argparse


# setup tasks for cli args

text = "Run without args to run server on 127.0.0.1 and port 55555"
parser = argparse.ArgumentParser(description=text)

# setting up cli args here:
parser.add_argument("-ip", "--host", help="specify host IP", type=str )
parser.add_argument("-p", "--port", help="specify host port", type=int )

args = parser.parse_args()


#Server setup task
def setup():
    print ("setting server in listen mode...")
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM) # this is where the magic happens, we define the socket and protocol for our server
    server.bind((host, port))
    server.listen()
    print ("server listening on IP: " + host + " and port " + str(port))

    # setting up lists to store clients and nicknames in, this is important because we will be appending this constantly

    clients= []
    nicknames = []
    
    return clients, nicknames, server

# setting up a broadcast system to send messages to all clients
def broadcast(message):
    clients = setup()
    print("setting up broadcasting...")
    for client in clients:
        client.send(message)


# Function to handle incoming client messages
def handle(client):
    clients, nicknames, server = setup()
    print ("setting up message handling...")
    while True:
        try:
            # Getting incoming message and sending it to everyone else
            message = client.recv(1024)
            broadcast(message)
        except:
            #Removing clients and closing them when we encounter an exception within our while loop
            index = clients.index(client)
            clients.remove(client)
            client.close()
            nickname = nicknames[index]
            broadcast("{} has left the server!".format(nickname).encode("ascii"))


# Function to receive and listen
def receive():
    clients, nicknames, server = setup()
    print("setting up service to receive and listen...")
    while True: 
        # we are running this in an endless while loop to constantly accept connections
        client, address = server.accept()
        print("Connected with {}".format(str(address)))
        
        #Requesting nickname from client, if we get one, we store it for further usage
        client.send("NICK".encode("ascii"))
        nickname = client.recv(1024).decode("ascii")
        nicknames.append(nickname)
        clients.append(client)
        
        # Printing and broadcasting the nicks
        
        print("Nickname is {}".format(nickname))
        broadcast("{} has joined..".format(nickname).encode("ascii"))
        client.send("Connected to the server".encode("ascii"))
        
        # starting thread for client message handling
        thread = threading.Thread(target=handle, args=(client,))
        thread.start()


if args.host:
    if args.port:
        host = args.host
        port = int(args.port)
        print("Setting server in listen mode on: " + host + " with port " + str(port))
        receive()
    else:
        host = args.host
        print("Setting server in listen mode on IP:" + host + " and port 55555")
        port = 55555
        receive()
else:
    print("DECUCK")
    host = "127.0.0.1"
    port = 55555
    receive()