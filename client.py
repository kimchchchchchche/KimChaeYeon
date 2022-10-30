import socket

ip = "192.168.56.1"
port = 9999

client = socket.socket()

client.connect((ip, port)) #클라이언트에서 서버로 접속
print("============server is connected==============")

client.send(b"hello ~ i'm client")
print('=============messege send==============')

msg = client.recv(1024)
print('=============messege erceived==============')
print(msg)

client.close()
