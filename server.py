import socket
import db
import json
import pickle
import threading
import configs
import receive_broadcast
import send_broadcast


class Server():
    customers = json.loads(db.Customer)
    hotels = json.loads(db.Hotel)
    booking = json.loads(db.Booking)
    rooms = json.loads(db.Room)

    def __init__(self, ID, clients_socket):
        # threading.Thread.__init__(self)
        self.ID = ID
        self.clients_socket = clients_socket
        # self.servers_socket = servers_socket
        self.leader = False
        self.leader_id = ''
        self.participant = False
        # self.ring = self.form_ring()

    def server_logic(self, received_data, client_address):
        query = received_data.decode().split('(')
        print("54 : " + received_data.decode())
        if query[0] == "get_hotels_by_name":
            message = eval("self." + received_data.decode())
            self.clients_socket.sendto(pickle.dumps(message), client_address)
        elif query[0] == "book_room":
            message = eval("self." + received_data.decode())
            self.clients_socket.sendto(pickle.dumps(message), client_address)
        elif query[0] == "elect":
            eval("self." + received_data.decode())
        elif query[0] == "election":
            self.election()
        elif query[0] == "close":
            self.clients_socket.close()
        elif query[0] == "leader":
            self.clients_socket.sendto(str.encode(self.leader_id), client_address)

    def get_hotels_by_name(self, name=None, country=None, city=None):
        result = []
        for hotel in self.hotels:
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

    def book_room(self, room_id):
        result = []
        for room in self.rooms:
            if room_id == room['roomID'] and room['availability'] == 1:
                temp = room
                temp['availability'] = 0
                self.rooms.remove(room)
                self.rooms.append(temp)
                result.append(temp)
        return result

    def election(self):
        neighbour = get_neighbour(self.ID)
        print(" 107 neighbour is : " + neighbour)
        self.participant = True
        # print("109" + self.participant)
        self.clients_socket.sendto(str.encode("elect('" + str(self.ID) + "'" + "," + "False)"), (neighbour, 4000))
        print("111 done")

    def elect(self, received_id, isLeader):
        neighbour = get_neighbour(self.ID)
        if isLeader is True:
            print("116 here")
            if received_id != self.ID:
                print("118 here")
                self.leader_id = received_id
                print(self.leader_id)
                self.participant = False
                self.clients_socket.sendto(str.encode("elect('" + str(received_id) + "'" + "," + "True" + ")"),
                                           (neighbour, 4000))
            else:
                leader_id = received_id
                self.participant = False
                return leader_id
        elif received_id < self.ID and not self.participant:
            print("126 received_id < ID ******************************************************")
            print("128" + str("elect('" + str(self.ID) + "'" + "," + "False" + ")"))
            self.participant = True
            self.clients_socket.sendto(str.encode("elect('" + str(self.ID) + "'" + "," + "False" + ")"),
                                       (neighbour, 4000))
        elif received_id > self.ID:
            print("133 received_id > ID ||||||||||||||||||||||||||||||||||||||||||||||||||||||")
            print(str("134 elect('" + str(received_id) + "'" + "," + "False" + ")"))
            self.participant = True
            self.clients_socket.sendto(str.encode("elect('" + str(received_id) + "'" + "," + "False" + ")"),
                                       (neighbour, 4000))
        elif received_id == self.ID:
            print("139 received_id == ID--------------------------------------------------------")
            print(str("140 elect('" + str(self.ID) + "'" + "," + "True" + ")"))
            self.leader_id = self.ID
            self.participant = False
            self.clients_socket.sendto(str.encode("elect('" + str(self.ID) + "'" + "," + "True" + ")"),
                                       (neighbour, 4000))


def client_handler():
    try:
        while True:
            # Receive message from client
            data, address = my_server.clients_socket.recvfrom(1024)
            print('158 : Received message \'{}\' at {}:{}'.format(data.decode(), address[0], address[1]))
            c_thread = threading.Thread(target=my_server.server_logic, args=(data, address))
            c_thread.start()
    except KeyboardInterrupt:
        my_server.clients_socket.close()


def form_ring():
    if configs.SERVER_LIST:
        sorted_binary_ring = sorted([socket.inet_aton(member) for member in configs.SERVER_LIST])
        sorted_ip_ring = [socket.inet_ntoa(node) for node in sorted_binary_ring]
        return sorted_ip_ring
    else:
        return []


def get_neighbour(current_node_ip, direction='left'):
    ring = form_ring()
    current_node_index = ring.index(current_node_ip) if current_node_ip in ring else -1
    if current_node_index != -1:
        if direction == 'left':
            if current_node_index + 1 == len(ring):
                return ring[0]
            else:
                return ring[current_node_index + 1]
        else:
            if current_node_index == 0:
                return ring[len(ring) - 1]
            else:
                return ring[current_node_index - 1]
    else:
        return None


if __name__ == "__main__":
    # IP = input("Enter your value for the IP: ")
    MY_HOST = socket.gethostname()
    IP = socket.gethostbyname(MY_HOST)
    # members = configs.SERVER_LIST
    # members.append(str(IP))
    # print(members)
    clients_port = 4000
    # servers_port = 4002
    clients_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    clients_socket.bind((IP, clients_port))
    print('Server up and running at {}:{}'.format(IP, clients_port))
    my_server = Server(IP, clients_socket)
    send_broadcast.send_broadcast_request()
    client_thread = threading.Thread(target=client_handler)
    rec_thread = threading.Thread(target=receive_broadcast.receive_broadcast_request)
    client_thread.start()
    rec_thread.start()
