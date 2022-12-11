import socket
HOST="127.0.0.1"
PORT=65432
msg=("bonjour chaimaa")
alphabet = "abcdefghijklmnopqrstuvwxyz"



def encryption(message,decalage):
     txtChiffre=""
     for i in range(0, len(message)):
                for j in range(0, len(alphabet)):
                     if message[i] == alphabet[j]:
                       txtChiffre+=alphabet[(j+decalage) % 26]
     return "le message"+txtChiffre

          
msg=encryption("bonjour chaimaa",2)

    
with socket.socket(socket.AF_INET , socket.SOCK_STREAM) as s:
    s.connect((HOST,PORT))
    s.sendall(msg.encode('utf-8'))
    data=s.recv(1024)
    s_data=data.decode('utf-8')
    print(s_data)
    print("received from server :"+s_data)