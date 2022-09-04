from util import *

# HashMap is the core data structure containing the packages.  Hashmap
# in general operate on O(1) for inserts and lookups as the key-value relations ship,
# make operation very fast.  However, this is under ideal circumstances with little or no collisions
# and balance accross the map
# Source: Joe james "Python: Creating a Hashmap using List"
class HashMap:
    def __init__(self, size):
        self.size = size
        self.map = [None] * self.size


    # Most basic hash function using package id for key_hash
    def _get_hash(self, key):
        return key % self.size

    # insert function works in O(1) as the check using the key is O(1) and then, when a collision
    # occurs, the check for update or add is O(1)
    def add(self, key, value):
        key_hash = self._get_hash(key)
        key_value = [key, value]

        if self.map[key_hash] is None:
            self.map[key_hash] = list([key_value])
            return True
        else:
            for pair in self.map[key_hash]:
                if pair[0] == key:
                    pair[1] = value
                    return True
            self.map[key_hash].append(key_value)
            return True

    # get function works in O(1) as the check using the key is O(1) and then, when a collision
    # occurs, the check for update or add is O(n).  For a balanced map, the collisions should be minimal
    def get(self, key):
        key_hash = self._get_hash(key)
        if self.map[key_hash] is not None:
            for pair in self.map[key_hash]:
                if pair[0] == key:
                    return pair[1]
        return None

    def delete(self, key):
        key_hash = self._get_hash(key)

        if self.map[key_hash] is None:
            return False
        for i in range ( 0, len(self.map[key_hash])):
            if self.map[key_hash][i][0] == key:
                self.map[key_hash].pop(i)
                return True

    def print(self):
        print('----Stuff----')
        for item in self.map:
            if item is not None:
                print(str(item))

    # Displays the status of the whole map by iterating through all the slots
    # Runs in O(n)
    def status(self, time):
        for i in range(1, len(self.map) + 1):
            if self.get(i) is not None:
                self.get(i).get_status(time)
            else:
                continue






