from models import Room
from items import HUBCAT, BOWMAN, DAB_RIG, MEAT, CAMERA

CHANDLERS_ROOM = Room(name="Chandler's Room", description="The air is heavy with weed smoke and soundcloud rap.", contents=[DAB_RIG])
LIVING_ROOM = Room(name="The Living Room", description="The walls are awfully bare.", contents=[HUBCAT])
HALLWAY = Room(name="The Hallway", description="You must be going somewhere, otherwise why are you here?")
KITCHEN = Room(name="The Kitchen", description="Someone's cooking some fucking MEAT.", contents=[MEAT])
BOWMANS_ROOM = Room(name="Bowman's Room", description="Screeching vocals emanate from a blanket fort.")
TAMIRS_ROOM = Room(name ="Tamir's Room", description ="Shit, it's clean in here", contents=[CAMERA])

CHANDLERS_ROOM.neighbors = {'west': HALLWAY}
HALLWAY.neighbors = {'south': CHANDLERS_ROOM, 'north': LIVING_ROOM, 'east': BOWMANS_ROOM, 'west': TAMIRS_ROOM}
LIVING_ROOM.neighbors = {'south': HALLWAY, 'west': KITCHEN}
KITCHEN.neighbors = {'east': LIVING_ROOM}
BOWMANS_ROOM.neighbors = {'west': HALLWAY}
TAMIRS_ROOM.neighbors = {'east': HALLWAY}