import sys

class InventoryItem:
	def __init__(self, name, description):
		self.name = name
		self.description = description

	def print(self):
		print(self.name + ": " + self.description)

	def print_name(self):
		print(self.name)

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
				print("")

	def get_item(self, name):
		for idx, item in enumerate(self.inventory):
			if name.lower() == item.name.lower():
				return self.inventory.pop(idx)
		else:
			return None

	def use_item(self, name):
		item = self.get_item(name)
		if item is None:
			print("You don't have a " + name)
			return

		if item.name.lower() == 'lighter' and self.location.name.lower() == "chandler's room":
			dab_rig = self.get_item("dab rig")
			if dab_rig is None:
				print("What are you lighting?")
				self.inventory.append(item)
				return
			hubcat = self.get_item("hubcat")
			if hubcat is None:
				print("Why are you dabbing by yourself? Everything OK at home?")
				self.inventory.extend([item, dab_rig])
				return
			print("You WIN!!!")
			sys.exit(0)
		elif item.name.lower() == 'meat' and self.location.name.lower() == "bowman's room":
			print("You give the meat to Bowman and he is pleased. His loudness is preserved. He hands you a lighter.")
			from items import LIGHTER
			self.inventory.append(LIGHTER)
		elif item.name.lower() == 'meat':
			print("You ate the meat you imbecile! Bowman emerges and eats you.")
			sys.exit(0)
		elif item.name.lower() == 'hubcat' and self.location.name.lower() == "tamir's room":
			print("Tamir is going to be pissed son.")
			self.get_item(item.name.lower())
			self.location.contents.append(item)

		else:
			print("You can't use that here.")
			self.inventory.append(item)