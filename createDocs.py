print("Generating the README...")

from markdownCreation import *

README = MarkdownFile()

#Title
README.add(Header("markdown-creation", 1, README))
README.add(Quote("A markdown file creation module for Python!"))
#Table of Content
README.add(Header("Table of Content", 1, README))
README.add(TableOfContent(README, 2))
#Description
README.add(Header("What is markdown-creation?", 1, README))
README.add(Paragraph(f"markdown-creation is a Python Module which lets you write Markdown Files ({InlineCode('.md')} files like {InlineCode('README.md')})"))
README.add(Paragraph("Especially useful when it comes down to creating your documentations programmatically (writing scripts to automate things) or rendering files for web servers, it can do many things!"))
README.add(Header("Features", 2, README))
README.add(List(["Markdown File Creation", "Automatic Table of Content creation", "Table creation", "HTML output (normal or minified)", "Less syntax errors", "Easy to use"]))
#HowToUse
README.add(Header("How to use?", 1, README))
README.add(Header("Here is a list of all the objects which comes with markdown-creation", 3, README))
objects = {
    "MarkdownFile": {
        "description": "This object initializes a new markdown file",
        "usage": f"You need to initialize a markdown file to put content in it. To initialize a new markdown file, just call it in a variable {InlineCode('myAwesomeFile = MarkdownFile()')}",
        "functions": Table(
            ["Functions", "Description", "Arguments", "Returned Value"], [
                [InlineCode("add()"), InlineCode("save()"), InlineCode("tableOfContent()"), InlineCode("render()"), InlineCode("html()")],
                ["Adds a line to the markdown file", "Saves the markdown file to the given location", "Returns a string representing the table of content at the current state (yeah I can't predict what you're going to put inside your file)", "Renders the whole file into a string", "Renders the file as an HTML file and gives back a string (and outputs it if you set the destination argument)"],
                ["object: What you want to add (it could be multiple objects but inside of an object, a string)", "destination: The destination of the file; appendToExistingFile: Wether or not you want to override (False) or append (True) if the file is already existing", "level: The maximum header level you want to add", "No argument", "title: Set this if you want to override the HTML title tag (by default it takes the first header content); onlyMarkdown: If you don't want a whole HTML file but only the HTML representation of your markdown file; minify: If you want to minify the HTML; destination: Set this argument if you want to output your HTML file"],
                ["Nothing", "Nothing", "A string with the table of content", "A string with the markdown file", "A string with the HTML file"]
            ],
            "center"
        ),
        "arguments": None
    },
    "Header": {
        "description": "This object returns a markdown header (# content) and adds a header to the index of headers of the provided markdown file",
        "usage": f"Call {InlineCode('Header()')} with the needed argument",
        "functions": None,
        "arguments": Table(
            ["Argument", "Description"],
            [ ["text", "level", "markdownObj"], ["The content of the header", "The level of the header (how many #)", "The MarkdownFile() object you want to add the header (used to make the Table of Content)"] ],
            "center"
        )
    },
    "Quote": {
        "description": "This object returns a markdown quotation text (> content)",
        "usage": f"Call {InlineCode('Quote()')} with the needed argument",
        "functions": None,
        "arguments": Table(
            ["Argument", "Description"],
            [ ["text", "level"], ["The content of the quote", "The level of the quotation (how many >)"] ],
            "center"
        )
    },
    "OrderedList": {
        "description": "This object returns a markdown ordered list (\n1. content\n2. content)",
        "usage": f"Call {InlineCode('OrderedList()')} with the needed argument",
        "functions": None,
        "arguments": Table(
            ["Argument", "Description"],
            [ ["inputList", ""], ["The list to turn into a markdown ordered list", ""] ],
            "center"
        )
    },
    "List": {
        "description": "This object returns a markdown list (\n- content\n- content)",
        "usage": f"Call {InlineCode('List()')} with the needed argument",
        "functions": None,
        "arguments": Table(
            ["Argument", "Description"],
            [ ["inputList"], ["The list to turn into a markdown unordered list"] ],
            "center"
        )
    },
    "InlineCode": {
        "description": "This object returns a markdown inline code string (`code content`)",
        "usage": f"Call {InlineCode('InlineCode()')} with the needed argument",
        "functions": None,
        "arguments": Table(
            ["Argument", "Description"],
            [ ["code"], ["The content of the inline code"] ],
            "center"
        )
    },
    "BlockCode": {
        "description": "This object returns a markdown code block (\n```\ncode\n```\n)",
        "usage": f"Call {InlineCode('CodeBlock()')} with the needed argument",
        "functions": None,
        "arguments": Table(
            ["Argument", "Description"],
            [ ["code", "language"], ["The content of the block code", "(optional) The language of the code if your markdown preprocessor is able to do syntax highlighting (normally it can)"] ],
            "center"
        )
    },
    "Separator": {
        "description": "This object returns a markdown separator (---)",
        "usage": f"Call {InlineCode('Separator()')} with the needed argument",
        "functions": None,
        "arguments": None
    },
    "Link": {
        "description": "This object returns a markdown link ([title](link \"hover title\"))",
        "usage": f"Call {InlineCode('Link()')} with the needed argument",
        "functions": None,
        "arguments": Table(
            ["Argument", "Description"],
            [ ["link", "title", "hoverTitle"], ["The link", "(optional) a title for the link which will be displayed to the user instead of the full link", "A title for the link which will be displayed when the user hovers the link"] ],
            "center"
        )
    },
    "Image": {
        "description": "This object returns a markdown image (![alt text](image URL))",
        "usage": f"Call {InlineCode('Image()')} with the needed argument",
        "functions": None,
        "arguments": Table(
            ["Argument", "Description"],
            [ ["URL", "alt_text"], ["The URL of the image", "(optional) An alt text for the image (by default it is the name found on the given URL)"] ],
            "center"
        )
    },
    "Table": {
        "description": "This object returns a markdown table (\n|header|\n|---|\n|value|)",
        "usage": f"Call {InlineCode('Table()')} with the needed argument",
        "functions": None,
        "arguments": Table(
            ["Argument", "Description"],
            [ ["headers", "values", "alignement"], ["A list of headers", "A list of lists of values", "(optional) the alignement for the table (could be a string (left, center or right) or a list to define the alignement of each column)"] ],
            "center"
        )
    },
    "Footnote": {
        "description": "This object returns a markdown footnote (text[^1]    and then at the end of the file [^1]: note)",
        "usage": f"Call {InlineCode('Footnote()')} with the needed argument",
        "functions": None,
        "arguments": Table(
            ["Argument", "Description"],
            [ ["note", "markdownObj"], ["The content of the note", "The markdown object you want to append the footnote to (it will be added at render time)"] ],
            "center"
        )
    },
    "HeadingID": {
        "description": "This object returns a markdown heading id ({#id})",
        "usage": f"Call {InlineCode('HeadingID()')} with the needed argument",
        "functions": None,
        "arguments": Table(
            ["Argument", "Description"],
            [ ["id", "correctSyntax"], ["The new Heading ID", "If you want to correct the syntax of the ID (incomplete for now)"] ],
            "center"
        )
    },
    "Definition": {
        "description": "This object returns a markdown definition (\nword\n: definition)",
        "usage": f"Call {InlineCode('Definition()')} with the needed argument",
        "functions": None,
        "arguments": Table(
            ["Argument", "Description"],
            [ ["word", "definition"], ["The word to define", "Either a string for one definition or a list of multiple definitions"] ],
            "center"
        )
    },
    "Strikethrough": {
        "description": "This object returns a markdown strikethrough text (~~text~~)",
        "usage": f"Call {InlineCode('Strikethrough()')} with the needed argument",
        "functions": None,
        "arguments": Table(
            ["Argument", "Description"],
            [ ["text"], ["The text to strikethrough"] ],
            "center"
        )
    },
    "TaskList": {
        "description": "This object returns a markdown tasklist ([x] do something)",
        "usage": f"Call {InlineCode('TaskList()')} with the needed argument",
        "functions": Table(
            ["Functions", "Description", "Arguments", "Returned Value"], [
                [InlineCode("addTask()")],
                ["Adds a task to the TaskList"],
                ["task: The task; checked (optional): Wether it is checked"],
                ["Nothing"]
            ],
            "center"
        ),
        "arguments": Table(
            ["Argument", "Description"],
            [ ["task", "checked"], ["The task", "Wether it is checked or not"] ],
            "center"
        )
    },
    "Paragraph": {
        "description": "This object returns a markdown paragraph (text)",
        "usage": f"Call {InlineCode('Paragraph()')} with the needed argument",
        "functions": None,
        "arguments": Table(
            ["Argument", "Description"],
            [ ["text"], ["The content of the paragraph"] ],
            "center"
        )
    },
    "BoldText": {
        "description": "This object returns a markdown bold text (**text**)",
        "usage": f"Call {InlineCode('BoldText()')} with the needed argument",
        "functions": None,
        "arguments": Table(
            ["Argument", "Description"],
            [ ["text"], ["The text"] ],
            "center"
        )
    },
    "ItalicText": {
        "description": "This object returns a markdown italic text (*text*)",
        "usage": f"Call {InlineCode('ItalicText()')} with the needed argument",
        "functions": None,
        "arguments": Table(
            ["Argument", "Description"],
            [ ["text"], ["The text"] ],
            "center"
        )
    },
    "BoldAndItalicText": {
        "description": "This object returns a markdown bold and italic text (***text***)",
        "usage": f"Call {InlineCode('BoldAndItalicText()')} with the needed argument",
        "functions": None,
        "arguments": Table(
            ["Argument", "Description"],
            [ ["text"], ["The text"] ],
            "center"
        )
    },
    "TableOfContent": {
        "description": "This object returns a markdown table of content (\n1. Header\n    - Something\n2. Header\n    - Something else)",
        "usage": f"Call {InlineCode('TableOfContent()')} with the needed argument",
        "functions": None,
        "arguments": Table(
            ["Argument", "Description"],
            [ ["markdownObj", "level"], ["The MarkdownFile object", "The maximum level of heading to include"] ],
            "center"
        )
    }
}

for element in objects:
    README.add(Header(element, 2, README))
    README.add(Paragraph(objects[element]["description"]))
    README.add(Quote(objects[element]["usage"], 1))
    if objects[element]["functions"] is None:
        README.add(Paragraph("There is no functions for the " + str(element) + "object."))
    else:
        README.add(objects[element]["functions"])
    
    if objects[element]["arguments"] is None:
        README.add(Paragraph("There is no arguments to pass for the " + str(element) + "object."))
    else:
        README.add(objects[element]["arguments"])

    README.add(Separator())


#Dependencies
README.add(Header("Dependencies", 1, README))
README.add(Paragraph("Here is a list of the depencies used by markdown-creation"))
README.add(Paragraph("They are automatically downloaded if you install it through pip"))
README.add(Quote("These dependencies are only used to convert the markdown file to HTML"))
README.add(List(["markdown - to convert markdown to html", "beautifulsoup4 - to prettify the html", "htmlmin - to minify the html"]))

#Copyright
README.add(Separator())
README.add(Header("By the way", 1, README))
README.add(Paragraph(f"This whole file was created with markdown-creation (the creation script is {InlineCode('createDocs.py')})"))
README.add(Quote("© Anime no Sekai - 2020"))

#Saving the file
README.html(destination="README.html")
README.save("README.md")
print("Done!")