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
BROADCAST_PORT = 10000

# Group view information
SERVER_LIST = []
CLIENT_LIST = []

# Socket connection parameters
BUFFER_SIZE = 1024
UNICODE = 'utf-8'

# State parameters
CLIENT_STATE = False