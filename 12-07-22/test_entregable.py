# TDD -> Test Development Driven
from .utils import File, ProccesList

def test_get_files():
    files = File().all_files()
    assert files == ["quiz_1.csv", 'quiz_2.csv']

def test_open_file():
    files = File().open_file(file_name="quiz_1.csv")
    assert type(files) == list

def test_join_csv_files():
    persons = File().join_csv_files()
    assert len(persons) == 67

def test_process_list_person(persons):
     persons = ProccesList(persons).persons
     assert persons

def test_process_list(persons):
    winners = ProccesList(persons).get_winners(4, "Score")
    assert len(winners) == 4

def test_persons_acurracy(persons):
    persons_to_process = File().get_persons_divide_each_quizz()
    acurracy = ProccesList(persons).get_percent_greater_than(persons_to_process,85)
    assert acurracy