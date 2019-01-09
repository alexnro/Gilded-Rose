from regular_item import RegularItem 


class Backstage(RegularItem):


    def update_quality(self):
        if self.sell_in >= 10:
            self.setQuality(+1)
        elif self.sell_in >= 5:
            self.setQuality(+2)
        elif self.sell_in >= 0:
            self.setQuality(+3)
        else:
            self.quality = 0
        self.setSellIn()




if __name__ == "__main__":
    

    backItem = Backstage("Backstage", 12, 23)
    backItem.update_quality() 
    assert backItem.getQuality() == 24

    stage1 = Backstage("Backstage", 5, 15)
    stage1.update_quality()
    assert stage1.getQuality() == 17

    stageBack = Backstage("Backstage", 0, 24)
    stageBack.update_quality()
    assert stageBack.getQuality() == 27

    backsito = Backstage("Backstage", 3, 49)
    backsito.update_quality()
    assert backsito.getQuality() == 50

    backson = Backstage("backstage", -2, 30)
    backson.update_quality()
    assert backson.getQuality() == 0