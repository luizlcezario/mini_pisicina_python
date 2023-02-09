#!/usr/bin/python3


class Text(str):
    """
    A Text class to represent a text you could use with your HTML elements.

    Because directly using str class was too mainstream.
    """

    def __str__(self):
        """
        Do you really need a comment to understand this method?..
        """
        return super().__str__().replace('<', '&lt;').replace('>', '&gt;').replace('"', '&quot;').replace('\n', '\n<br />\n')


class Elem:
    """
    Elem will permit us to represent our HTML elements.
    """
    indent = 0
    def __init__(self, tag='div', attr={}, content=None, tag_type='double'):
        """
        __init__() method.

        Obviously.
        """
        self.tag = tag
        self.attr = attr
        if self.check_type(content) == False and content != None:
            raise Elem.ValidationError
        elif type(content) is list: self.content = content
        elif content == None : self.content = []
        else : self.content = [content]
        self.tag_type = tag_type

    def __str__(self):
        """
        The __str__() method will permit us to make a plain HTML representation
        of our elements.
        Make sure it renders everything (tag, attributes, embedded
        elements...).
        """
        result = ""
        if self.tag_type == 'double':
            result = "<" + self.tag  + self.__make_attr() + ">" + self.__make_content() + "</" + self.tag + ">"
        elif self.tag_type == 'simple':
            result = "<" + self.tag  + self.__make_attr() + " />"
        return result

    def __make_attr(self):
        """
        Here is a function to render our elements attributes.
        """
        result = ''
        for pair in sorted(self.attr.items()):
            result += ' ' + str(pair[0]) + '="' + str(pair[1]) + '"'
        return result

    def __make_content(self):
        """
        Here is a method to render the content, including embedded elements.
        """

        if len(self.content) == 0:
            return ''
        result = ''
        for elem in self.content:
            if type(elem) is Text and elem == "": continue
            result = result.strip(' ')
            if not result.endswith('\n'): result += '\n'
            elem.indent = self.indent + 1
            for i in range(0, elem.indent ):
                result += '  ' 
            tmp = str(elem)
            if type(elem) is Text: tmp = tmp.replace( '&lt;', '<').replace('&gt;', '>').replace('&quot;', '"')
            result += tmp
            if not result.endswith('\n'):
                result += '\n'
                for i in range(0, self.indent):
                    result += '  ' 
        return result

    def add_content(self, content):
        if not Elem.check_type(content):
            raise Elem.ValidationError
        if type(content) == list:
            self.content += [elem for elem in content if elem != Text('')]
        elif content != Text(''):
            self.content.append(content)

    @staticmethod
    def check_type(content):
        """
        Is this object a HTML-compatible Text instance or a Elem, or even a
        list of both?
        """
        return (isinstance(content, Elem) or type(content) == Text or
                (type(content) == list and all([type(elem) == Text or
                                                isinstance(elem, Elem)
                                                for elem in content])))
    class ValidationError(Exception):
        def __init__(self):
            return None

def page():
    html = Elem(tag="html", content=Elem(tag="head" , content=Elem(tag="title", content=Text("\"Hello ground!\""))))
    body = Elem(tag="body", content=Elem(tag="h1", content=[Text("\"Oh no, not again!\""), Elem(tag="img", tag_type="simple", attr={'src' : 'http://i.imgur.com/pfp3T.jpg'})]))
    html.add_content(body)
    print(str(html))

if __name__ == '__main__':
    page()
