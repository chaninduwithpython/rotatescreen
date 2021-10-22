import rotatescreen
import keyboard

screen = rotatescreen.get_primary_display()

keyboard.add_hotkey('ctrl+windows+up', screen.set_landscape, suppress=True)
keyboard.add_hotkey('ctrl+windows+down', screen.set_portrait_flipped, suppress=True)
keyboard.add_hotkey('ctrl+windows+right', screen.set_portrait_flipped(), suppress=True)
keyboard.add_hotkey('ctrl+windows+left', screen.set_portrait, suppress=True)

keyboard.wait()
