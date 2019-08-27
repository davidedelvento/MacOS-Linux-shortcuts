ac = window.get_active_class()
if (ac == 'mate-terminal.Mate-terminal' or
    ac == 'gnome-terminal-server.Gnome-terminal'):
    pass
elif (ac == 'pluma.Pluma'):
    keyboard.send_keys("<ctrl>+h")
else:
    keyboard.send_keys("<ctrl>+r")
