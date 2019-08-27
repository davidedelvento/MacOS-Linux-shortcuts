ac = window.get_active_class()
if (ac != 'mate-terminal.Mate-terminal' and
    ac != 'gnome-terminal-server.Gnome-terminal'):
    keyboard.send_keys("<shift>+<ctrl>+c")
    
