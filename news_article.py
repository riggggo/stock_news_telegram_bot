class Article:
    def __init__(self, title, description, source):
        self.title = title
        self.description = description
        self.source = source

    def __str__(self):
        return f"{self.title}\n{self.description}\n(Source: {self.source})"



from io import StringIO
from html.parser import HTMLParser

class MLStripper(HTMLParser): # Class MLStripper from https://stackoverflow.com/questions/753052/strip-html-from-strings-in-python
    def __init__(self):
        super().__init__()
        self.reset()
        self.strict = False
        self.convert_charrefs = True
        self.text = StringIO()

    def handle_data(self, d):
        self.text.write(d)

    def get_data(self):
        return self.text.getvalue()


def strip_tags(html):
    s = MLStripper()
    s.feed(html)
    return s.get_data()
