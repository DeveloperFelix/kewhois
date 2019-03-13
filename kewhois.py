import socket
import sys

# .Ke whois lookup domain

class whoIsKE:

    server = 'whois.kenic.or.ke'
    port = 43

    s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    

    def conSocket(self):
        try:
            self.s.connect((self.server,self.port))
        except:
            print('connection error...')
            self.s.close()
            sys.exit()
            
    def whois(self,domain):
        
        self.conSocket()
        self.sendReq(domain)
        self.recvMSG()
        
    def sendReq(self,domain):
         try:

             self.s.sendall(domain.encode('utf-8'))
         except:
              print('sending error...')
              self.s.close()
              sys.exit()
                  
    def recvMSG(self):
        try:
            
            txt = self.s.recv(1024).decode('utf-8')
            
            if len(txt) > 0:
                
                rry = txt.split('\n')
                
                for i in rry:
                    print(i)
            else:
                 print('No data')
                 
        except:
             print('receiving error...')
             self.s.close()
             sys.exit()

               
