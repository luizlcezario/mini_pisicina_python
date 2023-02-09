import sys

def capital_city(to_verify, states, capital):
    state_s = ""
    city = ""
    for s in states:
        if (str(s).upper() == to_verify):
            city = s
            state_s = states[s]
    if (state_s == ""):
        return (False)
    else:
        print(city,  "is the capital of" , capital[state_s])
    return (True)

def capital_state(to_verify, states, capital):
    city_s = ""
    state = ""
    for s in capital:
        if (str(capital[s]).upper() == to_verify):
            state = capital[s]
            city_s = s
    if (city_s == ""):
        return (False)
    else:
        for i in states:
            if (states[i] == city_s):
                print(i, "is the capital of" , state)
    return (True)


def verify_type(original, to_verify, states, capital):
    test = capital_city(to_verify, states, capital)
    if (test == False):
        test = capital_state(to_verify, states, capital)
    if (test == False):
        print(original ,"is neither a capital city nor a state")

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
    to_verify = sys.argv[1].split(",")
    a = 0
    for i in to_verify:
        a = i.strip().upper()
        if (a != ""):
            verify_type(i.strip(), a, states, capital_cities)



if __name__ == '__main__':
    main()