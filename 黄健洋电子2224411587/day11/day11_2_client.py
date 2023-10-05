import socket
sk = socket.socket()
sk.connect( ("127.0.0.1",8999) )
while 1:
	send_data = input("客户端，发送的内容是:")
	sk.sendall(bytes(send_data, encoding="utf8"))
	accept_data = sk.recv(1024)
	print(f"客户端接收的内容是: {accept_data.decode('utf8')}")
sk.close()
