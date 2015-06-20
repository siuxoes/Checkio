__author__ = 'Siuxoes'
from itertools import chain

class Friends:
    def __init__(self, connections):
        self.connections = list(connections)

    def add(self, connection):
        if connection in self.connections:
            return False
        else:
            self.connections.append(connection)
            return True

    def remove(self, connection):
        if connection in self.connections:
            self.connections.remove(connection)
            return True
        else:
            return False

    def names(self):
        return set(chain(*self.connections))

    def connected(self, name):
        neighbors = []
        [neighbors.extend(list(i)) for i in self.connections if name in i]
        neighbors = set(neighbors)
        if name in set(neighbors):
            neighbors.remove(name)
        return neighbors

f = Friends(({"nikola", "sophia"}, {"stephen", "robot"}, {"sophia", "pilot"}))
print(f.connected("nikola"))