# MacOS-Linux-shortcuts

### Introduction

I have recently switched OS at work, getting a MacOS, while still keeping Linux Gnome and Mate at home.

Dealing with different keyboard shortcuts quickly became untenable, so I looked around for solutions, i.e. a setup on Linux to use the same shortcuts as the Mac.
Unfortunately I found no satisfactory solutions, so I proceeded as follows. You may use the following as instructions to use this repository.

### Instructions

1. Install autokey on your Linux box(es) with `sudo apt-get install autokey`

2. Fork this repository (optional but preferred way, so you can save your own changes and
make pull requests from them if appropriate)

3. Clone your fork (or this repository, if you did not fork)

4. Point autokey to it, e.g. by putting the clone, or a (symbolic) link to it in `~/.config/autokey/data/`

---

### Additional shortcuts

Unrelated to this repository, but related with having sane shortcuts, I also did the following:

1. Install `iterm2` on the Mac and make sure the
shortcuts for "move one word", "move to begin/end of line" and
the corresponding "select" work as in the other apps.
This requires manual configuration and would be needed even with the regular
`terminal` application, otherwise (like on Linux) there are some differences
between terminal and non-terminal shortcuts.

2. Configure your Linux Virtual Desktop switcher to use `CTRL-arrows` instead of
`CTRL-ALT-arrows` so the shortcut is consistent with the one on the Mac (this will break the
move-by-one-word, but that is fixed by autokey)

For the last two points, I will link the
instructions on how to do this as soon as soon as I find them again,
see [here](https://meta.stackexchange.com/questions/283899/) for details.

