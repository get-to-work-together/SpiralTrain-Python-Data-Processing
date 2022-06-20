import sys
import socket
from communication_handler import Handler

IP_ADDRESS = '0.0.0.0'   # all of localhost '127.0.0.1'
IP_PORT = 6669

class Listener:

    def __init__(self, host, port):
        self.host = host
        self.port = port

    def listen(self, handler):
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        print('Socket created')

        try:
            s.bind((self.host, self.port))
            
        except socket.error as err:
            print('Bind failed. Error Code: %s Message %s' % (err[0], err[1]))
            sys.exit()
            
        except Exception as err:
            print(err)
            sys.exit()

        print('Socket bind complete')

        s.listen()
        print('Listening on %s on port %d' % (self.host, self.port))

        conn, client_addr = s.accept()
        print('Connection from : ' + str(client_addr))

        try:
            pass
            handler(conn, client_addr)

        except:
            print('Client closed connection.')

        conn.close()
        print('Done. Connection closed.')


def main():
    handler = Handler()

    listener = Listener(IP_ADDRESS, IP_PORT)
    listener.listen(handler.handler)

    # handler.handler()

if __name__ == '__main__':
    main()