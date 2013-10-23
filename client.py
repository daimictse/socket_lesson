import socket
import sys
import select


def main():
    #open_connection and returns a new socket connection
    my_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    my_socket.connect(("localhost", 5555))

    running = True
    while running:
        inputready, outputready, exceptready = select.select([my_socket, sys.stdin], [],[])

        for s in inputready:
            if s == my_socket:
                msg = s.recv(1024)

                if msg:
                    #format_message
                    if "::" in msg:
                        msg = msg.split("::")
                        print "[%s] %s"%(msg[0], msg[1])
                    else:
                        print msg
                    
                else:
                    running = False

            elif s == sys.stdin:
                msg = s.readline()
                #exit the program when user enters /quit
                if msg == "/quit\n":
                    running = False
                my_socket.sendall(msg)
                   
    print "Disconnected from the server!"   
    my_socket.close()

main()

