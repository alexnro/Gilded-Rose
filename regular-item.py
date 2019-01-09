from item import Item
from updateable import Interface


class RegularItem(Item, Interface):


    def __init__(self, name, sell_in, quality):
        
        Item.__init__(self, name, sell_in, quality)
    







if __name__ == "__main__":
    

    item-sama = RegularItem("Pepe", 10, 5)
    item-sama.setQuality()
    item-sama.update-quality()
    item-sama.getQuality()