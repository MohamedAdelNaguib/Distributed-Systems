"""
Module for sending multicast 
type broadcast to the hosts 
on the cluster network.

@Author: R. Erdem Uysal
"""

# Import necessary modules
import socket
import pickle
from cluster import configs


# Define broadcast adress
broadcast_adress = (
    configs.BROADCAST_IP, 
    configs.BROADCAST_PORT
)
# Create a UDP socket for broadcast
socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
# Define a timeout for the socket
socket.settimeout(1)
# Set the socket to broadcast
socket.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)
# Enable socket for reusing addresses
socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)


def send_broadcast_request():
    """
    Sends its own group view of the cluster
    to the host which makes broadcast request.
    """

    # Format message with pickle
    broadcast_message = pickle.dumps(
        [
            configs.SERVER_LIST,
            configs.CLIENT_LIST,
        ]
    )

    socket.sendto(broadcast_message, broadcast_adress)
    print("[INFO] Sending broadcast request...")
    print("[INFO] Broadcast sender: \n", configs.MY_IP)

    # If receive data through the socket is successfull, return true
    try:
        data, addr = socket.recvfrom(configs.BUFFER_SIZE)
        print("Received broadcast message:", data.decode())
    # Otherwise, return false
    except socket.timeout:
        pass
        return False