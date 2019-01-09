from agedBrie import AgedBrie
from sulfuras import Sulfuras 
from backstage import Backstage 


class GildedRose():


    def __init__(self, stock):
        self.stock = stock

    
    def getStock(self):
        return self.stock

    
    def actualizarStock(self):
        for item in self.stock:
            item.update_quality()
        


if __name__ == "__main__":

    stock = [AgedBrie("Aged Brie", 2, 0), Sulfuras("Sulfuras", 0, 80), Backstage("Backstage", 12, 23)]

    tienda = GildedRose(stock)
    tienda.actualizarStock()
    assert tienda.getStock()[0].getQuality() == 1
    assert tienda.getStock()[1].getName() == "Sulfuras"
    assert tienda.getStock()[2].getSellIn() == 11
    assert tienda.getStock()[1].getSellIn() == 0
    assert tienda.getStock()[2].getQuality() == 24
