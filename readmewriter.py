from MDhandler import *

md = Markdown("README.md")

head = Paragraph("Markdownhandler")
head.endl()

codeQuality = Line("codebeat badge")
codeQuality.img_link("https://codebeat.co/badges/ad18ec78-fe15-4b73-a02a-5061b4d87a16")
codeQuality.link_with_context("https://codebeat.co/projects/github-com-dps0340-markdownhandler-master")
codeQuality.endl()
codeQuality.endl()


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

md.append_context([head, l1, codeQuality, l2, l3, l4, copyright().compiledby()])
md.write()
