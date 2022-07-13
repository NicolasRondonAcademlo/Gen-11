import pytest
from .utils import File

@pytest.fixture()
def persons():
    persons = File().join_csv_files()
    yield persons
