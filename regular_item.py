from item import Item
from updateable import Interface


class RegularItem(Item, Interface):


    def __init__(self, name, sell_in, quality):
        
        Item.__init__(self, name, sell_in, quality)
    

    def getName(self):
        return self.name

    
    def getSellIn(self):
        return self.sell_in
    

    def getQuality(self):
        return self.quality


    def setSellIn(self):
        self.sell_in -= 1


    def setQuality(self, valor):
        if self.quality + valor >= 50:
            self.quality = 50
        elif self.quality + valor >= 0:
            self.quality += valor
        elif self.quality + valor < 0:
            self.quality = 0
        


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

    itemSandra = RegularItem("Sandra", 5, 55)
    itemSandra.update_quality()
    assert itemSandra.getQuality() == 50

    itemAlex = RegularItem("Alex", 2, -2)
    itemAlex.update_quality()
    assert itemAlex.getQuality() == 0