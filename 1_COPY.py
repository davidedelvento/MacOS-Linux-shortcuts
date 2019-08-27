if window.get_active_class() != 'mate-terminal.Mate-terminal':
    keyboard.send_keys("<ctrl>+c")
else:
    keyboard.send_keys("<ctrl>+<shift>+c")
    
