import  requests, json, sys
import dewiki


def request():
    if len(sys.argv) != 2 : raise Exception("please type what you want to find in wikipedia")
    res = requests.get('http://en.wikipedia.org/w/api.php', params={ 'action': 'opensearch','search': sys.argv[1],'format': 'json'})
    if res.json()[1] != [] :
        title = res.json()[1][0]
    else:
        raise Exception("sorry not found nothing to take a wiki")
    res = requests.get('http://en.wikipedia.org/w/api.php', params={ 'action': 'query','titles': title, 'prop': 'revisions', 'rvprop': 'content', 'rvslots': '*', 'format': 'json'})
    if res.status_code != 200 : raise Exception("Page not found or search misspelled, please try again")
    res_j = json.loads(res.content)
    list_j = res_j['query']['pages']
    page_id = list(list_j.keys())
    if (page_id[0] == '-1'): raise Exception("Page not found or search misspelled, please try again")
    list_j = list_j[page_id[0]]["revisions"]
    final = ""
    for x in list_j:
            final = dewiki.from_string(x['slots']['main']['*'])
    fd = open(sys.argv[1] + ".wiki", "w")
    fd.write(final)

if __name__ == "__main__":
    try:
        request()
    except Exception as e:
        print(e)