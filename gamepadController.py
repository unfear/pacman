import pyglet
from pyglet.window import key

class GamepadController:
    def __init__(self):
        self.active = False
        joysticks = pyglet.input.get_joysticks()
        self.direction = key.O
        if joysticks:
            joystick = joysticks[0]
            joystick.open()
            joystick.push_handlers(self)
            active = True
        else:
            print("There is not Gamepad connected!")

    def getPress(self):
        return self.direction

    def on_joybutton_press(joystick, button):
        pass

    def on_joybutton_release(joystick, button):
        pass

    def on_joyaxis_motion(joystick, axis, value):
        pass

    def on_joyhat_motion(joystick, hat_x, hat_y):
        if hat_x != 0:
            if hat_x == 1:
                global direction
                direction = key.RIGHT
            if hat_x == -1:
                direction = key.LEFT

        if hat_y != 0:
            if hat_y == 1:
                direction = key.UP
            if hat_y == -1:
                direction = key.DOWN

        pass
