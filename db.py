import json

c = {"customerID": 1, "fullName": "A", "dateBirth": "15.05.1998"}, \
    {"customerID": 2, "fullName": "B", "dateBirth": "16.05.1998"}, \
    {"customerID": 3, "fullName": "C", "dateBirth": "17.05.1998"}, \
    {"customerID": 4, "fullName": "D", "dateBirth": "18.05.1998"}, \
    {"customerID": 5, "fullName": "E", "dateBirth": "19.05.1998"}, \
    {"customerID": 6, "fullName": "F", "dateBirth": "20.05.1998"}, \
    {"customerID": 7, "fullName": "G", "dateBirth": "21.05.1998"}, \
    {"customerID": 8, "fullName": "H", "dateBirth": "22.05.1998"}, \
    {"customerID": 9, "fullName": "I", "dateBirth": "23.05.1998"}, \
    {"customerID": 10, "fullName": "J", "dateBirth": "24.05.1998"}, \
    {"customerID": 11, "fullName": "K", "dateBirth": "25.05.1998"}, \
    {"customerID": 12, "fullName": "L", "dateBirth": "26.05.1998"}
Customer = json.dumps(c, indent=4)
h = {"hotelID": 1, "name": "A", "country": "Germany", "city": "Stuttgart", "address": "70569", "stars": "3"}, \
    {"hotelID": 2, "name": "B", "country": "France", "city": "Paris", "address": "70569", "stars": "5"}, \
    {"hotelID": 3, "name": "C", "country": "Austria", "city": "Vienna", "address": "70569", "stars": "6"}, \
    {"hotelID": 4, "name": "D", "country": "Turkey", "city": "Istanbul", "address": "70569", "stars": "5"}, \
    {"hotelID": 5, "name": "E", "country": "Spain", "city": "Barcelona", "address": "70569", "stars": "4"}, \
    {"hotelID": 6, "name": "F", "country": "Egypt", "city": "Cairo", "address": "70569", "stars": "7"}
Hotel = json.dumps(h, indent=4)
r = {"roomID": 101, "hotelID": "1", "capacity": "1", "availability": 0, "pricePerNight": "10"}, \
    {"roomID": 102, "hotelID": "1", "capacity": "2", "availability": 1, "pricePerNight": "20"}, \
    {"roomID": 103, "hotelID": "1", "capacity": "3", "availability": 0, "pricePerNight": "30"}, \
    {"roomID": 104, "hotelID": "1", "capacity": "4", "availability": 1, "pricePerNight": "35"}, \
    {"roomID": 105, "hotelID": "2", "capacity": "1", "availability": 1, "pricePerNight": "20"}, \
    {"roomID": 106, "hotelID": "2", "capacity": "2", "availability": 0, "pricePerNight": "35"}, \
    {"roomID": 107, "hotelID": "2", "capacity": "3", "availability": 0, "pricePerNight": "45"}, \
    {"roomID": 108, "hotelID": "2", "capacity": "4", "availability": 1, "pricePerNight": "50"}, \
    {"roomID": 109, "hotelID": "3", "capacity": "1", "availability": 1, "pricePerNight": "12"}, \
    {"roomID": 110, "hotelID": "3", "capacity": "2", "availability": 1, "pricePerNight": "15"}, \
    {"roomID": 111, "hotelID": "3", "capacity": "3", "availability": 1, "pricePerNight": "18"}, \
    {"roomID": 112, "hotelID": "3", "capacity": "4", "availability": 1, "pricePerNight": "20"}, \
    {"roomID": 113, "hotelID": "4", "capacity": "1", "availability": 1, "pricePerNight": "30"}, \
    {"roomID": 114, "hotelID": "4", "capacity": "2", "availability": 1, "pricePerNight": "50"}, \
    {"roomID": 115, "hotelID": "4", "capacity": "3", "availability": 1, "pricePerNight": "70"}, \
    {"roomID": 116, "hotelID": "4", "capacity": "4", "availability": 1, "pricePerNight": "100"}, \
    {"roomID": 117, "hotelID": "5", "capacity": "1", "availability": 1, "pricePerNight": "50"}, \
    {"roomID": 118, "hotelID": "5", "capacity": "2", "availability": 1, "pricePerNight": "75"}, \
    {"roomID": 119, "hotelID": "5", "capacity": "3", "availability": 1, "pricePerNight": "100"}, \
    {"roomID": 120, "hotelID": "5", "capacity": "4", "availability": 1, "pricePerNight": "125"}, \
    {"roomID": 121, "hotelID": "6", "capacity": "1", "availability": 1, "pricePerNight": "80"}, \
    {"roomID": 122, "hotelID": "6", "capacity": "2", "availability": 1, "pricePerNight": "100"}, \
    {"roomID": 123, "hotelID": "6", "capacity": "3", "availability": 1, "pricePerNight": "110"}, \
    {"roomID": 124, "hotelID": "6", "capacity": "4", "availability": 1, "pricePerNight": "125"}
Room = json.dumps(r, indent=4)
b = {"bookingID": 1, "date": "07.12.2019", "customerID": "1", "checkInDate": "10.12.2019",
     "checkOutDate ": "15.12.2019", "roomID": "101"}, \
    {"bookingID": 2, "date": "15.12.2019", "customerID": "2", "checkInDate": "20.12.2019",
     "checkOutDate ": "25.12.2019", "roomID": "102"}, \
    {"bookingID": 3, "date": "01.01.2020", "customerID": "3", "checkInDate": "10.01.2020",
     "checkOutDate ": "13.01.2020", "roomID": "103"}, \
    {"bookingID": 4, "date": "01.01.2020", "customerID": "4", "checkInDate": "10.01.2020",
     "checkOutDate ": "13.01.2020", "roomID": "104"}, \
    {"bookingID": 5, "date": "12.05.2020", "customerID": "5", "checkInDate": "17.05.2020",
     "checkOutDate ": "28.05.2020", "roomID": "105"}, \
    {"bookingID": 6, "date": "25.07.2020", "customerID": "6", "checkInDate": "01.8.2020",
     "checkOutDate ": "15.12.2020", "roomID": "106"}
Booking = json.dumps(b, indent=4)
# {"bookingID": "7", "date": "07.12.2019", "customerID": "1", "checkInDate": "10.12.2019",
#  "checkOutDate ": "15.12.2019", "roomID": "1"}, \
# {"bookingID": "8", "date": "07.12.2019", "customerID": "1", "checkInDate": "10.12.2019",
#  "checkOutDate ": "15.12.2019", "roomID": "1"}, \
# {"bookingID": "9", "date": "07.12.2019", "customerID": "1", "checkInDate": "10.12.2019",
#  "checkOutDate ": "15.12.2019", "roomID": "1"}, \
# {"bookingID": "10", "date": "07.12.2019", "customerID": "1", "checkInDate": "10.12.2019",
#  "checkOutDate ": "15.12.2019", "roomID": "1"}, \
# {"bookingID": "11", "date": "07.12.2019", "customerID": "1", "checkInDate": "10.12.2019",
#  "checkOutDate ": "15.12.2019", "roomID": "1"}, \
# {"bookingID": "12", "date": "07.12.2019", "customerID": "1", "checkInDate": "10.12.2019",
#  "checkOutDate ": "15.12.2019", "roomID": "1"}
# {"bookingID": "1", "date": "07.12.2019", "customerID": "1", "checkInDate": "10.12.2019",
#  "checkOutDate ": "15.12.2019", "roomID": "1"}, \
# {"bookingID": "1", "date": "07.12.2019", "customerID": "1", "checkInDate": "10.12.2019",
#  "checkOutDate ": "15.12.2019", "roomID": "1"}, \
# {"bookingID": "1", "date": "07.12.2019", "customerID": "1", "checkInDate": "10.12.2019",
#  "checkOutDate ": "15.12.2019", "roomID": "1"}, \
# {"bookingID": "1", "date": "07.12.2019", "customerID": "1", "checkInDate": "10.12.2019",
#  "checkOutDate ": "15.12.2019", "roomID": "1"}, \
# {"bookingID": "1", "date": "07.12.2019", "customerID": "1", "checkInDate": "10.12.2019",
#  "checkOutDate ": "15.12.2019", "roomID": "1"}, \
# {"bookingID": "1", "date": "07.12.2019", "customerID": "1", "checkInDate": "10.12.2019",
#  "checkOutDate ": "15.12.2019", "roomID": "1"}, \
# {"bookingID": "1", "date": "07.12.2019", "customerID": "1", "checkInDate": "10.12.2019",
#  "checkOutDate ": "15.12.2019", "roomID": "1"}, \
# {"bookingID": "1", "date": "07.12.2019", "customerID": "1", "checkInDate": "10.12.2019",
#  "checkOutDate ": "15.12.2019", "roomID": "1"}, \
# {"bookingID": "1", "date": "07.12.2019", "customerID": "1", "checkInDate": "10.12.2019",
#  "checkOutDate ": "15.12.2019", "roomID": "1"}, \
# {"bookingID": "1", "date": "07.12.2019", "customerID": "1", "checkInDate": "10.12.2019",
#  "checkOutDate ": "15.12.2019", "roomID": "1"}, \
# {"bookingID": "1", "date": "07.12.2019", "customerID": "1", "checkInDate": "10.12.2019",
#  "checkOutDate ": "15.12.2019", "roomID": "1"}, \
# {"bookingID": "1", "date": "07.12.2019", "customerID": "1", "checkInDate": "10.12.2019",
#  "checkOutDate ": "15.12.2019", "roomID": "1"}, \
# {"bookingID": "1", "date": "07.12.2019", "customerID": "1", "checkInDate": "10.12.2019",
#  "checkOutDate ": "15.12.2019", "roomID": "1"}
