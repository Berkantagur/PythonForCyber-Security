import socket

portList = []
bannerList = []

file = open("ip.txt", "r")
ips = file.read()
file.close()

for ip in ips.splitlines():

    print(ip)

    for port in range(1, 25):

        try:

            socket1 = socket.socket()
            socket1.connect((str(ip), int(port)))
            banner = socket.recv(1024)
            bannerList.append(str(banner))
            portList.append(str(port))
            socket1.close()
            print(port)
            print(banner)

        except:
            pass

print(portList)
print(bannerList)