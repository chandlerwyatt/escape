class InventoryItem:
    def __init__(self, name, description):
        self.name = name
        self.description = description

    def print(self):
        print(self.name + ": " + self.description)

    def print_name(self):
        print(self.name)


LIGHTER = InventoryItem(
    name="lighter",
    description="This is a lighter. It makes things hot af."
)
DAB_RIG = InventoryItem(
    name="dab rig",
    description="This item will make you very high."
)
HUBCAT = InventoryItem(
    name="hubcat",
    description="This little guy is a hubcat. Hello hubcat."
)
MEAT = InventoryItem(
    name="meat",
    description="This is Bowman's meat. Beware."
)
BOWMAN = InventoryItem(
    name="bowman",
    description="This is Bowman.\
        He is a human and needs meat to maintain his loudness."
)
CAMERA = InventoryItem(
    name="camera",
    description="This is a really nice camera. Don't fuck it up."
)
