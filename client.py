#!/usr/bin/env python
from socket import *
from os import popen
# from input_handler import *


HOST = gethostname()  # Get local machine name
PORT = 23456  # Reserve a port for your service.

try:
    with socket() as s:  # Creating a socket object
        s.connect((HOST, PORT))  # Establishing a new connection to a remote machine
        print("Please enter a valid url:")

        while True:  # Running the program in a loop to receive and send many messages
            client_input = input('CLIENT >> ')
            s.sendall(client_input.encode())# Sending the message as a Byte stream 
            print(s.recv(1024).decode('UTF-8'))
            if client_input == "exit":  # If the client is interested to exit
                print("CLIENT>> Exiting the program!")
                break			
            
        
except ConnectionRefusedError:  # Couldn't establish a connection to the remote host
    print("No connection could be made because the target machine refused it")
except ConnectionResetError:  # The established connection was reset by the remote host
    print("An existing connection was forcibly closed by the remote host")
except ValueError:
    print("Error: not a valid URL")
