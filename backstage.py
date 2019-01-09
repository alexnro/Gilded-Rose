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

    stageOne = Backstage("Backstage", 5, 15)
    stageOne.update_quality()
    assert stageOne.getQuality() == 17

    stageBack = Backstage("Backstage", 0, 24)
    stageBack.update_quality()
    assert stageBack.getQuality() == 27

    back = Backstage("Backstage", 3, 49)
    back.update_quality()
    assert back.getQuality() == 50

    backStage = Backstage("backstage", -2, 30)
    backStage.update_quality()
    assert backStage.getQuality() == 0