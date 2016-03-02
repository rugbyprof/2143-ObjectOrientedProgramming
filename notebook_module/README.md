Python 3 Object Oriented Programming
Harness the power of Python 3 objects
Dusty Phillips
http://www.amazon.com/Python-3-Object-Oriented-Programming/dp/1849511268

To tie it all together, let's build a simple command-line notebook application. This is a fairly simple task, so we won't be experimenting with multiple packages. We will, however, see common usage of classes, functions, methods, and docstrings.

Let's start with a quick analysis: Notes are short memos stored in a notebook. Each note should record the day it was written and can have tags added for easy querying. It should be possible to modify notes. We also need to be able to search for notes. All of this should be done from the command-line.

The obvious object is the Note. Less obvious is a Notebook container object. Tags and dates also seem to be objects, but we can use dates from Python's standard library and a comma-separated string for tags. To avoid complexity at this point, let's not de ne separate classes for these objects.

Note objects have attributes for the memo itself, tags, and a creation_date. Each note will also need a unique integer id, so that users can select them in a menu interface. Notes could have a method to modify note content and another for tags, or we could just let the notebook access those attributes directly. To make searching easier, we should put a match method on the Note. This method will accept a string and can tell us if a note matches the string without accessing the attributes directly. That way, if we want to modify the search parameters (to search tags instead of note contents, for example, or to make the search case-insensitive), we only have to do it in one place.

The Notebook obviously has the list of notes as an attribute. It will also need a search method that returns a list of  ltered notes.

But how do we interact with these objects? We've speci ed a command-line app, which can either mean we run the program with different options to add or edit commands, or we could have some kind of a menu that allows us to pick different things to do to the notebook. It would be nice if we could design it so that either interface was allowed, or we could add other interfaces such as a GUI toolkit or a web-based interface in the future.

As a design decision, we'll implement the menu interface now, but will keep the command-line options version in mind to ensure we design our Notebook class with extensibility in mind.

So if we have two command-line interfaces each interacting with the Notebook, then Notebook is going to need some methods for them to interact with. We'll need to be able to add a new note, and modify an existing note by id, in addition to the search method we've already discussed. The interfaces will also need to be able to list all notes, but they can do that by accessing the notes list attribute directly.

We may be missing a few details, but that gives us a really good overview of the code we need to write. We can summarize all this in a simple class diagram:
                                                                                                                                                                                         Before writing any code, let's de ne the folder structure for this project. The menu interface should clearly be in its own module, since it will be an executable script, and we may have other executable scripts accessing the notebook in the future. The Notebook and Note objects can live together in one module. These modules can both exist in the same top-level directory without having to put them in a package. An empty command_option.py module can help remind us in the future that we were planning to add new user interfaces.
