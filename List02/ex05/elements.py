from elem import Elem, Text 

class Html(Elem):
    def __init__(self, __ = None, attr = {}):
        super().__init__(tag='html', content=__, attr=attr0)

class Head(Elem):
    def __init__(self, __ = None, attr = {}):
        super().__init__(tag='head', content=__, attr=attr)

class Body(Elem):0
    def __init__(self, __ = None,  attr = {}):
        super().__init__(tag='body', content=__, attr=attr)

class Title(Elem):
    def __init__(self, __ = None,  attr = {}):
        super().__init__(tag='title', content=__, attr=attr)

class Meta(Elem):
    def __init__(self, __ = None,  attr = {}):
                super().__init__(tag='meta', attr=attr, tag_type='simple')

class Img(Elem):
    def __init__(self, attr = {}):
        super().__init__(tag='img', attr=attr, tag_type='simple')

class Table(Elem):
   def __init__(self, __ = None,  attr = {}):
        super().__init__(tag='table', content=__, attr=attr)

class Td(Elem):
   def __init__(self, __ = None,  attr = {}):
        super().__init__(tag='td', content=__, attr=attr)

class Th(Elem):
   def __init__(self, __ = None,  attr = {}):
        super().__init__(tag='th', content=__, attr=attr)

class Tr(Elem):
   def __init__(self, __ = None,  attr = {}):
        super().__init__(tag='tr', content=__, attr=attr)

class Ol(Elem):
   def __init__(self, __ = None,  attr = {}):
        super().__init__(tag='ol', content=__, attr=attr)

class Ul(Elem):
   def __init__(self, __ = None,  attr = {}):
        super().__init__(tag='ul', content=__, attr=attr)

class Li(Elem):
   def __init__(self, __ = None,  attr = {}):
        super().__init__(tag='li', content=__, attr=attr)
class H1(Elem):
   def __init__(self, __ = None,  attr = {}):
        super().__init__(tag='h1', content=__, attr=attr)
class H2(Elem):
   def __init__(self, __ = None,  attr = {}):
        super().__init__(tag='h2', content=__, attr=attr)
class P(Elem):
   def __init__(self, __ = None,  attr = {}):
        super().__init__(tag='p', content=__, attr=attr)
class Div(Elem):
   def __init__(self, __ = None,  attr = {}):
        super().__init__(content=__, attr=attr)
class Hr(Elem):
   def __init__(self, attr = {}):
        super().__init__(tag='hr', attr=attr,  tag_type='simple')
class Span(Elem):
   def __init__(self, __ = None,  attr = {}):
        super().__init__(tag='span', content=__, attr=attr)
class Br(Elem):
   def __init__(self, __ = None,  attr = {}):
        super().__init__(tag='br', attr=attr, tag_type='simple')
    




def test():
    print(Html(
        [Head(Title(Text("Hello ground!"))),
        Body([
            H1(Text("Oh no, not again!")),
            Img({'src' : 'http://i.imgur.com/pfp3T.jpg'})
            ])
        ]))
    # print( Html([Head(), Body()], attr={'class': 'test'}))

if __name__ == '__main__':
    test()