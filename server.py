import socket
import pickle

auTourDe = 0

def nouvelleSelection():
    return{
        'pieceSelectionne':False,
        'piece':[],
        'enEchec':False,
        'auTourDes':"blanc"
    }

host = socket.gethostname()
port = 1300

server_socket = socket.socket()
server_socket.bind((host, port))
server_socket.listen(2)
test = nouvelleSelection()
conn1, address1 = server_socket.accept()  # accept new connection
print("Connection from: " + str(address1))
conn1.send("1".encode())

conn2, address2 = server_socket.accept()  # accept new connection
print("Connection from: " + str(address2))
conn2.send("2".encode())

while True:
   if(auTourDe == 0):
      # receive data stream. it won't accept data packet greater than 1024 bytes
      for i in range(3):
         data = conn1.recv(256)
         if not data:
            # if data is not received break
            break
         print("from connected user: ")
         conn2.send(data)  # send data to the client
      auTourDe = 1
   else:
      # receive data stream. it won't accept data packet greater than 1024 bytes
      for i in range(3):
         data = conn2.recv(256)
         if not data:
            # if data is not received break
            break
         print("from connected user: ")
         conn1.send(data)  # send data to the client
      auTourDe = 0
   
   

conn1.close()  # close the connection
conn2.close()