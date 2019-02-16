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

    def speak(self):
        print("\nYou say \"Arf.\" Good boy.\n")


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
        "Oh hey, there's Sam making beats on a log."


class FrontPorch(Room):

    name = "Front Porch"
    description = "Sam is out here gettin spliffed mon"
    description_alt = "There is no one here."\
                      "A thin layer of ash covers everything"

    sams_there = False

    def speak(self):
        print(f"{self.name}: \"Yo Sam, cash me ousside how bow dah?\"")
        print("Sam: \"Alright, I'll meet you at the chateau.\"")
        print("\nSam disappears around the corner. Some mysterious force"
              "prevents you from following him.")
        self.sams_there = True

    def print_description(self):
        print(f"You are in {self.name}.")
        print("")
        if self.sams_there is False:
            print(self.description)
        else:
            print(self.description_alt)


CHANDLERS_ROOM = ChandlersRoom()
LIVING_ROOM = LivingRoom()
HALLWAY = Hallway()
KITCHEN = Kitchen()
BOWMANS_ROOM = BowmansRoom()
TAMIRS_ROOM = TamirsRoom()
BACKYARD = Backyard()
FRONT_PORCH = FrontPorch()


CHANDLERS_ROOM.neighbors = {
    'west': HALLWAY,
    'south': BACKYARD
}

HALLWAY.neighbors = {
    'south': CHANDLERS_ROOM,
    'north': LIVING_ROOM,
    'east': BOWMANS_ROOM,
    'west': TAMIRS_ROOM
}

LIVING_ROOM.neighbors = {
    'south': HALLWAY,
    'west': KITCHEN,
    'north': FRONT_PORCH
}

KITCHEN.neighbors = {
    'east': LIVING_ROOM
}

BOWMANS_ROOM.neighbors = {
    'west': HALLWAY
}

TAMIRS_ROOM.neighbors = {
    'east': HALLWAY
}

BACKYARD.neighbors = {
    'north': CHANDLERS_ROOM
}

FRONT_PORCH.neighbors = {
    'south': LIVING_ROOM
}