import sys

def capital_city(to_verify, states, capital):
    state_s = ""
    for s in states:
        if (s == to_verify):
            state_s = states[s]
    if (state_s == ""):
        return (False)
    else:
        print(capital[state_s])
    return (True)

def capital_state(to_verify, states, capital):
    city_s = ""
    for s in capital:
        if (capital[s] == to_verify):
            city_s = s
    if (city_s == ""):
        return (False)
    else:
        for i in states:
            if (states[i] == city_s):
                print(i)
    return (True)


def verify_type(to_verify, states, capital):
    test = capital_city(to_verify, states, capital)
    if (test == False):
        test = capital_state(to_verify, states, capital)
    if (test == False):
        print("Unknow Capital City")

def main():
    states = {
    "Oregon" : "OR",
    "Alabama" : "AL",
    "New Jersey": "NJ",
    "Colorado" : "CO"
    }
    capital_cities = {
    "OR": "Salem",
    "AL": "Montgomery",
    "NJ": "Trenton",
    "CO": "Denver"
    }
    if (len(sys.argv) != 2):
        return ()
    else:
        to_verify = sys.argv[1]
        verify_type(to_verify, states, capital_cities)



if __name__ == '__main__':
    main()