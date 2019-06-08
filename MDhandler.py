# DO NOT REMOVE THIS THREE COMMENTS! #
# Original repository: https://github.com/DPS0340/Markdownhandler.py #
# MIT License #

class Markdown:
    def __init__(self, filename=""):
        self.filename = filename
        self.context = []
    def append_context(self, obj):
        self.context.append(obj)
    def write(self):
        result = ""
        for obj in self.context:
            result += obj.eval()
        with open(file=self.filename, mode="w") as w:
            w.write(result)
        return result

class Attribute:
    def __init__(self, context="", left=False, right=False):
        self.context = context
        self.left = left
        self.right = right

class Parser:
    def __init__(self):
        self.attributes = []
    def process(self, context):
        str = context
        for attr in self.attributes:
            if attr.left:
                str = self.parse(attr) + str
            if attr.right:
                str = str + self.parse(attr)
        return str
    def parse(self, attribute):
        if attribute.context == "bold":
            return "**"
        elif attribute.context == "endl":
            return "\n"
        elif attribute.context == "para":
            return "#"
        elif attribute.context == "blank":
            return " "
        else:
            return ""
    def bold(self):
        self.attributes.append(Attribute("bold", True, True))
    def endl(self):
        self.attributes.append(Attribute("endl", False, True))
    def para(self):
        self.attributes.append(Attribute("para", True, False))
    def leftBlank(self):
        self.attributes.append(Attribute("blank", True, False))
    def rightBlank(self):
        self.attributes.append(Attribute("blank", False, True))

class Paragraph(Parser):
    def __init__(self, head="", context=[]):
        super().__init__()
        self.head = head
        self.context = context
    def edithead(self, head):
        self.head = head
    def addhead(self, appendstr):
        self.head += appendstr
    def append_context(self, line):
        self.context.append(line)
    def eval(self):
        self.leftBlank()
        self.para()
        result = ""
        result += self.process(self.head)
        for line in self.context:
            result += line.eval()
        return result
class Line(Parser):
    def __init__(self, context=""):
        super().__init__()
        self.context = context
    def editcontext(self, context):
        self.context = context
    def addhead(self, appendstr):
        self.context += appendstr
    def link(self, url):
        self.context = "[" + self.context + "]" + "(" + url + ")"
    def eval(self):
        return self.process(self.context)