import sys
from items import LIGHTER, DAB_RIG, HUBCAT, MEAT, CAMERA
from rooms import BOWMANS_ROOM, TAMIRS_ROOM, BACKYARD


class PlayerFlags(object):

    sam_cam = False


class Player:
    def __init__(self, name, location):
        self.name = name
        self.inventory = {}
        self.location = location
        self.flags = PlayerFlags()

    def help(self):
        print("""
            You can perform the following actions in Escape from the Skank:

            go <direction> : This allows you to move to different areas
            e.g. go east

            get <item_name> : This allows you to take an item
            from a room
            e.g. get hubcat

            use <item_name> : This allows you to use an item in your inventory
            e.g. use meat

            inventory : This prints the contents of your inventory
        """)

    def print_inventory(self):
        if len(self.inventory) == 0:
            print("You ain't got shit\n")
        else:
            print('\n------------------------------')
            print('\nYou have:')
            for item in self.inventory.values():
                item.print()
            print()
            print('------------------------------\n')

    def go(self, destination):
        if destination in self.location.neighbors:
            self.location = self.location.neighbors[destination]
        else:
            print("You can't go there asshole")

    def use_item(self, name):
        item = self.inventory.get(name)
        if item is None:
            print("You don't have a " + name)
            return

        if item == LIGHTER and self.location == BACKYARD:
            dab_rig = self.inventory.get(DAB_RIG.name)
            if dab_rig is None:
                print("What are you lighting?")
                return
            hubcat = self.inventory.get(HUBCAT.name)
            if hubcat is None:
                print("Why are you dabbing by yourself? \
                    Everything OK at home?")
                return
            if self.flags.sam_cam is False:
                print("No one will believe you dabbed \
                    this gloriously without a photo")
                return
            print("You WIN!!!")
            sys.exit(0)
        elif item == MEAT and self.location == BOWMANS_ROOM:
            print("You give the meat to Bowman and he is pleased. \
                His loudness is preserved. He hands you a lighter.")
            self.inventory[LIGHTER.name] = LIGHTER
        elif item == MEAT:
            print("You ate the meat you imbecile! \
                Bowman emerges and eats you.")
            sys.exit(0)
        elif item == HUBCAT and self.location == TAMIRS_ROOM:
            print("Tamir is going to be pissed son.")
            del self.inventory[item.name]
            self.location.contents.append(item)
        elif item == CAMERA and self.location == BACKYARD:
            print("You hand the camera to Sam. He is a fancy boy, \
                and will take a sexy photo of you.")
            del self.inventory[item.name]
            self.flags.sam_cam = True

        else:
            print("You can't use that here.")
