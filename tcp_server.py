import SocketServer

HOST, PORT = "", 60000

class MyTCPHandler(SocketServer.BaseRequestHandler):
    """
    This program is modified from an example (c)Python Software Foundation
    that was posted at https://docs.python.org/2/library/socketserver.html

    The request handler class for our server.
    It is instantiated once per connection to the server, and must
    override the handle() method to implement communication to the
    client.
    """

    def handle(self):
        # global variables that are modified inside a function must be declared first as global
        global count

        # self.request is the TCP socket connected to the client
        self.request.sendall("Welcome to the server.\r\nWhat is your name please?\r\n")

        # string.strip removes all leading and trailing white space inclduing \r\n
        # number inside socket.recv(nnn) sets the maximum number of bytes to receive
        name = self.request.recv(1024).strip()
        print name + " has just contacted us from " + format(self.client_address[0])

        count = count + 1;
        
        # observe the conversion from an integer number to string
        data = "Nice to meet you " + name + ".\r\nYou are the " + str(count) + "th  person who stopped by today\r\n"
        self.request.sendall(data)

# Global counter variable
count = 0
        
# Create the server, binding to HOST network interface ("" for all) on port PORT
server = SocketServer.TCPServer((HOST, PORT), MyTCPHandler)

# Activate the server; this will keep running until you
# interrupt the program with Ctrl-C or Ctrl-Break
server.serve_forever()