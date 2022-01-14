"""
This is a configuration file where
all the global variables declared 
shared by multiple modules.

@Author: R. Erdem Uysal
"""

# Import necessary modules
import socket


# Local host information
MY_HOST = socket.gethostname()
MY_IP = socket.gethostbyname(MY_HOST)

# Broadcast information
BROADCAST_IP= '192.168.0.255'

# Port information
# Ubiquiti UniFi access points broadcast
# to 255.255.255.255:10001 (UDP) to locate the controller(s)
# https://en.wikipedia.org/wiki/List_of_TCP_and_UDP_port_numbers 
BROADCAST_PORT = 10001

# Group view information
GROUP_LEADER = ''  # Index 0
SERVER_LIST = []  # Index 1
CLIENT_LIST = []  # Index 2

# Socket connection parameters
BUFFER_SIZE = 1024
UNICODE = 'utf-8'

# State parameters
CLIENT_STATE = False