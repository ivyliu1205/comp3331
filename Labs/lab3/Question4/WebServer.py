# Python 2.7
from socket import *
import sys

# Execute command: 
# $python WebServer.py port (for Python)

# Used to handle requests
def html_server(connectionSocket):
    request = connectionSocket.recv(1024).decode("utf-8")

    # GET /filename HTTP/1.1
    fileName = request.split()[1][1:]
    print 'The request file: ' + fileName

    try:
        file = open(fileName, "rb")
        responseFile = file.read()
        connectionSocket.send('HTTP/1.1 200 OK\n\n')
        connectionSocket.send(responseFile)
        print '200 OK'

    except IOError:
        connectionSocket.send('HTTP/1.1 400 File not found\n\n')
        connectionSocket.send('<h1>404 Error: File not found</h1>')
        print '404 ERROR'

    print '/////////////////////////////////////////////////'
        

if __name__ == "__main__":
    serverPort = int(sys.argv[1])

    # create a connection socket
    serverSocket = socket(AF_INET, SOCK_STREAM)

    serverSocket.bind(('localhost', serverPort))
    serverSocket.listen(1)

    print 'The server is ready to receive'

    while 1:
        connectionSocket, addr = serverSocket.accept()

        html_server(connectionSocket)

        connectionSocket.close()