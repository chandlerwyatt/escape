# setup the game world
from sys import exit
from .player import Player
from .rooms import LIVING_ROOM


class GameFlags(object):

    # is Sam in the backyard?
    sam_backyard = False
    # has the player given the camera to Sam?
    sam_cam = False


class Game(object):

    def __init__(self):
        self.flags = GameFlags()

    def run(self):
        player = Player(name='chandler', location=LIVING_ROOM,
                        flags=self.flags)

        while True:
            player.location.print_description(self.flags)
            print("")
            player.location.print_contents()
            print("")
            player.location.print_neighbors()
            print("")

            raw = input("Whatchu wanna do? ")
            raw = raw.split(" ")
            action = raw[0]
            if action.lower() == "go":
                player.go(raw[1])
            elif action.lower() == "get":
                item_name = " ".join(raw[1:])
                item = player.location.get_item(item_name)
                if item is not None:
                    player.inventory[item.name] = item
                else:
                    print("I don't see that")
            elif action.lower() == "inventory":
                player.print_inventory()
            elif action.lower() == "use":
                item_name = " ".join(raw[1:])
                player.use_item(item_name)
            elif action.lower() == "help":
                player.help()
            elif action.lower() == "speak":
                player.speak()
            elif action.lower() == "quit":
                exit()
