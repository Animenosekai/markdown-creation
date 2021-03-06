# markdown-creation  

> A markdown file creation module for Python!  

# Table of Content  

1. [markdown-creation](#markdown-creation)
2. [Table of Content](#table-of-content)
3. [What is markdown-creation?](#what-is-markdown-creation)
    - [Features](#features)
4. [How to use?](#how-to-use)
    - [MarkdownFile](#markdownfile)
        - [Header](#header)
        - [Quote](#quote)
        - [OrderedList](#orderedlist)
        - [List](#list)
        - [InlineCode](#inlinecode)
        - [BlockCode](#blockcode)
        - [Separator](#separator)
        - [Link](#link)
        - [Image](#image)
        - [Table](#table)
        - [Footnote](#footnote)
        - [HeadingID](#headingid)
        - [Definition](#definition)
        - [Strikethrough](#strikethrough)
        - [TaskList](#tasklist)
        - [Paragraph](#paragraph)
        - [BoldText](#boldtext)
        - [ItalicText](#italictext)
        - [BoldAndItalicText](#boldanditalictext)
        - [TableOfContent](#tableofcontent)
5. [Dependencies](#dependencies)
6. [By the way](#by-the-way)
  

# What is markdown-creation?  

markdown-creation is a Python Module which lets you write Markdown Files (`.md` files like `README.md`)  

Especially useful when it comes down to creating your documentations programmatically (writing scripts to automate things) or rendering files for web servers, it can do many things!  

## Features  

- Markdown File Creation
- Automatic Table of Content creation
- Table creation
- HTML output (normal or minified)
- Less syntax errors
- Easy to use  

# How to use?  

### Here is a list of all the objects which comes with markdown-creation  

## MarkdownFile  

This object initializes a new markdown file  

> You need to initialize a markdown file to put content in it. To initialize a new markdown file, just call it in a variable `myAwesomeFile = MarkdownFile()`  

| Functions | Description | Arguments | Returned Value |
| :-----: | :-----: | :-----: | :-----: |
| `add()` | Adds a line to the markdown file | object: What you want to add (it could be multiple objects but inside of an object, a string) | Nothing |
| `save()` | Saves the markdown file to the given location | destination: The destination of the file; appendToExistingFile: Wether or not you want to override (False) or append (True) if the file is already existing | Nothing |
| `tableOfContent()` | Returns a string representing the table of content at the current state (yeah I can't predict what you're going to put inside your file) | level: The maximum header level you want to add | A string with the table of content |
| `render()` | Renders the whole file into a string | No argument | A string with the markdown file |
| `html()` | Renders the file as an HTML file and gives back a string (and outputs it if you set the destination argument) | title: Set this if you want to override the HTML title tag (by default it takes the first header content); onlyMarkdown: If you don't want a whole HTML file but only the HTML representation of your markdown file; minify: If you want to minify the HTML; destination: Set this argument if you want to output your HTML file | A string with the HTML file |
  

There is no arguments to pass for the MarkdownFileobject.  

---  

## Header  

This object returns a markdown header (# content) and adds a header to the index of headers of the provided markdown file  

> Call `Header()` with the needed argument  

There is no functions for the Headerobject.  

| Argument | Description |
| :-----: | :-----: |
| text | The content of the header |
| level | The level of the header (how many #) |
| markdownObj | The MarkdownFile() object you want to add the header (used to make the Table of Content) |
  

---  

## Quote  

This object returns a markdown quotation text (> content)  

> Call `Quote()` with the needed argument  

There is no functions for the Quoteobject.  

| Argument | Description |
| :-----: | :-----: |
| text | The content of the quote |
| level | The level of the quotation (how many >) |
  

---  

## OrderedList  

This object returns a markdown ordered list (  
1. content  
2. content)  

> Call `OrderedList()` with the needed argument  

There is no functions for the OrderedListobject.  

| Argument | Description |
| :-----: | :-----: |
| inputList | The list to turn into a markdown ordered list |
|  |  |
  

---  

## List  

This object returns a markdown list (  
- content  
- content)  

> Call `List()` with the needed argument  

There is no functions for the Listobject.  

| Argument | Description |
| :-----: | :-----: |
| inputList | The list to turn into a markdown unordered list |
  

---  

## InlineCode  

This object returns a markdown inline code string (`code content`)  

> Call `InlineCode()` with the needed argument  

There is no functions for the InlineCodeobject.  

| Argument | Description |
| :-----: | :-----: |
| code | The content of the inline code |
  

---  

## BlockCode  

This object returns a markdown code block (  
```  
code  
```  
)  

> Call `CodeBlock()` with the needed argument  

There is no functions for the BlockCodeobject.  

| Argument | Description |
| :-----: | :-----: |
| code | The content of the block code |
| language | (optional) The language of the code if your markdown preprocessor is able to do syntax highlighting (normally it can) |
  

---  

## Separator  

This object returns a markdown separator (---)  

> Call `Separator()` with the needed argument  

There is no functions for the Separatorobject.  

There is no arguments to pass for the Separatorobject.  

---  

## Link  

This object returns a markdown link ([title](link "hover title"))  

> Call `Link()` with the needed argument  

There is no functions for the Linkobject.  

| Argument | Description |
| :-----: | :-----: |
| link | The link |
| title | (optional) a title for the link which will be displayed to the user instead of the full link |
| hoverTitle | A title for the link which will be displayed when the user hovers the link |
  

---  

## Image  

This object returns a markdown image (![alt text](image URL))  

> Call `Image()` with the needed argument  

There is no functions for the Imageobject.  

| Argument | Description |
| :-----: | :-----: |
| URL | The URL of the image |
| alt_text | (optional) An alt text for the image (by default it is the name found on the given URL) |
  

---  

## Table  

This object returns a markdown table (  
|header|  
|---|  
|value|)  

> Call `Table()` with the needed argument  

There is no functions for the Tableobject.  

| Argument | Description |
| :-----: | :-----: |
| headers | A list of headers |
| values | A list of lists of values |
| alignement | (optional) the alignement for the table (could be a string (left, center or right) or a list to define the alignement of each column) |
  

---  

## Footnote  

This object returns a markdown footnote (text[^1]    and then at the end of the file [^1]: note)  

> Call `Footnote()` with the needed argument  

There is no functions for the Footnoteobject.  

| Argument | Description |
| :-----: | :-----: |
| note | The content of the note |
| markdownObj | The markdown object you want to append the footnote to (it will be added at render time) |
  

---  

## HeadingID  

This object returns a markdown heading id ({#id})  

> Call `HeadingID()` with the needed argument  

There is no functions for the HeadingIDobject.  

| Argument | Description |
| :-----: | :-----: |
| id | The new Heading ID |
| correctSyntax | If you want to correct the syntax of the ID (incomplete for now) |
  

---  

## Definition  

This object returns a markdown definition (  
word  
: definition)  

> Call `Definition()` with the needed argument  

There is no functions for the Definitionobject.  

| Argument | Description |
| :-----: | :-----: |
| word | The word to define |
| definition | Either a string for one definition or a list of multiple definitions |
  

---  

## Strikethrough  

This object returns a markdown strikethrough text (~~text~~)  

> Call `Strikethrough()` with the needed argument  

There is no functions for the Strikethroughobject.  

| Argument | Description |
| :-----: | :-----: |
| text | The text to strikethrough |
  

---  

## TaskList  

This object returns a markdown tasklist ([x] do something)  

> Call `TaskList()` with the needed argument  

| Functions | Description | Arguments | Returned Value |
| :-----: | :-----: | :-----: | :-----: |
| `addTask()` | Adds a task to the TaskList | task: The task; checked (optional): Wether it is checked | Nothing |
  

| Argument | Description |
| :-----: | :-----: |
| task | The task |
| checked | Wether it is checked or not |
  

---  

## Paragraph  

This object returns a markdown paragraph (text)  

> Call `Paragraph()` with the needed argument  

There is no functions for the Paragraphobject.  

| Argument | Description |
| :-----: | :-----: |
| text | The content of the paragraph |
  

---  

## BoldText  

This object returns a markdown bold text (**text**)  

> Call `BoldText()` with the needed argument  

There is no functions for the BoldTextobject.  

| Argument | Description |
| :-----: | :-----: |
| text | The text |
  

---  

## ItalicText  

This object returns a markdown italic text (*text*)  

> Call `ItalicText()` with the needed argument  

There is no functions for the ItalicTextobject.  

| Argument | Description |
| :-----: | :-----: |
| text | The text |
  

---  

## BoldAndItalicText  

This object returns a markdown bold and italic text (***text***)  

> Call `BoldAndItalicText()` with the needed argument  

There is no functions for the BoldAndItalicTextobject.  

| Argument | Description |
| :-----: | :-----: |
| text | The text |
  

---  

## TableOfContent  

This object returns a markdown table of content (  
1. Header  
    - Something  
2. Header  
    - Something else)  

> Call `TableOfContent()` with the needed argument  

There is no functions for the TableOfContentobject.  

| Argument | Description |
| :-----: | :-----: |
| markdownObj | The MarkdownFile object |
| level | The maximum level of heading to include |
  

---  

# Dependencies  

Here is a list of the depencies used by markdown-creation  

They are automatically downloaded if you install it through pip  

> These dependencies are only used to convert the markdown file to HTML  

- markdown - to convert markdown to html
- beautifulsoup4 - to prettify the html
- htmlmin - to minify the html  

---  

# By the way  

This whole file was created with markdown-creation (the creation script is `createDocs.py`)  

> © Anime no Sekai - 2020  

