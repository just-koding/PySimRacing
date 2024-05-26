""" App starting point """
from core.worker.game import IRacingWorker
from core.worker.gui import UIWorker


def init_app():
    """ Inits all main resources (workers) """
    try:
        gui_worker = UIWorker()
        game_worker = IRacingWorker()
        # when the UI sends an event the SDK will receive an "ui_update"
        gui_worker.subscribe("ui_update", game_worker.ui_update)
        # when the SDK sends an event the UI will receive an "data_update"
        game_worker.subscribe("data_update", gui_worker.data_update)
        gui_worker.start()
        game_worker.start()
        print("App Init!")
    except KeyboardInterrupt:
        # press ctrl+c to exit
        game_worker.stop()
        gui_worker.stop()


if __name__ == '__main__':
    init_app()
