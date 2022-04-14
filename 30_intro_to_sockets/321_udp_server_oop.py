# UDP server using OOP approach example for IPv4
import socketserver

class MyUDPHandler(socketserver.BaseRequestHandler):
    """
    This program is modified from an example (c)Python Software Foundation
    that was posted at https://docs.python.org/3.4/library/socketserver.html

    This class works similar to the TCP handler class, except that
    self.request consists of a pair of data and client socket, and since
    there is no connection the client address must be given explicitly
    when sending data back via sendto().
    """

    def handle(self):
        data = self.request[0]
        socket = self.request[1]
        text = str( data, 'UTF-8').strip()
        print( self.client_address , " has just contacted us with the following message: " + text )
        text = text.upper()
        socket.sendto( bytes( text, 'UTF-8') , self.client_address)

if __name__ == "__main__":
    HOST, PORT = "", 1200
    server = socketserver.UDPServer((HOST, PORT), MyUDPHandler)
    server.serve_forever()
