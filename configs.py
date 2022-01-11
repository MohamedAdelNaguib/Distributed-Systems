"""
This is a configuration file where
all the global variables declared 
shared by multiple modules.

@Author: R. Erdem Uysal
"""

# Import necessary modules
import socket


# Local host information
my_host = socket.gethostname()
my_ip = socket.gethostbyname(my_host)

# Socket connection parameters
buffer_size = 1024
unicode = 'utf-8'

# Broadcast information
broadcast_ip= '192.168.0.255'

# Group view information
server_list = []
client_list = []

# State parameters
client_running = False