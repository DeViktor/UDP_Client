import socket

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
print("sucess")

host="localhost"
port= 5432

s.bind((host,port))
mssg = "test"

while 1:
  data, address = s.recvfrom(4096)
  if data:
    print('server sending message ')
    s.sendto(data + mssg.encode(), address)