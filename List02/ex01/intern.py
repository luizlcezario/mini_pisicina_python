class Intern:
    def __init__(self, n =  "My name? I’m nobody, an intern, I have no name." ):
        self.name = n
        pass
    def __str__(self):
        return self.name 
    class Coffee:
        def __str__(self) -> None:
            return "This is the worst coffee you ever tasted."
    def work(self):
        raise Exception("I’m just an intern, I can’t do that...")
    def make_coffee(self):
        return self.Coffee()


def test_class():
    intern1 = Intern()
    intern2 = Intern('Mark')
    print(str(intern1))
    print(str(intern2))
    coffee = intern2.make_coffee()
    print(str(coffee))
    try:
        intern1.work()
    except:
        print("Error: intern not work")


if __name__ == '__main__':
    test_class()