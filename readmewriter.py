from MDhandler import *

md = Markdown("README.md")

head = Paragraph("Markdownhandler")
head.endl()

hr = Line()
hr.horizonalLine()

l1 = Line("Object oriented markdown writing library - Python Based")
l1.bold()
l1.endl()
l1.endl()

l2 = Line("This means can convert python script using this library to markdown document, not means compile markdown to html.")
l2.endl()
l2.endl()

l3 = Line("Work in Progress - Anyone can commit!")
l3.endl()
l3.endl()

l4 = Line("TODO")
l4.link_with_context("https://github.com/DPS0340/Markdownhandler/blob/master/TODO.md")
l4.endl()
l4.endl()


l5 = Line("LICENSE:")
l5.link_with_context("https://github.com/DPS0340/Markdownhandler/blob/master/TODO.md")
l6 = Line(" MIT")
l6.endl()
l6.endl()

md.append_context([head, l1, l2, l3, l4, l5, l6, copyright().compiledby()])
md.write()
print(head is copyright().compiledby())