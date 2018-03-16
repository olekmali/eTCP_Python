# TCP server using OOP approach example for IPv4
import socketserver

count = 0

class MyTCPHandler(socketserver.BaseRequestHandler):
    """
    This program is modified from an example (c)Python Software Foundation
    that was posted at https://docs.python.org/3.4/library/socketserver.html

    The RequestHandler class for our server.
    It is instantiated once per connection to the server, and must
    override the handle() method to implement communication to the
    client.
    """

    def handle(self):
        global count
        count = count + 1;
        # self.request is the TCP socket self.request connected to the client
        try:
            # Let's connect a file reader that will allow us to read data line by line
            so_file = self.request.makefile('r', encoding='UTF-8')
            self.request.sendall( bytes( "Welcome to the server.\r\nWhat is your name please?\r\n", 'UTF-8' ) )
            # string.strip removes all leading and trailing white space including \r\n
            name = ( so_file.readline() ).strip()
            print( name , " has just contacted us from " , self.client_address )
            # prepare the reply
            data = "Nice to meet you " + name + ".\r\nYou are the " + str(count) + "th person who stopped by today. Bye now!\r\n"
            self.request.sendall( bytes( data, 'UTF-8' ) )
        except self.request.Timeouterror:
            self.request.sendall( bytes( "You are not very talkative today. Bye now!\r\n", 'UTF-8' ) )
        # Note that we only handled the timeout exception. Anything else will be passed to the place this function was called


if __name__ == "__main__":
    HOST, PORT = "", 1200
    # Create the server, binding to the network interface HOST on port PORT
    server = socketserver.TCPServer((HOST, PORT), MyTCPHandler)

    # Activate the server; this will keep running until you
    # interrupt the program with Ctrl-C
    server.serve_forever()
