"""
Module for sending multicast 
type broadcast to the hosts 
on the cluster network.

@Author: R. Erdem Uysal
"""

# Import necessary modules
import sys
import socket
import pickle
import time
import configs

# Define broadcast adress
broadcast_adress = (configs.BROADCAST_IP, configs.BROADCAST_PORT)
# Create a UDP socket for broadcast
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
# Set the socket to broadcast
sock.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)
# Enable socket for reusing addresses 
# Therefore we will be able to run multiple 
# clients and servers on single (host, port)
sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
# Define a timeout for the socket
sock.settimeout(1)


def send_broadcast_request():
    """
    Sends its own group view of the cluster
    to the host which makes broadcast request.
    """

    # Format message with pickle
    broadcast_message = pickle.dumps(
        [
            configs.MY_IP
            #configs.GROUP_LEADER,
            #configs.SERVER_LIST,
            #configs.CLIENT_LIST,
        ]
    )

    sock.sendto(broadcast_message, broadcast_adress)
    print("[INFO] Broadcast message sent...\n", file=sys.stderr)
    # print("[INFO] Broadcast sender: ", configs.MY_IP)
    time.sleep(1)

    # If receive data through the socket is successfull, return true
    try:
        data, addr = sock.recvfrom(configs.BUFFER_SIZE)
        print(f"[INFO] {configs.MY_IP} received reply message from {addr}\n", file=sys.stderr)
        print(f"[INFO] Reply message {pickle.loads(data)}\n", file=sys.stderr)
        configs.SERVER_LIST = pickle.loads(data)[0]
        configs.CLIENT_LIST = pickle.loads(data)[1]
        print(f"[INFO] Group view has been updated.\n", file=sys.stderr)
        return True

    # Otherwise, return false
    except socket.timeout:
        return False

# if __name__ == '__main__':
# # Main driver 
#     send_broadcast_request()