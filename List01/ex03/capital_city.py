import sys

def capital_city():
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
    state = sys.argv[1]
    state_s = ""
    for s in states:
        if (s == state):
            state_s = states[s]
    if (state_s == ""):
        print("Unknown state")
    else:
        print(capital_cities[state_s])
            


if __name__ == '__main__':
    capital_city()