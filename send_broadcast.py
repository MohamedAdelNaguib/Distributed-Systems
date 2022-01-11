import socket
import pickle


def send_broadcast(ip, port, broadcast_message):
    # Create a UDP socket
    broadcast_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    broadcast_socket.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)
    broadcast_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    # Send message on broadcast address
    broadcast_socket.sendto(str.encode(broadcast_message), (ip, port))
    broadcast_socket.close()


if __name__ == '__main__':
    # Broadcast address and port
    BROADCAST_IP = "192.168.0.255"
    BROADCAST_PORT = 5973

    # Local host information
    MY_HOST = socket.gethostname()
    MY_IP = socket.gethostbyname(MY_HOST)
    print('My IP:', MY_IP)

    BUFFER_SIZE = 4096
    GROUP_VIEW = []

    # Send broadcast message
    message = MY_IP + ' sent a broadcast'
    send_broadcast(BROADCAST_IP, BROADCAST_PORT, message)
    print("Sent a broadcast")

    print("Listening for a reply")
    # Create a UDP socket
    listen_reply = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    while True:
        data, addr = listen_reply.recvfrom(BUFFER_SIZE)
        if data:
            print("Received broadcast message:", data.decode())