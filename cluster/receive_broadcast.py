"""
Module for sending multicast 
type broadcast to the hosts on 
the cluster network.

@Author: R. Erdem Uysal
"""

# Import necessary modules
import socket
import pickle
from cluster import configs

# Define broadcast adress
broadcast_ip = configs.BROADCAST_IP
server_address = ('', configs.BROADCAST_PORT)
# Create a UDP socket for broadcast
socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
# Bind socket to the server adress
socket.bind(server_address)
# Set the socket to broadcast
socket.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)
# Enable socket for reusing addresses
socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)


def receive_broadcast_request():
    """
    Receive a broadcast message from a 
    host in the cluster who wants to join.
    """

    while True:
        try:
            data, addr = socket.recvfrom(configs.BUFFER_SIZE)
            print("[INFO] Receiver {configs.MY_IP}] broadcast request from {address}\n')
        except KeyboardInterrupt:
            print("[ERROR] UDP socket terminated...")