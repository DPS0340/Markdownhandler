from MDhandler import *

md = Markdown("output.md")

pr = Paragraph("lorem ipsum")
pr.bold()
pr.endl()

l1 = Line("This is Test.")
l1.bold()
l1.endl()
l1.endl()

pr.append_context(l1)

l2 = Line("This is Test - DPS0340")
l2.bold()
l2.bold()
l2.endl()
l2.endl()

l3 = Line("Compiled by ")
l4 = Line("MDhandler")
l4.link("https://github.com/DPS0340/Markdownhandler")

md.append_context(pr)
md.append_context(l2)
md.append_context(l3)
md.append_context(l4)


md.write()