from markdownCreation import *

newMD = MarkdownFile()
newMD.add(Header("Hey", 1, newMD))
newMD.add(Header("This is a test for markdown-creation", 2, newMD))
newMD.add(TableOfContent(newMD, 5))
newMD.add(Paragraph(f"I hope that it will work {str(ItalicText('properly'))}"))
newMD.add(Separator())
newMD.add(Header("What am I going to do?", 1, newMD))
newMD.add(Paragraph("Well for example I could put a " + Link("https://animenosekai.herokuapp.com/status", BoldText("link")) + Footnote("I don't know if it will work", newMD)))
newMD.add(Paragraph(f"This is an inline code: {str(InlineCode('pip install markdown-creation'))}"))
code = """
{
    "key": "value",
    "details": "this is a test of the code block"
}
"""
newMD.add(Header("Let me test code blocks", 2, newMD))
newMD.add(CodeBlock(code, "JSON"))
newMD.add(Paragraph("I think that I will print out the table of content with newMD.tableOfContent(2)"))
newMD.add(Paragraph("And I'll maybe try to output an html file"))
newMD.add(Header("I'm running out of idea to write", 5, newMD))
newMD.add(Quote("Anime no Sekai - 2020"))
newMD.html(minify=True, destination="minified.html")
newMD.html(destination="output.html")
newMD.html(onlyMarkdown=True, destination="onlyMarkdown.html")
newMD.save("newMD.md")