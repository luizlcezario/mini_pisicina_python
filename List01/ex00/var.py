def my_var():
    x1 = 42
    x2 = "42"
    x3 = "quarante-deux"
    x4 = 42.0
    x5 = True
    x6 = [42]
    x7 = {42: 42}
    x8 =  (42,)
    x9 = set()
    print(x1, " has a type ", type(x1))
    print(x2, " has a type ", type(x2))
    print(x3, " has a type ", type(x3))
    print(x4, " has a type ", type(x4))
    print(x5, " has a type ", type(x5))
    print(x6, " has a type ", type(x6))
    print(x7, " has a type ", type(x7))
    print(x8, " has a type ", type(x8))
    print(x9, " has a type ", type(x9))




if __name__ == '__main__':
    my_var()