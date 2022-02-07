"""
Module for sending multicast 
type broadcast to the hosts on 
the cluster network.

@Author: R. Erdem Uysal
"""

# Import necessary modules
import sys
import socket
import pickle
import configs


server_address = ('', configs.BROADCAST_PORT)
# Create a UDP socket for broadcast
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
# Bind socket to the server adress
sock.bind(server_address)
# Set the socket to broadcast
sock.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)
# Enable socket for reusing addresses 
# Therefore we will be able to run multiple 
# clients and servers on single (host, port)
sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

def receive_broadcast_request():
    """
    Receive a broadcast message from a 
    host in the cluster who wants to join.
    """

    while True:
        try:
            data, addr = sock.recvfrom(configs.BUFFER_SIZE)
            print(f"[INFO] {configs.MY_IP} received broadcast message from {addr}.\n", file=sys.stderr)
            configs.CLIENT_LIST.append(addr[0]) if addr[0] not in configs.CLIENT_LIST else print()
            print(f"[INFO] {addr[0]} has been added to the group view.\n", file=sys.stderr)

            # print(f"[INFO] Received message: {pickle.loads(data)[0]}")
            # # Update leader of the host
            # configs.LEADER = pickle.loads(data)[0]
            # # Update server list of the host
            # configs.SERVER_LIST = pickle.loads(data)[1]
            # # Update client list of the host
            # configs.CLIENT_LIST = pickle.loads(data)[2]
            # print(f"[INFO] \nLeader: {configs.LEADER} \nServer list: {configs.SERVER_LIST} \nClient list: {configs.CLIENT_LIST}")


            # Format message with pickle
            reply_message = pickle.dumps(
                [
                    #configs.MY_IP
                    configs.SERVER_LIST,
                    configs.CLIENT_LIST,
                ]
            )

            sock.sendto(reply_message, addr)
            print(f"[INFO] Group view sent to {addr[0]}\n", file=sys.stderr)

        except KeyboardInterrupt:
            print("[ERROR] UDP socket terminated...", file=sys.stderr)
            sys.exit()


# if __name__ == '__main__':
# # Main driver 
#     receive_broadcast_request()