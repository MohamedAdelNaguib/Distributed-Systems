"""
Module for sending multicast 
type broadcast to the hosts on 
the cluster network.

@Author: R. Erdem Uysal
"""

# Import necessary modules
import socket
import pickle
import configs

# Define broadcast adress
broadcast_ip = configs.BROADCAST_IP
server_address = ('', configs.BROADCAST_PORT)
# Create a UDP socket for broadcast
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
# Bind socket to the server adress
sock.bind(server_address)
# Set the socket to broadcast
sock.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)
# Enable socket for reusing addresses
# s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)


def receive_broadcast_request():
    """
    Receive a broadcast message from a 
    host in the cluster who wants to join.
    """

    while True:
        try:
            data, addr = sock.recvfrom(configs.BUFFER_SIZE)
            print("[INFO] Receiver {configs.MY_IP}] broadcast request from {address}\n")
        except KeyboardInterrupt:
            print("[ERROR] UDP socket terminated...")


if __name__ == '__main__':
# Main driver 
    receive_broadcast_request()