import pyglet

class GamepadController:
    def __init__(self):
        active = False
        joysticks = pyglet.input.get_joysticks()
        if joysticks:
            joystick = joysticks[0]
            joystick.open()
            active = True
        else:
            print("There is not Gamepad connected!")

    def on_joybutton_press(joystick, button):
        pass

    def on_joybutton_release(joystick, button):
        pass

    def on_joyaxis_motion(joystick, axis, value):
        pass

    def on_joyhat_motion(joystick, hat_x, hat_y):
        pass
