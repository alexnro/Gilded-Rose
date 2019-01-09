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
    

    cheese = AgedBrie("Aged Brie", 2, 0)
    assert cheese.getName() == "Aged Brie"
    cheese.update_quality()
    assert cheese.getQuality() == 1

    cheeseTwo = AgedBrie("Sandra", 3, 50)
    cheeseTwo.update_quality()
    assert cheeseTwo.getQuality() == 50

    cheeseThree = AgedBrie("Coche", 2, 0)
    cheeseThree.update_quality()
    assert cheeseThree.getQuality() == 1
    assert cheeseThree.getSellIn() == 1

    cheeseFour = AgedBrie("Portatil", 1, 1)
    cheeseFour.update_quality()
    assert cheeseFour.getQuality() == 2
    assert cheeseFour.getSellIn() == 0

    cheeseFive = AgedBrie("Raton", 0, 2)
    cheeseFive.update_quality()
    assert cheeseFive.getQuality() == 4
    assert cheeseFive.getSellIn() == -1
