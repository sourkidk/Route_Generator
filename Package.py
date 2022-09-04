import sys
from util import *
class Package:
    def __init__(self, id, address, city, state, zip, deadline, mass, notes):
        self.id = id
        self.address = address
        self.city = city
        self.state = state
        self.zip = zip
        self.deadline = deadline
        self.mass = mass
        self.notes = notes
        self.status = "At Hub"
        self.location = -1
        self.loaded_time = sys.maxsize
        self.delivery_time = sys.maxsize

    def __str__(self):
        return '{self.id}: {self.address} : {self.deadline}'.format(self=self)

    # def __repr__(self):
        # return 'Package_#: {self.id}'.format(self=self)

    def __repr__(self):
        return 'Package_#: {self.id} : {self.status}'.format(self=self)

    def deliver_package(self):
        self.status = "Delivered"

    def get_status(self, time: int):

        if int(self.delivery_time) <= time:
            status = f'Delivered @ {minutes_to_time(self.delivery_time)}'
        elif int(self.loaded_time) <= time:
            status = f'Loaded @ {minutes_to_time(self.loaded_time)}'
        else:
            status = "At HUB"

        message = f'Package: {self.id} Address: {self.address}  {status}'

        print(message)
        print('----------')




