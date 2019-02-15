from items import HUBCAT, DAB_RIG, MEAT, CAMERA

class Room:

    name = None
    description = None
    contents = []
    neighbors = {}

    def print_contents(self):
        if len(self.contents) == 0:
            print("There is nothing in the room")
        else:
            print("The contents of the room are as follows:")
            for item in self.contents:
                item.print()

    def print_description(self):
        print(f"You are in {self.name}.")
        print("")
        print(self.description)

    def print_neighbors(self):
        print("You can go the following directions:")
        for direction, room in self.neighbors.items():
            print(direction + " to " + room.name)

    def get_item(self, name):
        for idx, item in enumerate(self.contents):
            if name.lower() == item.name.lower():
                return self.contents.pop(idx)
        else:
            return None


class ChandlersRoom(Room):

    name = "Chandler's Room"
    description = "The air is heavy with weed smoke and soundcloud rap."
    contents = [DAB_RIG]


class LivingRoom(Room):

    name = "Living Room"
    description = "The walls are awfully bare."
    contents = [HUBCAT]


class Hallway(Room):

    name = "The Hallway"
    description = "You must be going somewhere, otherwise why are you here?"


class Kitchen(Room):

    name = "Kitchen"
    description = "Someone's cooking some fucking MEAT."
    contents = [MEAT]


class BowmansRoom(Room):

    name = "Bowman's Room"
    description = "Screeching vocals emanate from a blanket fort."


class TamirsRoom(Room):

    name = "Tamir's Room"
    description = "Shit, it's clean in here."
    contents = [CAMERA]


class Backyard(Room):

    name = "Backyard"
    description = "Ahh the great outdoors. Beautiful day for a picture."\
        "Oh hey, there's Sam making beats with a log!"


CHANDLERS_ROOM = ChandlersRoom()
LIVING_ROOM = LivingRoom()
HALLWAY = Hallway()
KITCHEN = Kitchen()
BOWMANS_ROOM = BowmansRoom()
TAMIRS_ROOM = TamirsRoom()
BACKYARD = Backyard()


CHANDLERS_ROOM.neighbors = {'west': HALLWAY, 'south': BACKYARD}
HALLWAY.neighbors = {'south': CHANDLERS_ROOM, 'north': LIVING_ROOM, 'east': BOWMANS_ROOM, 'west': TAMIRS_ROOM}
LIVING_ROOM.neighbors = {'south': HALLWAY, 'west': KITCHEN}
KITCHEN.neighbors = {'east': LIVING_ROOM}
BOWMANS_ROOM.neighbors = {'west': HALLWAY}
TAMIRS_ROOM.neighbors = {'east': HALLWAY}
BACKYARD.neighbors = {'north': CHANDLERS_ROOM}
