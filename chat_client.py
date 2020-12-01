#By SxNade
#https://github.com/SxNade
#CONTRIBUTE

from termcolor import colored
import socket
import os

#Receiving The Value Of IP and PORT From the User

SERVER_IP = input(colored("What Is Ip of the server running: ", "green"))
SERVER_PORT = int(input(colored("Enter Port No on which the server is running: ", "green")))

USER_NAME = input(colored("Please Choose a Username for Chat: "))

os.system('clear')

print(colored("<1>ONLINE..", "green", attrs=['bold']))

name = USER_NAME + ">> "
encoded_name = name.encode()

# chat Fucntion Initiates the Connection to the Server

def chat():
    s = socket.socket()
    #connecting to the chat server
    s.connect((str(SERVER_IP), SERVER_PORT))

    #infinite loop to recieve messages from the user till the server runs
    
    while True:
        In_msg = s.recv(8192)
        print(In_msg.decode())
        Out_msg = input(colored("MSG> ", "red", attrs=['bold']))
        s.send(encoded_name + Out_msg.encode())

        #condition statement to close the chat incase server_user enters 'bye'

        if In_msg.decode() == 'bye':
            os.system('clear')
            print(colored("<0>OFFLINE", "red", attrs=['bold']))
            s.close()
            break

#Final Main function to run the Chat Program! 

def main():
    chat()
main()
