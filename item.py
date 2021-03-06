class Item():


    def __init__(self, name, sell_in, quality):
        self.name = name
        self.sell_in = sell_in
        self.quality = quality


    def __repr__(self):
        return "%s, %s, %s" % (self.name, self.sell_in, self.quality)



if __name__ == '__main__':


    new_item = Item("Alex", "20", "30")

    assert new_item.getName() == 'Alex'
    assert new_item.getSellIn() == '20'
    assert new_item.getQuality() == '30'