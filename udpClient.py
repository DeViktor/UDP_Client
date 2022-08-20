import socket

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
print("sucess")

host='localhost'
port= 5433
msg= 'mensagem pro servidor '

try:
  print("i'm trying send mensage" + msg)
  s.sendto(msg.encode(), (host,5432))
  
  data, serv = s.recvfrom(4096)
  data.decode()
  print(data)
finally:
  print("ended")
  s.close()