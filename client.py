import socket
import multiprocessing
import os
import pickle


def send_message(s_address, s_port):
    # Create a UDP socket
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    # Message sent to server
    # message = "get_hotels_by_name(name='A',country='Germany',city='berlin')"
    message = "election"

    # Send data
    client_socket.sendto(str.encode(message), (s_address, s_port))
    print('Sent to server: ', message)
    # Receive response from server
    print('Waiting for response...')
    data, server = client_socket.recvfrom(1024)
    print('Received message: ', pickle.loads(data))


if __name__ == '__main__':

    # Server application IP address and port
    server_address = '127.234.204.5'
    server_port = 4000

    for i in range(1):
        # Spawn three client processes
        p = multiprocessing.Process(target=send_message, args=(server_address, server_port))
        p.start()
        p.join
