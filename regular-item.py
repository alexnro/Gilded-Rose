from item import Item
from updateable import Interface


class RegularItem(Item, Interface):


    def __init__(self, name, sell_in, quality):
        
        Item.__init__(self, name, sell_in, quality)
    

    def setSellIn(self):
        self.sell_in -= 1

    def setQuality(self, valor):
        pass


    def update_quality(self):
        if self.sell_in > 0:
            self.quality -= 1
        else:
            self.quality -= 2
        self.setSellIn()






if __name__ == "__main__":
    

    itemSama = RegularItem("Pepe", 10, 5)
    itemSama.update_quality()
    assert itemSama.getQuality() == 4
    assert itemSama.getSellIn() == 9