from datetime import datetime
import time
from src.database import SqliteClient
from src.database.maria_client import MariaClient
from src.polosdk import RestClient
from src.yml import decode_yaml_config
from threading import Thread
import os


class CustomTimer(Thread):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.sql_client = None
        self.start_time = time.time()
        self.client = RestClient()
        self.pairs = decode_yaml_config()['pairs']
        self.timer_running = False
        self.cool_down = 20

    def process_pairs(self):
        for pair in self.pairs:
            response = self.client.markets().get_price(pair)
            symbol = response['symbol']
            price = response['price']
            daily_change = response['dailyChange']
            price_time = response['time']
            self.sql_client.insert_price_values(symbol, price, daily_change, price_time)

    def start_timer(self):
        self.timer_running = True
        #db_path = os.path.join(os.path.abspath(os.curdir),
        #    "db","data.db")
        #print(f"using db from: {db_path}")
        #self.sql_client = SqliteClient(db_path)
        #self.sql_client.init_prices()
        self.sql_client = MariaClient()
        self.sql_client.init_prices()

        while self.timer_running:
            self.process_pairs()
            time.sleep(self.cool_down)

    def stop_timer(self):
        self.timer_running = False

    def run(self):
        # thumbnail will be resolved on second OR newly created below thread
        thread = Thread(target=self.start_timer)
        thread.start()
