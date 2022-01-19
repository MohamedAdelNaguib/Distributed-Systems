import multiprocessing
import socket
import db
import json
import pickle


def get_neighbour(ring, current_node_ip, direction='left'):
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


class Server(multiprocessing.Process):
    customers = json.loads(db.Customer)
    hotels = json.loads(db.Hotel)
    booking = json.loads(db.Booking)
    rooms = json.loads(db.Room)
    members = ['127.234.204.3', '127.234.204.2', '127.234.204.4', '127.234.204.1', '127.234.204.5']

    def __init__(self, id, server_socket, received_data, client_address):
        super(Server, self).__init__()
        self.id = id
        self.server_socket = server_socket
        self.received_data = received_data
        self.client_address = client_address
        self.leader = False
        self.ring = self.form_ring()
        self.leader_id = ''
        self.participant = False

    # Override run method
    def run(self):
        query = self.received_data.decode().split('(')
        print("46 : " + self.received_data.decode())
        if query[0] == "get_hotels_by_name":
            message = eval("self." + self.received_data.decode())
            self.server_socket.sendto(pickle.dumps(message), self.client_address)
        elif query[0] == "book_room":
            message = eval("self." + self.received_data.decode())
            self.server_socket.sendto(pickle.dumps(message), self.client_address)
        elif query[0] == "elect":
            eval("self." + self.received_data.decode())
        elif query[0] == "election":
            self.election()
            self.server_socket.sendto(str.encode("done"), self.client_address)
            # self.server_socket.sendto(pickle.dumps(message), self.client_address)
        # Send message to client
        # self.server_socket.sendto(str.encode("This is server" + str(os.getpid())),self.client_address)
        # self.server_socket.sendto(pickle.dumps(message), self.client_address)

    def election(self):
        neighbour = get_neighbour(self.ring, self.id)
        self.participant = True
        self.server_socket.sendto(str.encode("elect( '" + str(self.id) + "'" + "," + "False)"), (neighbour, 4000))

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

    def form_ring(self):
        if self.members:
            sorted_binary_ring = sorted([socket.inet_aton(member) for member in self.members])
            # print(sorted_binary_ring)
            sorted_ip_ring = [socket.inet_ntoa(node) for node in sorted_binary_ring]
            # print(sorted_ip_ring)
            return sorted_ip_ring
        else:
            return []

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

    def elect(self, id, isLeader):
        neighbour = get_neighbour(self.ring, self.id)
        if isLeader is True:
            if id != self.id:
                self.leader_id = id
                self.participant = False
                self.server_socket.sendto(str.encode("elect( '" + str(id) + "'" + "," + "True" + ")"),
                                          (neighbour, 4000))
            else:
                self.leader_id = id
                self.participant = False
                print(self.leader_id)
        if id < self.id and not self.participant:
            self.participant = True
            self.server_socket.sendto(str.encode("elect( '" + str(self.id) + "'" + "," + "False" + ")"),
                                      (neighbour, 4000))
        elif id > self.id and not self.participant:
            self.participant = True
            self.server_socket.sendto(str.encode("elect( '" + str(id) + "'" + "," + "False" + ")"), (neighbour, 4000))
        elif id == self.id:
            self.leader_id = self.id
            self.participant = False
            self.server_socket.sendto(str.encode("elect( '" + str(self.id) + "'" + "," + "True" + ")"),
                                      (neighbour, 4000))


if __name__ == "__main__":
    # Create a UDP socket
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    # Server application IP address and port
    # server_address = '127.0.0.1'
    server_port = 4000
    server_address = input("Enter your value for the IP: ")
    # print(type(server_address))

    # Buffer size
    buffer_size = 1024

    # Bind socket to address and port
    server_socket.bind((server_address, server_port))
    print('Server up and running at {}:{}'.format(server_address, server_port))
    # print(server_socket.gethostbyaddr(server_address))
    i = 0
    while True:
        i += 1
        # Receive message from client
        data, address = server_socket.recvfrom(buffer_size)
        print('Received message \'{}\' at {}:{}'.format(data.decode(), address[0], address[1]))
        # Create a server process
        p = Server(server_address, server_socket, data, address)
        if (i % 10 == 0):
            print(p.leader_id)
        p.start()
        p.join()
        # print(p.ring)
        # ne = get_neighbour(p.ring, server_address)
        # p.server_socket.sendto(str.encode("elect(" + str(p.id) + "," + "False" + ")"), (ne, 95))
        # if p.leader_id != '':
        #     print(p.leader_id)
