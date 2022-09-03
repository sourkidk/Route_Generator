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

    def __str__(self):
        return '{self.id}: {self.address} : {self.deadline}'.format(self=self)

    def __repr__(self):
        return 'Package_#: {self.id}'.format(self=self)

    def __repr__(self):
        return 'Package_#: {self.id} : {self.status}'.format(self=self)

    def deliver_package(self):
        self.status = "Delivered"




