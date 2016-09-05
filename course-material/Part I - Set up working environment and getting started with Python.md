# Setting up your Python working environment

This part was shamelessly copied from http://wiki.openhatch.org/Boston_Python_Workshop_6/Friday (with tiny modification).  

The reason for the copying and not using original source is to avoid the risk of the original source not available during the class for any reason.

## Goal #1: Set up Python

This section has instructions for installing Python and running Python from a command prompt.

* [Windows](./standalone-tutorials/Windows_set_up_Python.md)
* [Mac](./standalone-tutorials/OSX_set_up_Python.md)
* [Linux](./standalone-tutorials/Linux_set_up_Python.md)

## Goal #2: Prepare a text editor

In addition to being able to run Python, we are going to install a good text editor for writing and saving Python code during the workshop.  

If you would like to use a different text editor from the recommendation for your operating system, please let a staff member know.

* [Sublime Text (available for Windows/Mac/Linux)](./standalone-tutorials/Text_editor.md)

## Goal #3: Practice starting and exiting Python

We'll do a lot of learning and practicing at a Python prompt (this is "interactive" because you are typing the code and hitting enter to run it yourself, instead of running it from a file).  
So let's practice starting and exiting Python:

* [Windows](./standalone-tutorials/Windows_interactive_Python.md)
* [Mac / Linux](./standalone-tutorials/Mac_Linux_interactive_Python.md)

## Goal #4: Practice navigating the computer from a command prompt

We will be running files containing Python code (Python "scripts") from the command prompt.  
You'll need to be able to navigate to those scripts using the command prompt so you can run them.  
In this section, we'll practice using these navigation commands.

* [Windows](./standalone-tutorials/Windows_terminal_navigation.md)
* [Mac / Linux](./standalone-tutorials/Mac_linx_terminal_navigation.md)

## Goal #5: Practice running Python code from a file

Interactive Python programming at a Python prompt is great for short pieces of code and for testing ideas.  
For longer code, it can be easier to save the code in a file, and execute the contents of that file (aka a Python script).  
In this section, we'll practice running Python scripts.

We're now going into deep waters and giving instructions eith one higher level of abstraction (assuming you have good control of previous steps).

### Create your first Hello World script in Python

1. Start your text editor
2. Start a new, blank text file
3. Add the following line to your text file:  
`print "Hellow World!"`  
4. Save the script as `hello.py` in your Desktop directory. The `.py` extension indicated that this file contains Python code.

### Run your script

1. Start a new command prompt (see previous goals tutorial if you forgot how to).
2. Navigate to your Desktop directory form the command prompt using `cd` / `dir` (Windows) or `ls`, `pwd`, `cd` (Mac/Linux) commands.
3. Once you are in your Desktop directory, you'll see `hello.py` in the output of `dir` / `ls`.
4. Type  
`python hello.py`  
and hit enter.
Doing this will cause Python to execute the contents of that script -- it should print `Hello World!` to the screen.  
What you've done here is run the Python application with an argument -- the name of a file, in this case `hello.py`.  
Python knows that when you give it a file name as an argument, it should execute the contents of the provided file.  
You get the same result as if you typed  
`print "Hello World!"`  
at a Python prompt and hit enter.

### Success

You created and ran your first Python script!
* When you run the python command by itself, you start a Python prompt. You can execute Python code interactively at that prompt.
* When you run the python command with a file name as an argument, Python executes the Python code in that file.
