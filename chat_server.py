#BY SxNade
#https://github.com/SxNade

from termcolor import colored
import socket
import sys
import os


LISN_IP = input(colored("Enter The Local IP of your Machine: ", "green"))
LISN_PORT = int(input(colored("Enter The port no. to bind: ", "green")))

USER_NAME = input(colored("Please Choose a Username for Chat: "))

os.system('clear')

print(colored("<1>ONLINE...", "green", attrs=['bold']))

name = USER_NAME + ">> "
encoded_name = name.encode()

# this chat function starts the server

def chat():
    s = socket.socket()
    #binding the socket address and port
    s.bind((LISN_IP, LISN_PORT))
    s.listen(1)
    conn , addr = s.accept()
    print(colored(f"[+] {addr} Connected", "green"))

#infinite loop to recieve messages from the user till the server runs

    while True:
        msg = input(colored("MSG> ", "red", attrs=['bold']))
        #condition statement to close the chat incase server_user enters 'bye'
        if msg == 'bye':
            conn.send('bye'.encode())
            os.system('clear')
            print(colored("<0>OFFLINE", "red", attrs=['bold']))
            conn.close()
            sys.exit()
            break

        else:
            conn.send(encoded_name + msg.encode())
            print(conn.recv(8192).decode())

#Final Main function to run the Chat Program! 

def main():
    chat()
main()

