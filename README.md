# MacOS-Linux-shortcuts
I have recently switched OS at work, getting a MacOS, while still keeping Linux Gnome and Mate at home.

Dealing with different keyboard shortcuts quickly became untenable, so I looked around for solutions, i.e. a setup on Linux to use the same shortcuts as the Mac.
Unfortunately I found no satisfactory solutions, so I proceeded as follows. You may use the following as instructions to use this repository.

1. I installed autokey on my Linux box(es) with `sudo apt-get install autokey`

2. I created this repository and pointed autokey to it. You may want to
    1. fork it (optional but preferred way, so you can save your own changes and make pull requests of them if appropriate)
    2. clone your fork (or this repository, if you did not fork)
    3. point autokey to it, e.g. by putting the clone, or a (symbolic) link to it in `~/.config/autokey/data/`

---

Unrelated to this repository, but related with having sane shortcuts, I also did the following:

1. I installed `iterm2` on the Mac, for various reasons, and I made sure the "move one word", "move to begin/end of line" and the corresponding "select" worked. This required manual configuration. This needed to be done even with the regular `terminal` application, otherwise (like on Linux) there are some differences between terminal and non-terminal shortcuts, but I need them to be the same, yet I get crazy.... You may want to do the same, and I will link the instructions there as soon as they let me find it again, see [here](for details)
