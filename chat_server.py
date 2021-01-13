#By SxNade
#https://github.com/SxNade/Terminal_chat
#CONTRIBUTE
#server script


from termcolor import colored
from Crypto.Cipher import AES
import socket
import sys
import os

banner = '''
 _____ _____ ____  __  __ ___ _   _    _    _           ____ _   _    _  _____ 
|_   _| ____|  _ \|  \/  |_ _| \ | |  / \  | |         / ___| | | |  / \|_   _|
  | | |  _| | |_) | |\/| || ||  \| | / _ \ | |   _____| |   | |_| | / _ \ | |  
  | | | |___|  _ <| |  | || || |\  |/ ___ \| |__|_____| |___|  _  |/ ___ \| |  
  |_| |_____|_| \_\_|  |_|___|_| \_/_/   \_\_____|     \____|_| |_/_/   \_\_|  
                                                                               
                                                    *By SxNade https://github.com/SxNade 
'''
print(banner)

#Receiving The Value Of IP and PORT From the User

LISN_IP = input(colored("Enter The Local IP of your Machine: ", "green"))
LISN_PORT = int(input(colored("Enter The port no. to bind: ", "green")))

USER_NAME = input(colored("Please Choose a Username for Chat: "))

os.system('clear')

print(colored("<1>ONLINE...", "green", attrs=['reverse', 'blink']))

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
        msg = input(colored("\nSEND-> ", "red", attrs=['bold']))
        #condition statement to close the chat incase server_user enters 'bye'
        if msg == 'bye':
            conn.send('bye'.encode())
            os.system('clear')
            print(colored("<0>OFFLINE", "red", attrs=['bold']))
            conn.close()
            sys.exit()
            break

        else:
         #adding AES encryption
            magic = AES.new('EBC3D4C51C46801A7267AAB59A63551B', AES.MODE_CFB, 'This is an IV456')
            #YOU MUST REPLACE THIS AES KEY.....>!!!FIND ONE FOR YOURSELF ON GOOGLE>>>>>!
            data = encoded_name + msg.encode()
            data_send = magic.encrypt(data)
            conn.send(data_send)
            In_messg = conn.recv(8192)
            #decrypting the incoming AES encrypted data
            recv_data_enc = magic.decrypt(In_messg)
            recv_data_unenc = recv_data_enc.decode()
            print("\n" + recv_data_unenc)

#Final Main function to run the Chat Program! 

def main():
    chat()
main()

