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

md.append_context(pr)
md.append_context(l2)

md.write()