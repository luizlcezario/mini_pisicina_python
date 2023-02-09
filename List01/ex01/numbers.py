def my_number():
    f = open("./numbers.txt", "r")
    str = f.read().split(",")
    for i in str:
        print(i)



if __name__ == '__main__':
    my_number()