from markdownCreation import *
from markdown import markdown

newMD = MarkdownFile()
newMD.add(Header("Hey", 1))
newMD.add(Header("I'm just testing the module", 3))
newMD.add(Definition("This is a text", ["This is his first definition", "This is his second definition"]))
newMD.add(Quote("Anime no Sekai - 2020"))
newMD.add(Separator())
newMD.add(List(["Testing the list", "second element"]))
newMD.add(OrderedList(["Testing the list", "second element"]))
newMD.add(str(Paragraph("Hey how are you all\nI'm testing this feature with ")) + str(InlineCode("Python")))
codeVar = """
{
    "hey": "wow"
}
"""
newMD.add(CodeBlock(codeVar, "json"))
newMD.add(Paragraph("Let me link you something" + Footnote("wow little footnote you didn't see it coming", newMD) + "real quick"))
newMD.add(Link("https://animenosekai.herokuapp.com/status", "My server status page"))
newMD.add(Paragraph("I will test Strikethrough text too like " + Strikethrough("this one")))
newMD.add(BoldText("Now I'm gonna add a text in " + str(ItalicText("italic"))))

newMD.add(Table(["Key", "Value", "wow", 'ahoy'], [["Hey", "Hqdjsqkdhqskjdheyo", "weeeee", 'ahoy'], ["yeHhjsdgfjhdsfjhdgf", "oyeH", 'reeeeee', 'ahoy'], ["kjzehkjhe", "yohooo", "ahooyyyy", 'ahoy'], ['ahoy']*4], ["left", "center", "right", "center"]))

print(newMD.html("Hey", False, False, "output.html"))
print(newMD)
newMD.save("newMD.md")