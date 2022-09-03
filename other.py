def move_to_nearest_stop(self, graph):
    coordinate_list = [(self.current_stop, i) for i in self.stops]
    # print(coordinate_list)

    distance, next_stop = min((graph.edge_weights[k], k) for k in coordinate_list)

    self.miles_driven += distance
    self.stops.remove(next_stop[1])
    self.current_stop = next_stop[1]

    self.show_route_specs(distance, next_stop)

def move_to_specific_stop(self, graph, stop):
    coordinate = (self.current_stop, stop)
    # print(coordinate)
    next_stop = stop
    distance = graph.edge_weights[coordinate]
    self.miles_driven += distance
    self.stops.remove(stop)
    self.current_stop = stop

    self.show_route_specs(distance,next_stop)