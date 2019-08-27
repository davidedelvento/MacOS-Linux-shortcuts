ac = window.get_active_class()
if (ac == 'mate-terminal.Mate-terminal' or
    ac == 'gnome-terminal-server.Gnome-terminal'):
    keyboard.send_keys("<ctrl>+<right>")
else:
    keyboard.send_keys("<shift>+<ctrl>+<right>")
