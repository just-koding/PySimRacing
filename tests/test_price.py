import unittest
import time
from classes.price import Price


class TestPrice(unittest.TestCase):

    def test_out(self):
        temp_time = str(time.time())
        stream = "TEST 2.034 -2.34 " + temp_time
        price = Price("TEST", "2.034", "-2.34", temp_time)
        self.assertEqual(stream, price.out)  # add assertion here


if __name__ == '__main__':
    unittest.main()
