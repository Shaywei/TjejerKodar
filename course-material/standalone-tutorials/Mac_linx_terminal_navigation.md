# Terminal Navigation - Mac/Linux

The filesystem on your computer is like a tree made up of folders (also called "directories") and files.  

The filesystem has a root directory called /, and everything on your computer lives in subdirectories of this root directory.  

We often navigate the filesystem graphically by clicking on graphical folders. We can do the exact same navigation from the command line.  

There are two commands that we'll be using at a command prompt to navigate the filesystem on your computer:  
* `ls`  
* `pwd`
* `cd`
`ls` lists the contents of a directory.
`pwd` gives the full directory path to your current directory.
`cd` moves you into a new directory (it stands for "change directory").  

Let's practice using these commands.

### Open a command prompt:
* On Mac: You can find the Terminal application through Spotlight, or navigate to Applications/Utilities/Terminal.
* On Linux: For example, `Ctrl+Alt+T`

### Practice using `ls`, `pwd` and `cd`

Type each of these commands and hit enter:  

`ls`  
This lists all the files in your home directory.  

`pwd`  
This displays the full directory path to your current directory, which is your home directory.

`cd /`  
This will change you into the `/` root directory.

`ls`  
This lists the contents of the `/` root directory.  

`cd Users` (Mac) or `cd home` (Linux)
This will change you into the Users subdirectory of the `C:\` directory.

`ls`  
You should see the names of all the files and directories in `/Users` / `/home` respectively.

`pwd`  
This displays the full directory path to your current directory, `/Users` / `/home`.

`cd ..`  
`..` means "parent directory", so this command moved you up to the parent directory.  
You were in `/Users` / `/home`, so now you are in `/`, the root directory.

`ls`  
This lists the contents of the root directory, confirming where you are.

### Tips
* You can use Tab to auto-complete directory and file names. So from inside the root directory /, if you type cd Us and hit Tab, the command prompt will auto-complete the directory name, and you can then hit enter to change into the `/Users` / `/home` directory.
* The command prompt maintains a command history. You can use the up arrow to cycle through old commands.

### Check your understanding
Answer these questions. Experiment at the command line if you need to! If you aren't sure about an answer, ask a helper.

1. What directory are you in after starting a new command line prompt?
2. After starting a new command line prompt, how would you get to the root directory?
3. How do you check what files and directories are in your current working directory?
4. If you are in directory `/Users` / `/home`, and you want to get to `/Users/jesstess/projects` / `/home/jesstess/projects`, how would you do that?
5. What are 2 ways to avoid typing out a full navigation command? (hint: one requires that you've run the command before)
6. What is the difference between a command prompt and a Python prompt?

### Success!
You've practiced using dir and cd to navigate your computer's filesystem from the command prompt.
