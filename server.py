#!/usr/bin/env python
from socket import *  # Import socket module
from os import system,popen
from funcs import *


HOST = gethostname()  # Get local machine name
PORT = 23456  # Reserve a port for your service.

# Opening a firewall port
system(
    'netsh advfirewall firewall add rule name="Open Port {0}" dir=in action=allow protocol=TCP localport={1} remoteip={2}'.format(
        PORT, PORT, HOST))

with socket() as s:  # Create a socket object
    print('Server started!')
    print('Waiting for clients...')

    s.bind((HOST, PORT))  # Bind to the port
    s.listen(5)  # Now wait for client connection.
    c, addr = s.accept()  # Establish connection with client.

    # Remote client machine connection
    print('Got connection from', addr)
    while True:  # Running the program in a loop to receive and send many messages
        remote_input = c.recv(1024).decode('UTF-8')# Getting a message from the remote client machine
        if url_check(remote_input):#Calling url_check function
            split_url=remote_input.split("://")#Split the url because "HTTPS://" cant be pinged
            ping_output=popen("ping -c5 "+split_url[1]).read() #Storing the ping output in a variable
            write_to_file("trace.log",ping_output) #Calling a function that write the ping output in a log file
            c.send(ping_output.encode()) #Sending the ping output to the client
           

        else:
            c.send("Error: the request status is not 200".encode())

        if remote_input == "exit":
            break
