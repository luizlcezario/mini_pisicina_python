from settings import *
import sys, re 

def get_var(var_globals):
    var_dict = {}
    b = False
    for i in var_globals:
        if i == "sys":
            break 
        elif b is True:
            var_dict[i] = var_globals[i] 
        elif i == "__cached__":
            b = True
    return (var_dict)

def sub_template(file, var_globals):
    text = file
    for i in var_globals:
        sub ="({" + i + "})" 
        text = re.sub(sub, var_globals[i], text)
    return text

def main():
    if len(sys.argv) != 2:
        exit()
    try:
        if sys.argv[1].endswith('.template') != True: raise Exception("Error on input extension")
        template = open(sys.argv[1], 'r+')
        var_dict = get_var(globals())
        file = template.read()
        html = open(sys.argv[1].replace(".template", "") + ".html", "w+")
        text = sub_template(file, var_dict)
        html.write(text)
        html.close()
        template.close()
    except Exception as e: 
        print(e)

if __name__ == '__main__':
    main()