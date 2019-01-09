from item import Item
from updateable import Interface


class RegularItem(Item, Interface):


    def __init__(self, name, sell_in, quality):
        
        Item.__init__(self, name, sell_in, quality)
    

    def setSellIn(self):
        self.sell_in -= 1


    def setQuality(self, valor):
        if self.quality + valor >= 0:
            self.quality += valor
        elif self.quality + valor < 0:
            self.quality = 0
        elif self.quality > 50:
            self.quality = 50


    def update_quality(self):
        if self.sell_in > 0:
            self.setQuality(-1)
        else:
            self.setQuality(-2)
        self.setSellIn()






if __name__ == "__main__":
    

    itemSama = RegularItem("Pepe", 10, 5)
    itemSama.update_quality()
    assert itemSama.getQuality() == 4
    assert itemSama.getSellIn() == 9