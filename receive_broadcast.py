import socket
import pickle


def send_reply(ip, port, reply_message):
    # Create a UDP socket
    reply_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    reply_socket.bind((ip, port))
    reply_socket.sendto(str.encode(reply_message), (ip, port))
    reply_socket.close()

if __name__ == '__main__':
    # Broadcast address and port
    BROADCAST_IP = "192.168.0.255"
    BROADCAST_PORT = 5973

    # Local host information
    MY_HOST = socket.gethostname()
    MY_IP = socket.gethostbyname(MY_HOST)

    BUFFER_SIZE = 1024
    GROUP_VIEW = []
    #GROUP_VIEW.append(MY_IP) if MY_IP not in GROUP_VIEW else None

    # Create a UDP socket
    listen_broadcast = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    # Set the socket to broadcast and enable reusing addresses
    listen_broadcast.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)
    listen_broadcast.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    # Bind socket to address and port
    listen_broadcast.bind((BROADCAST_IP, BROADCAST_PORT))

    print("Listening to broadcast messages")

    while True:
        data, addr = listen_broadcast.recvfrom(BUFFER_SIZE)
        print("Received broadcast message:", data.decode())
        if addr[0] not in GROUP_VIEW:
            GROUP_VIEW.append(addr[0])
            print('New participant: ', data.split()[0].decode())
            message = MY_IP + ' sent a reply'
            print('Sent a reply to', addr[0], ':', BROADCAST_PORT)
            send_reply(addr[0], BROADCAST_PORT, message)
