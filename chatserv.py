#!/usr/bin/python3

__author__ = 'Rawlings'
__contact__ = 'sh0t@hashbang.sh'

import socket
import threading
import sys
import time


# declaring host and port by checking for commandline args, if none are specified we will default to localhost:55555
host = str(sys.argv[1])
port = int(sys.argv[2])

if len(sys.argv) != 3: 
    print ("using 127.0.0.1 and port 55555 as default values")
    host = "127.0.0.1"
    port = 55555

# server start up
print ("setting server in listen mode...")
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM) # this is where the magic happens, we define the socket and protocol for our server
server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1) 
    
server.bind((host, port))
server.listen()
    
print ("server listening on: " + host + ":" + str(port))
time.sleep(1)

# setting up lists to store clients and nicknames in, this is important because we will be appending this constantly
clients= []
nicknames = []
messagelist = []

# this is where we set the actual messaging system up, this function allows us to broadcast to all clients connected
print("setting up messaging...")
def broadcast(message):
    for client in clients:
        client.send(message)



print ("setting up message handling...")
time.sleep(1)

# Function to handle incoming client messages
def handle(client):
    while True:
        try:
            # Getting incoming message and sending it to everyone else
            message = client.recv(1024)
            #testmes = client.recv(1024)
            #name = nicknames[index]
            print (message) # shows messages in server log
            broadcast(message)
            #extra(testmes)
        except:
            #Removing clients and closing them when we encounter an exception within our while loop
            index = clients.index(client)
            clients.remove(client)
            client.close()
            nickname = nicknames[index]
            broadcast("{} has left the server! \n".format(nickname).encode("utf8"))

# Function to receive and listen
print("setting up service to receive and listen...")
time.sleep(1)
def receive():
    while True: 
        # we are running this in an endless while loop to constantly accept connections
        client, address = server.accept()
        print("Connected with {}".format(str(address)))
        
        #Requesting nickname from client, if we get one, we store it for further usage
        client.send("NICK".encode("utf8"))
        nickname = client.recv(1024).decode("utf8")
        # adding nicknames and clients to the list
        nicknames.append(nickname)
        clients.append(client)
        
        # Printing nicks to server log and to client side
        
        print("Nickname is {}".format(nickname))
        broadcast("{} has joined..".format(nickname).encode("utf8"))
        client.send("Connected to the server".encode("utf8"))
        
        # starting thread for client message handling
        thread = threading.Thread(target=handle, args=(client,))
        thread.start()
        #extra_thread = threading.Thread(target=extra)
        #extra_thread.start()

receive()
