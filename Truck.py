from HashMap import HashMap
class Truck:
    def __init__(self, truck_id, weight, driver, miles_driven, location):
        self.truck_id = truck_id
        self.weight = weight,
        self.num_packages = len(self.packages)
        self.packages = []
        self.driver = driver
        self.miles_driven = miles_driven
        self._speed = 18
        self.route = []
        self.pack_map = HashMap(16)
        self.location = location
