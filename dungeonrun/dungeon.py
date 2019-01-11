class Map:
    def __init__(self, size):
        if size not in [4, 5, 8]:
            raise Exception("Wrong size")
        self.size = size
        self.matrix = tuple(tuple(Room(col, row) for col in range(size)) for row in range(size))

        corner = {'NW': self.matrix[0][0], 'NE': self.matrix[0][size-1], 'SW': self.matrix[size-1][0], 'SE': self.matrix[size-1][size-1]}

    def enterDoor(self, currentRoom, door):
        newRoom = currentRoom
        x = currentRoom.position[0]
        y = currentRoom.position[1]
        if door.lower() == "west":
            newRoom= self.matrix[x-1][y]
        elif door.lower() == "north":
            newRoom = self.matrix[x][y-1]
        elif door.lower() == "east":
            newRoom = self.matrix[x+1][y]
        elif door.lower() == "south":
            newRoom = self.matrix[x][y+1]
        else:
            raise Exception("How did you enter else?")
        return newRoom

        corner = {
                'NW': self.matrix[0][0],
                'NE': self.matrix[0][size-1],
                'SW': self.matrix[size-1][0],
                'SE': self.matrix[size-1][size-1]
                }

    def generateRooms(self):
        for room in self.matrix[3]:
            room.doors[0] = False
class Room:

    def __init__(self, col, row, isDark=True, hasExit=False,
                 monsters=[], treasures=[], doors=[True, True, True, True]):
        self.dark, self.hasExit = isDark, hasExit
        self.monsters, self.treasures = monsters, treasures

        # DOORS N E S W
        self.doors = doors

        # Position X,Y tuple
        self.position = (col, row)

    def getCoords(self):
        print(self.position)
