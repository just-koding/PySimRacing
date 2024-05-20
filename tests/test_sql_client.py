import pytest
import time

from src.classes.price import Price


def test_insert_sql_price_values(sql_client):
    sql_client.insert_price_values("test_insert_sql_price_values", "2.034", "-2.34", str(time.time()))
    sql_client.print_prices()


def test_insert_sql_price_object(sql_client):
    price = Price("test_insert_sql_price_object", "1.463", "32.44", str(time.time()))
    sql_client.insert_price_object(price)
    sql_client.print_prices()
