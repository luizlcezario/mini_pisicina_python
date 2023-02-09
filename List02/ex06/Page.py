from elem import Elem, Text
from elements import *

class Page :
    def __init__(self, element: Elem):
        self.page = element

    def is_valid(self):
        has_title = False
        if not isinstance(self.page, Html): return False
        if not isinstance(self.page.content[0], Head): return False
        if not isinstance(self.page.content[1], Body): return False
        for elem in self.page.content[0].content:
            if has_title == False and isinstance(elem, Title) and len(elem.content) == 1 and isinstance(elem.content[0], Text): has_title = True
            elif not isinstance(elem, Meta ): return False
        for elem in self.page.content[1].content:
            if not isinstance(elem, (H1, H2, Div, Table, Ul, Ol, Span, Text)): return False
            if isinstance(Div, Table, Ul, Ol) and not self.__test_container(elem): return False
            if isinstance(elem, (H1, H2, Li, Th, Td, P)) and not isinstance(elem.content, Text): return False 
        return (True)

    def __str__(self):
        if (self.page.tag == 'html'):
           return "<!DOCTYPE html>\n" + str(self.page)
        else:
            return str(self.page)
    
    def write_to_file(self, name_page):
        fd = open(name_page, "w+")
        if (self.page.tag == 'html'):
            fd.write("<!DOCTYPE html>\n")
            fd.write(str(self.page))
        else:
            fd.write(str(self.page))
        fd.close()

def test():
    test = Page(Html(
        [Head(Title(Text("Hello ground!"))),
        Body([
            H1(Text("Oh no, not again!")),
            Div(
                Img({'src' : 'http://i.imgur.com/pfp3T.jpg'})
            )])
        ]))

    assert test.is_valid() == True
    test = Page(Html(
        [Head(Title(Text("Hello ground!"))),
        Body([
            H1(Text("Oh no, not again!")),
        
                Img({'src' : 'http://i.imgur.com/pfp3T.jpg'})
            ])
        ]))

    assert test.is_valid() == False
    print(test)
    test.write_to_file("index.html")
    
if __name__ == '__main__':
    test()


