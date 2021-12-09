import multiprocessing
import socket
import os
from pkgutil import resolve_name

import db
import json
import pickle


class Server(multiprocessing.Process):
    def __init__(self, server_socket, received_data, client_address):
        super(Server, self).__init__()
        self.server_socket = server_socket
        self.received_data = received_data
        self.client_address = client_address

    # Override run method
    def run(self):
        query = self.received_data.decode().split('(')
        print(self.received_data.decode())
        match query[0]:
            case "get_hotels_by_name": message = eval(self.received_data.decode())
            case "book_room": message = eval(self.received_data.decode())
        # Send message to client
        # self.server_socket.sendto(str.encode("This is server" + str(os.getpid())),self.client_address)
        self.server_socket.sendto(pickle.dumps(message), self.client_address)


customers = json.loads(db.Customer)
hotels = json.loads(db.Hotel)
booking = json.loads(db.Booking)
rooms = json.loads(db.Room)


def get_hotels_by_name(name=None, country=None, city=None):
    result = []
    for hotel in hotels:
        if name and country and city:
            if name == hotel['name'] and country == hotel['country'] and city == hotel['city']:
                result.append(hotel)
        elif name and country and hotel not in result:
            if name == hotel['name'] and country == hotel['country']:
                result.append(hotel)
        elif name and city and hotel not in result:
            if name == hotel['name'] and city == hotel['city']:
                result.append(hotel)
        elif city and country and hotel not in result:
            if city == hotel['city'] and country == hotel['country']:
                result.append(hotel)
        elif name and hotel not in result:
            if name == hotel['name']:
                result.append(hotel)
        elif country and hotel not in result:
            if country == hotel['country']:
                result.append(hotel)
        elif city and hotel not in result:
            if city == hotel['city']:
                result.append(hotel)
    return result


def book_room(room_id):
    result = []
    for room in rooms:
        if room_id == room['roomID'] and room['availability'] == 1:
            temp = room
            temp['availability'] = 0
            rooms.remove(room)
            rooms.append(temp)
            result.append(temp)
    return result



if __name__ == "__main__":
    # Create a UDP socket
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    # Server application IP address and port
    server_address = '127.0.0.1'
    server_port = 10001

    # Buffer size
    buffer_size = 1024

    # Bind socket to address and port
    server_socket.bind((server_address, server_port))
    print('Server up and running at {}:{}'.format(server_address, server_port))

    while True:
        # Receive message from client
        data, address = server_socket.recvfrom(buffer_size)
        # print('Received message \'{}\' at {}:{}'.format(data.decode(), address[0], address[1]))
        # Create a server process
        p = Server(server_socket, data, address)
        p.start()
        p.join()
