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
            self.active = True
        else:
            print("There is not Gamepad connected!")

    def getPress(self):
        return self.direction

    # def on_joybutton_press(self, joystick, button):
    #     pass
    #
    # def on_joybutton_release(self, joystick, button):
    #     pass
    #
    # def on_joyaxis_motion(self, joystick, axis, value):
    #     pass

    def on_joyhat_motion(self, joystick, hat_x, hat_y):
        print("Hat ({}, {})".format(hat_x, hat_y))
        if hat_x != 0:
            if hat_x == 1:
                self.direction = key.RIGHT
            if hat_x == -1:
                self.direction = key.LEFT

        if hat_y != 0:
            if hat_y == 1:
                self.direction = key.UP
            if hat_y == -1:
                self.direction = key.DOWN

        pass
