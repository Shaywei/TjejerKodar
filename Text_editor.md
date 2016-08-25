# Text Editor - Mac / Linux / Linux

## My recommendation

**Sublime Text 3** - A powerful, extendable yet lightweight text editor.

* [OSX Download](https://download.sublimetext.com/Sublime%20Text%20Build%203114.dmg)
* [Windows](https://download.sublimetext.com/Sublime%20Text%20Build%203114%20Setup.exe)
* [Windows 64 bit](https://download.sublimetext.com/Sublime%20Text%20Build%203114%20x64%20Setup.exe)
* [Linux (Ubuntu) 64 bit](https://download.sublimetext.com/sublime-text_build-3114_amd64.deb)
* [Linux (Ubuntu) 32 bit](https://download.sublimetext.com/sublime-text_build-3114_i386.deb)


### Basic configuration of Sublime for Python:

Go to: `Sublime Text > Preferences > Settings – User`
Add the following to the file:

```
{
  // base settings
  "word_wrap": true
	"translate_tabs_to_spaces": true
}
```

### Install Package Control

To begin taking advantage of the various packages for extending Sublime’s functionality, you need to install the package manager called Package Control – which you must install manually. Once installed, you can use Package Control to install/remove/upgrade all other ST3 packages.

1. install, copy the Python code for Sublime Text 3 found [here](https://sublime.wbond.net/installation#st3). Click `View > Show Console` to open the ST3 console. Paste the code into the console. Press Enter. Reboot ST3.
2. You can now install packages by using the keyboard shortcut `cmd+shift+P`. Start typing install until Package Control: Install Package appears. Press Enter and search for available packages.
3. Some other relevant commands are:
  * List Packages shows all your installed packages
  * Remove Packages removes a specific package
  * Upgrade Package upgrades a specific package
  * Upgrade/Overwrite All Packages upgrades all your installed packages

### Insatll some useful packages

Install the following packages:

* Git
* Python Flake8 Lint
* SideBarEnhancements
* SyncedSideBar


