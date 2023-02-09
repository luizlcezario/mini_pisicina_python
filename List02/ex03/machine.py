from beverages import *
import random
class CoffeMachine:
    broken = 10
    def __init__(self) -> None:
        pass
    class EmptyCup(HotBeverage):
        price = 0.90
        name = "empty cup"
        def description(self):
            return "An empty cup?! Gimme my money back!"
    class BrokenMachineException(Exception):
        def __init__(self):
            super().__init__("This coffee machine has to be repaired.")
    def repair(self):
        self.broken = 10
    def serve(self, cup : HotBeverage):
        if (self.broken == 0):
            raise self.BrokenMachineException()
        else:
            i = random.randint(0, 1)
            self.broken -= 1 
            if (i == 0):
                return (self.EmptyCup())
            elif (i == 1):
                return(cup)
        

def test_machine():
    newmachine = CoffeMachine()
    hot = HotBeverage()
    cho = Chocolate()
    tea = Tea()
    cap = Cappuccino()
    cof = Coffee()
    
    for i in range(4):
        try:
            print(i, str(newmachine.serve(hot)))
            print(i, str(newmachine.serve(cho)))
            print(i, str(newmachine.serve(tea)))
            print(i, str(newmachine.serve(cap)))
            print(i, str(newmachine.serve(cof)))
        except :
            print(newmachine.BrokenMachineException().message)
            print("When the coffee machine serve the", i, "they broke")
            newmachine.repair()


if __name__ == '__main__':
    test_machine()
            