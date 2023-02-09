import sys
import requests
from bs4 import BeautifulSoup


def check(tag : BeautifulSoup):
    res_ul = tag.name == 'ul'
    res_p =  tag.name == 'p'    
    return res_ul or res_p

def verify_loop(lists : list, treat):
    if len(lists) != 0:
        for e in lists:
            if treat == e:
                return True
    return False

def call_api(count, url, lists : list):
    if (url == None or url == "/wiki/Wikipedia:About"):
        raise Exception("Not find any link in de contet of this wiki")
    treat = url.replace(" ", "_").replace("/wiki/", "").strip("/")
    print(count, "roads from", treat, "to philoshophy")
    if (treat == "Philosophy"):
        return (count)
    if (verify_loop(lists, treat)):
        raise Exception(f"{count} infinite loop, please try again!")
    lists.append(treat)
    res = requests.get('https://en.wikipedia.org/wiki/' + treat)
    test = BeautifulSoup(res.content, "html.parser").select_one('#bodyContent')
    for table in test.select('table'):
        table.clear()
    tag = test.find_all_next(check)
    for elem in tag:
        for span in elem.find_all('span'):
            span.clear()
        for sup in elem.find_all('sup'):
            sup.clear()
        if (elem.find('a')):
            for a in  elem.find_all_next('a'):
                if(a['href'].startswith('/wiki/')):
                    return (call_api(count + 1, str(a["href"]), lists))
    


def main():
    try:
        if len(sys.argv) != 2 : raise Exception("please type what you want to find in wikipedia")
        lists = []
        count = call_api(1, sys.argv[1], lists)
        print(count," roads from", lists[0], "to philosophy !")
    except Exception as e :
        print(e)

if __name__ == "__main__":
    main()
