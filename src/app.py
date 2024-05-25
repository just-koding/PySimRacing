from core.worker.game import IRacingWorker


def init_app():
    try:
        worker = IRacingWorker()
        worker.start()
    except KeyboardInterrupt:
        # press ctrl+c to exit
        worker.stop()


if __name__ == '__main__':
    init_app()
