class Sulfuras():
    
    #Todas las funciones que empiecen por dos guiones bajos son lo que en Java se llama "private class", con la diferencia de que aqui si se puede acceder a ella, es una recomendación que da el programador para que no se ejecute esa fución
    def __init__(self, name, sell_in, quality):
        self.name = name
        self.sell_in = sell_in
        self.quality = quality

    #Reflection, permite que el programa mire la clase y el tipo del objeto
    def update_quality(self): 
        self.quality = 80
        assert self.quality == 80, "Quality de %s no es 80" % self.__class__.__name__
        

    def __repr__(self):
        #Este def es para definir el output del objeto
        return "%s, %s, %s" % (self.name, self.sell_in, self.quality)


if __name__ == '__main__':

    item = Sulfuras("Sulfuras, mano de Maradona", 3, 80)
    print(item)
    # test update_quality
    for dia in range(1, 10):
        item.update_quality()
        print(item)

    # test update_quality incorret input
    item = Sulfuras("Sulfuras, mano de Dios", 3, 10000)
    for dia in range(1, 10):
        item.update_quality()
        print(item)