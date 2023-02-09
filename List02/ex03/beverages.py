class HotBeverage:
    price = 0.30
    name = "hot beverage"
    def description(self):
        return "Just some hot water in a cup."
    def __str__(self):
        return "'name' : " + str(self.name) +"\n'price' : " + "{:0.2f}".format(self.price) + "\n'description' : """ + self.description()

class Coffee(HotBeverage):
    price = 0.40
    name = "coffee"
    def description(self):
        return "A coffee, to stay awake."

class Tea(HotBeverage):
    price = 0.30
    name = "tea"
    def description(self):
        return "Just some hot water in a cup."

class Chocolate(HotBeverage):
    price = 0.50
    name = "chocolate"
    def description(self):
        return "Chocolate, sweet chocolate..."
    
class Cappuccino(HotBeverage):
    price = 0.45
    name = "cappuccino"
    def description(self):
        return "Un po' di Italia nella sua tazza!"

def test_class():
    hotbeverage = HotBeverage()
    coffee = Coffee()
    tea = Tea()
    chocolate = Chocolate()
    cappuccino = Cappuccino()
    print(str(hotbeverage))
    print(str(coffee))
    print(str(tea))
    print(str(chocolate))
    print(str(cappuccino))



if __name__ == '__main__':
    test_class()