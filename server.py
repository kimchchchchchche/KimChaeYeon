import socket

server = socket.socket()
server.bind(("192.168.56.1" , 9999)) # 9999번 포트에서 모든 인터페이스에 연결한다.
server.listen(1) #입력하지 않으면 파이썬이 자의적으로 판단해서 임의의 숫자로 진
print("============the server is ready==============")

client , addr = server.accept() #누군가 소켓에 접속하여 연결됐을때 결과값을 return
print("=========client is connected===========")

msg = client.recv(1024) #소켓에서 1024 바이트만큼 가져온다. (가져올 바이트 크기 지정)
print("============messege received========")
print(msg)

client.sendall(b'hi hi i\'m server. your messege is \' ' + msg + b'\'')
print("=======messege send==============")

client.close()
server.close()
