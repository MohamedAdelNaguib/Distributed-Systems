"""
This is a module for sending 
multicast type broadcast to
the hosts on the cluster network.

@Author: R. Erdem Uysal
"""

# Import necessary modules
import socket
import pickle
from cluster import configs


# Define broadcast adress
broadcast_adress = (
    configs.broadcast_ip, 
    configs.broadcast_ip
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
    """
    broadcast_message = pickle.dumps(
        [
            configs.server_list,
            configs.client_list,
        ]
    )

    socket.sendto(broadcast_message, broadcast_adress)
    print("[INFO] Sending broadcast request...")
    print("[INFO] Broadcast sender: \n", configs.my_ip)

    try:
        socket.recvfrom
    
    except socket.timeout:
        pass
        return False