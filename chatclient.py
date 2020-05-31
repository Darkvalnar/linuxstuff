#!/usr/bin/python3

__author__ = 'Rawlings'
__contact__ = 'sh0t@hashbang.sh'


import socket
import threading
import sys
import time
import os

# declaring ip and port by checking for commandline args, if none are specified we will default to localhost:55555
IP = str(sys.argv[1])
port = int(sys.argv[2])

if len(sys.argv) != 3: 
    print ("using 127.0.0.1 and port 55555 as default values")
    host = "127.0.0.1"
    port = 55555

userinput = []

# Setup tasks, picking nick and connecting to the server
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((IP, port))
nickname = input("Choose your nickname >")

print ("connecting to", str(IP) + ":" + str(port))
time.sleep(2)

# Function to listen to the server and sending your nick 
def receive():
    print("connected!")
    while True:
        try:
            # This is where you receive the message, if it is NICK, then we send the nickname
            message = client.recv(1024).decode("utf8")
            if message == "NICK":
                client.send(nickname.encode("utf8"))
            else:
                userinput.append(message)
                os.system("cls" if os.name == "nt" else "clear")
                for messages in userinput:
                    print(messages)
        except:
            # We have to close the connection to handle errors
            print("Exception occured, closing connection")
            client.close()
            break

# Function to send messages to the server
def write():
    print("ready to send messages!")
    while True:
        message = "{}: {}".format(nickname, input("")) # this will store the message you want to send 
        #userinput.append(message)
        client.send(message.encode("utf8")) # we encode the message to utf8 and then send it to the server
        #os.system('cls' if os.name == 'nt' else 'clear')
    
# Threads setup for listening and for writing
receive_thread = threading.Thread(target=receive)
receive_thread.start()
write_thread = threading.Thread(target=write)
write_thread.start()
