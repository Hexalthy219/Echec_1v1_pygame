import socket
import pickle

host = socket.gethostname()  # as both code is running on same pc
port = 1300  # socket server port number

client_socket = socket.socket()  # instantiate
client_socket.connect((host, port))  # connect to the server

message = input(" -> ")  # take input

while message.lower().strip() != 'bye':
   client_socket.send(message.encode())  # send message
   data = client_socket.recv(1024)  # receive response

   print('Received from server: ')  # show in terminal
   print(pickle.loads(data))
   message = input(" -> ")  # again take input

client_socket.close()  # close the connection