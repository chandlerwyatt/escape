class InventoryItem:
	def __init__(self, name, description):
		self.name = name
		self.description = description

	def print(self):
		print(self.name + ":" + self.description)

class Room:
	def __init__(self, name, description, contents=[]):
		self.name = name
		self.description = description
		self.contents = contents
		self.neighbors = {}

	def print_contents(self):
		if len(self.contents) == 0:
			print("There is nothing in the room")
		else:
			print("The contents of the room are as follows:")
			for item in self.contents:
				item.print()

	def print_description(self):
		print(f"You are in {self.name}.")
		print(self.description)

	def print_neighbors(self):
		print("You can access the following rooms:")
		for direction, room in self.neighbors.items():
			print("Direction: " + direction + ", Room: " + room.name)

	def get_item(self, name):
		for idx, item in enumerate(self.contents):
			if name.lower() == item.name.lower():
				return self.contents.pop(idx)
		else:
			return None

class Player:
	def __init__(self, name, location):
		self.name = name
		self.inventory = []
		self.location = location

	def print_inventory(self):
		if len(self.inventory) == 0:
			print("You ain't got shit")
		else:
			print('You have:')
			for item in self.inventory:
				item.print()