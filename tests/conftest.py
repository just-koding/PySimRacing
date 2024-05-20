import pytest
import os

from src.database import SqliteClient


@pytest.fixture
def write_file():
    print('\nCreating file')
    f = open('append_file.txt', 'w+', encoding='utf-8')

    for i in range(20):
        f.write('\nX Y Z %d' % (i + 1))

    f.flush()

    yield f

    print('\nClosing file')
    f.close()


@pytest.fixture(scope='module')
def sql_client():
    print('\nCreating DB')
    sql_client = SqliteClient("test.db")
    sql_client.init_prices()
    yield sql_client

    del sql_client
