# MacOS-Linux-shortcuts

### Introduction

This repository is for people dealing with two of more among MacOS, Linux/Gnome and Linux/Mate.
Linux/KDE or other OSes not supported yet (but should be easy to add, please contribute).

Dealing with different keyboard shortcuts quickly becomes untenable, so to maintain sanity
one has to change shortcuts for one or more of these machines. This repository changes the
shortcuts for Linux, and suggests a few changes for Mac OS.

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

1. Install [`iterm2`](https://www.iterm2.com/) on the Mac and make sure the
shortcuts for "move one word", "move to begin/end of line" and
the corresponding "select" work as in the other apps.
This requires manual configuration and would be needed even with the regular
`terminal` application, otherwise (like on Linux) there are some differences
between terminal and non-terminal shortcuts, which can drive you crazy..

#### On Linux

2. Configure your Virtual Desktop switcher to use `CTRL-arrows` as Spaces do on the Mac
(this will break the move-by-one-word, but that is fixed by autokey). Also, arrange your
Virtual Dektops on a single line, as Space do on the Mac, and set them to the same number.

3. Configure the shortcut to lock the screen from `CTRL-L` to `CTRL-CMD-q`

For the last three points, I will link the
instructions on how to do this as soon as soon as I find them again,
see [here](https://meta.stackexchange.com/questions/283899/) for details.

### Further documentation

See [Autokey documentation](https://github.com/autokey/autokey/wiki/Scripting)

### Problems, questions or suggestions?

Please submit an issue and I will be happy to respond! Do also submit Pull Requests:
[Pull Requests](https://help.github.com/en/articles/creating-a-pull-request-from-a-fork) are very welcome
to improve anything, especially wrong or incomplete shortcuts, including ones for Linux/KDE or other OSes.

