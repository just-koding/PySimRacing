""" This file contains all classes used in the events sharing data between
the GUI and the SDK module """


class UIData():
    """ UIData """
    def __init__(self) -> None:
        self.button_pressed = False

    def set_button_pressed(self, value: bool):
        """ set_button_pressed """
        self.button_pressed = value

    def get_button_pressed(self) -> bool:
        """ get_button_pressed """
        return self.button_pressed


class SDKData():
    """ SDKData """
    def __init__(self) -> None:
        self.time = 0

    def set_time(self, value: int):
        """ set_time """
        self.time = value

    def get_time(self) -> int:
        """ get_time """
        return self.time
