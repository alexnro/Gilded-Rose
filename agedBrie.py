from regular_item import RegularItem


class AgedBrie(RegularItem):


    def __init__(self, name, sell_in, quality):
        RegularItem.__init__(self, name, sell_in, quality)


    def update_quality(self):
        if RegularItem.getSellIn(self) > 0:
            self.setQuality(+1)
        else:
            self.setQuality(+2)
        self.setSellIn()


if __name__ == "__main__":
    

    quesito = AgedBrie("Aged Brie", 2, 0)
    assert quesito.getName() == "Aged Brie"
    quesito.update_quality()
    assert quesito.getQuality() == 1

    quesitoSandra = AgedBrie("Sandra", 3, 50)
    quesitoSandra.update_quality()
    assert quesitoSandra.getQuality() == 50

    quesitocoche = AgedBrie("Coche", 2, 0)
    quesitocoche.update_quality()
    assert quesitocoche.getQuality() == 1
    assert quesitocoche.getSellIn() == 1