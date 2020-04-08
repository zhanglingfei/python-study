import getpass
import socket

user_name = getpass.getuser() # 获取当前用户名
hostname = socket.gethostname() # 获取当前主机名
#ip = socket.gethostbyname_ex(hostname)

host_ip = socket.gethostbyname("localhost")

#print('C:\\Users\\' + user_name + '\\AppData\Local\Temp\\')

print(user_name)
print(host_ip)