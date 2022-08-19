from HashMap import HashMap
class Truck:
    def __init__(self, truck_id, weight, num_packages, driver, miles_driven):
        self.truck_id = truck_id
        self.weight = weight,
        self.num_packages = num_packages
        self.driver = driver
        self.miles_driven = miles_driven
        self._speed = 18
        self.route = []
        self.pack_map = HashMap(16)
