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

    quesitoCoche = AgedBrie("Coche", 2, 0)
    quesitoCoche.update_quality()
    assert quesitoCoche.getQuality() == 1
    assert quesitoCoche.getSellIn() == 1

    quesitoPortatil = AgedBrie("Portatil", 1, 1)
    quesitoPortatil.update_quality()
    assert quesitoPortatil.getQuality() == 2
    assert quesitoPortatil.getSellIn() == 0

    quesitoRaton = AgedBrie("Raton", 0, 2)
    quesitoRaton.update_quality()
    assert quesitoRaton.getQuality() == 4
    assert quesitoRaton.getSellIn() == -1
