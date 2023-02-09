def var_to_dict(d):
    total  = {}
    for i in d:
        if i[1] in total:
            total[i[1]] = sorted([total[i[1]] ,i[0]])
        else:
            total[i[1]] = i[0]
    return total



def order(d):
    year = []
    names = []
    inverted_d = var_to_dict(d.items())
    for a in inverted_d:
        year.append(a)
    year_ord = sorted(year)
    for a in range(len(year_ord)):
        if type(inverted_d[year_ord[a]]) is list:
            for i in inverted_d[year_ord[a]]:
                names.append(i)
        else:
            names.append(inverted_d[year_ord[a]])
    return (names)
        


def main():
    d = {
    'Hendrix' : '1942',
    'Allman' : '1946',
    'King' : '1925',
    'Clapton' : '1945',
    'Johnson' : '1911',
    'Berry' : '1926',
    'Vaughan' : '1954',
    'Cooder' : '1947',
    'Page' : '1944',
    'Richards' : '1943',
    'Hammett' : '1962',
    'Cobain' : '1967',
    'Garcia' : '1942',
    'Beck' : '1944',
    'Santana' : '1947',
    'Ramone' : '1948',
    'White' : '1975',
    'Frusciante': '1970',
    'Thompson' : '1949',
    'Burton' : '1939',
    }
    orded = order(d)
    for i in range(len(orded)):
        print(orded[i])

if __name__ == '__main__':
    main()