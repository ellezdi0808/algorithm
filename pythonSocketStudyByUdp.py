#基于UDP

#客户端
# 导入socket库:
import socket

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
for data in [b'Michael', b'Tracy', b'Sarah']:
    # 发送数据:
    s.sendto(data, ('127.0.0.1', 9999))
    # 接收数据:
    print(s.recv(1024).decode('utf-8'))
    #recv接受TCP套接字的数据，数据以字符串形式返回
    #接收数据时，调用recv(max)方法，一次最多接收指定的字节数，因此，在一个while循环中反复接收，直到recv()返回空数据，表示接收完毕，退出循环。

s.close()



#服务端
import socket

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
# 绑定端口:
s.bind(('127.0.0.1', 9999))
print('Bind UDP on 9999...')
while True:
    # 接收数据:
    data, addr = s.recvfrom(1024)
    # recvfrom()方法返回数据和客户端的地址与端口，这样，服务器收到数据后，直接调用sendto()就可以把数据用UDP发给客户端。
    #recv接受TCP套接字的数据，数据以字符串形式返回

    #recvfrom接受UDP套接字的数据u，与recv()类似，但返回值是tuple(data, address)。其中data是包含接受数据的字符串，address是发送数据的套接字地址

    print('Received from %s:%s.' % addr)
    s.sendto(b'Hello, %s!' % data, addr)
