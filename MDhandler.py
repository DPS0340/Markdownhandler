# DO NOT REMOVE THIS THREE COMMENTS! #
# Original repository: https://github.com/DPS0340/Markdownhandler.py #
# MIT License #

class Markdown:
    def __init__(self, filename=""):
        self.filename = filename
        self.context = []
    def append_context(self, args):
        for obj in args:
            self.context.append(obj)
    def write(self):
        result = ""
        for obj in self.context:
            if isinstance(obj, tuple) or isinstance(obj, list):
                for elem in obj:
                    result += elem.eval()
            else:
                result += obj.eval()
        with open(file=self.filename, mode="w") as w:
            w.write(result)
        return result

class Attribute:
    def __init__(self, context="", left=False, right=False, lazy=False):
        self.context = context
        self.left = left
        self.right = right
        self.lazy = lazy

class Parser:
    def __init__(self):
        self.attributes = []
    def process(self, context):
        str = context
        lazies = []
        for attr in self.attributes:
            if attr.lazy:
                lazies.append(attr)
                continue
            str = self.parse(str, attr)
        for lazyattr in lazies:
            str = self.parse(str, lazyattr)
        return str
    def parse(self, str, attr):
        if attr.left:
            str = attr.context + str
        if attr.right:
            str = str + attr.context
        return str
    def bold(self):
        self.attributes.append(Attribute("**", True, True, True))
    def endl(self):
        self.attributes.append(Attribute("\n", False, True, True))
    def para(self):
        self.attributes.append(Attribute("#", True, False, True))
    def leftBlank(self):
        self.attributes.append(Attribute(" ", True, False))
    def rightBlank(self):
        self.attributes.append(Attribute(" ", False, True))
    def strike(self):
        self.attributes.append(Attribute("~~", True, True, True))
    def horizonalLine(self):
        self.attributes.append(Attribute("***", False, True))
    def link_with_context(self, url):
        self.attributes.append(Attribute("[", True, False, True))
        self.attributes.append(Attribute("]", False, True, True))
        self.attributes.append(Attribute("(%s)" % url, False, True, True))
    def img_link(self, url):
        self.attributes.append(Attribute("![", True, False, True))
        self.attributes.append(Attribute("]", False, True, True))
        self.attributes.append(Attribute("(%s)" % url, False, True, True))
    def linkSelf(self):
        self.attributes.append(Attribute("<", True, False))
        self.attributes.append(Attribute(">", False, True))
    def italic(self):
        self.attributes.append(Attribute("*", True, True, True))
    def blockQoute(self):
        self.attributes.append(Attribute("> ", True, False, True))


class Line(Parser):
    def __init__(self, context=""):
        super().__init__()
        self.context = context
    def editcontext(self, context):
        self.context = context
    def addhead(self, appendstr):
        self.context += appendstr
    def eval(self):
        return self.process(self.context)

class Paragraph(Line):
    def __init__(self, context=""):
        super().__init__()
        self.context = context
        self.leftBlank()
        self.para()


class copyright:
    def compiledby(self):
        hr = Line("")
        hr.horizonalLine()
        hr.endl()
        tail = Line("Compiled by ")
        taillink = Line("MDHandler")
        taillink.link_with_context("https://github.com/DPS0340/Markdownhandler")
        return hr, tail, taillink
