# setup the game world
from models import Player
from rooms import LIVING_ROOM

def run_game():
	player = Player(name='chandler', location=LIVING_ROOM)
	#turn = 1

	while True:
		player.location.print_description()
		print("")
		player.location.print_contents()
		print("")
		player.location.print_neighbors()
		print("")

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
		elif action.lower() == "use":
			item_name = " ".join(raw[1:])
			player.use_item(item_name)
		#turn += 1
		elif action.lower() == "help":
			print("You can perform the following actions in Escape from the Skank:\n\ngo <direction> : This allows you to move to different areas  e.g. go east\nget <item_name> : This allows you to take an item from a room  e.g. get hubcat\nuse <item_name> : This allows you to use an item in your inventory  e.g. use meat\ninventory : This prints the contents of your inventory")


run_game()