class Item():
    def __init__(self, name, sell_in, quality):
        self.name = name
        self.sell_in = sell_in
        self.quality = quality


    def getName(self):
        return self.name

    
    def getSellIn(self):
        return self.sell_in
    

    def getQuality(self):
        return self.quality


    def __repr__(self):
        return "%s, %s, %s" % (self.name, self.sell_in, self.quality)



if __name__ == '__main__':

    new_item = Item("Alex", "20", "30")

    assert new_item.getName() == 'Alex'
    assert new_item.getSellIn() == '20'
    assert new_item.getQuality() == '30'
    assert new_item.update_quality() == None