# setup the game world
from models import InventoryItem, Room, Player

DAB_RIG = InventoryItem(name="Dab Rig", description="This item will make you very high.")
HUBCAT = InventoryItem(name="Hubcat", description="This little guy is a hubcat. Hello hubcat.")
MEAT = InventoryItem(name="Meat", description="This is Bowman's meat. Beware.")
BOWMAN = InventoryItem(name="Bowman", description="This is Bowman. He is a human and needs meat to maintain his loudness.")
LIGHTER = InventoryItem(name="Lighter", description="This is a lighter. It makes things hot af.")

CHANDLERS_ROOM = Room(name="Chandler's Room", description="The air is heavy with weed smoke and soundcloud rap.", contents = [DAB_RIG])
LIVING_ROOM = Room(name="The Living Room", description="The walls are awfully bare.", contents=[HUBCAT])
HALLWAY = Room(name="The Hallway", description="You must be going somewhere, otherwise why are you here?")
KITCHEN = Room(name="The Kitchen", description="Someone's cooking some fucking MEAT.", contents=[MEAT])
BOWMANS_ROOM = Room(name="Bowman's Room", description="Screeching vocals emanate from a blanket fort.", contents = [BOWMAN, LIGHTER])

CHANDLERS_ROOM.neighbors = {'west': HALLWAY}
HALLWAY.neighbors = {'south': CHANDLERS_ROOM, 'north': LIVING_ROOM, 'east': BOWMANS_ROOM}
LIVING_ROOM.neighbors = {'south': HALLWAY, 'west': KITCHEN}
KITCHEN.neighbors = {'east': LIVING_ROOM}
BOWMANS_ROOM.neighbors = {'west': HALLWAY}


def run_game():
	player = Player(name='chandler', location=KITCHEN)
	while True:
		player.location.print_description()
		player.location.print_contents()
		player.location.print_neighbors()

		raw = input("Whatchu wanna do? ")
		raw = raw.split(" ")
		action = raw[0]
		if action.lower() == "go":
			destination = raw[1]
			if destination in player.location.neighbors.keys():
				player.location = player.location.neighbors[destination]
			else:
				print("You can't go there asshole")
		elif action.lower() == "get":
			item_name = " ".join(raw[1:])
			item = player.location.get_item(item_name)
			if item is not None:
				player.inventory.append(item)
			else:
				print("I don't see that")
		elif action.lower() == "inventory":
			player.print_inventory()
		#elif action.lower() == "use"

run_game()