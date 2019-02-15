# setup the game world
from player import Player
from rooms import LIVING_ROOM


def run_game():
    player = Player(name='chandler', location=LIVING_ROOM)

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


run_game()
