""" This files has all classes and functions to get
the IRacing data from the game while running """
import time
import irsdk
from core.data.event_data import SDKData


class IrSdk():
    """ Gets all the data available from IRacing """

    def __init__(self) -> None:
        print('irsdk init')
        self.car_number = 1
        self.cam = 9
        self.ir_connected = False
        self.last_car_setup_tick = -1
        self.run_loop = True
        self.fps = 5
        # initializing ir and self
        self.ir = irsdk.IRSDK()
        self.sdk_data = SDKData()

    def check_iracing(self):
        """ Validates the IRacing connection """
        if self.ir_connected and not (self.ir.is_initialized and self.ir.is_connected):
            self.stop_loop()
        elif not self.ir_connected and self.ir.startup() and self.ir.is_initialized and self.ir.is_connected:
            self.start_loop()

    def loop(self, callback):
        """ Loop function startign the process """
        while self.run_loop:
            time.sleep(1/self.fps)
            if self.ir.is_connected:
                self.ir.freeze_var_buffer_latest()

                t = self.ir['SessionTime']
                self.sdk_data.set_time(t)
                print('session time:', t)

                car_setup = self.ir['CarSetup']
                if car_setup:
                    car_setup_tick = self.ir.get_session_info_update_by_key('CarSetup')
                    if car_setup_tick != self.last_car_setup_tick:
                        self.last_car_setup_tick = car_setup_tick
                        print('car setup update count:', car_setup['UpdateCount'])
                self.ir.cam_switch_pos(self.car_number, self.cam)
            else:
                print("Detected Disconnection from IRSDK")
            callback(self.sdk_data)

    def stop_loop(self):
        """ Starts the loop process """
        print('irsdk stop_loop')
        self.ir_connected = False
        # don't forget to reset your self variables
        self.last_car_setup_tick = -1
        # we are shutting down ir library (clearing all internal variables)
        self.run_loop = False
        self.ir.shutdown()

    def start_loop(self):
        """ Stops the loop process """
        print('irsdk start_loop')
        self.ir_connected = True

    def pause_loop(self):
        """ Pauses the loop process """
        print('irsdk pause_loop')
        self.run_loop = False

