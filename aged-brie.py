from item import Item
from updateable import Interface
from regular_item import RegularItem


class AgedBrie(RegularItem):


    def __init__(self, name, sell_in, quality):
        RegularItem.__init__(self, name, sell_in, quality)
    


if __name__ == "__main__":
    

    quesito = AgedBrie("Aged Brie", 2, 0)
    assert quesito.getName == "Aged Brie"
    quesito.update_quality()
    assert quesito.getQuality == -2