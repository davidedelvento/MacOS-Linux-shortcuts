# MacOS-Linux-shortcuts

### Introduction

This repository is for people dealing with two of more among MacOS, Linux/Gnome and Linux/Mate.
Linux/KDE or other OSes not supported yet (but should be easy to add, please contribute).

Dealing with different keyboard shortcuts uses a lot of mental energy, so to maintain focus on
the task at hand (as opposed to which keys to press) one has to change shortcuts for one or
more of these machines. This repository changes some of the
shortcuts for Linux, and this README suggests a few additional changes, including ones for Mac OS.

Best results will be achieved if you use identical keyboards across all your machines.

### Instructions

1. Install autokey on your Linux box(es) with `sudo apt-get install autokey` or `yum install autokey-gtk` or `pip`.
See [autokey instructions](https://github.com/autokey/autokey/wiki/Installing) if you need details.

2. Fork this repository (optional but recommended)

3. Clone your fork (or this repository, if you did not fork)

4. Point autokey to the nested directory `MacOS-Linux-shortcuts`, e.g. by putting a hard or symbolic link
to it in `~/.config/autokey/data/`

---

### Additional shortcuts

Unrelated to this repository, but related with having sane shortcuts...

#### On the Mac

1. Install [`iterm2`](https://www.iterm2.com/) on the Mac and set the
shortcuts for "move one word" as described 
[here](https://apple.stackexchange.com/questions/154292/iterm-going-one-word-backwards-and-forwards/293988#293988).
You will also need the "move to begin/end of line" and
the corresponding "select" to work as in the other apps, and
this part requires manual configuration. If you use the regular
`terminal` application, you will also need to change its shortcuts. In fact (like on Linux) there are some differences
between terminal and non-terminal shortcuts, not sure why anybody thought that was a good idea...

#### On Linux

2. Configure your Virtual Desktop switcher to use `CTRL-arrows` as Spaces do on the Mac
(this will break the move-by-one-word, but that is fixed by autokey with the scripts in this repository).
Also, arrange your Virtual Dektops on a single line, as Space do on the Mac, and set them to the same number.

3. Configure the shortcut to lock the screen from `CTRL-L` to `CTRL-CMD-q`.

On Mate you can do the last two items by opening the
[Control Center](https://screenshots.debian.net/package/mate-control-center) and selecting `Keyboard Shortcuts`.

On Gnome, proceed as described [here](https://help.gnome.org/users/gnome-help/stable/keyboard-shortcuts-set.html)


### Further documentation

See [Autokey documentation](https://github.com/autokey/autokey/wiki/Scripting)

### Problems, questions or suggestions?

Please submit an [issue](https://github.com/davidedelvento/MacOS-Linux-shortcuts/issues) and I will be happy to respond!

Do also submit Pull Requests:
[Pull Requests](https://help.github.com/en/articles/creating-a-pull-request-from-a-fork) are very welcome
to improve anything, especially wrong or incomplete shortcuts, including ones for Linux/KDE or other OSes.

