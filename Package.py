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

    def __str__(self):
        return '{self.id}: {self.deadline}'.format(self=self)




