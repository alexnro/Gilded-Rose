from regular_item import RegularItem


class Sulfuras(RegularItem):

    
    def setSellIn(self):
        pass


    def setQuality(self):
        pass


    def update_quality(self):
        self.setSellIn()
    


if __name__ == "__main__":

    sulfuro = Sulfuras("sulfuras", 0, 80)
    sulfuro.update_quality()
    assert sulfuro.getSellIn() == 0
    assert sulfuro.getQuality() == 80

    sulfurasTest = Sulfuras("Sulfuras", -1, 80)
    sulfurasTest.update_quality()
    assert sulfurasTest.getQuality() == 80
    assert sulfurasTest.getSellIn() == -1