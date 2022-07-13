from utils import File, ProccesList

data = File().join_csv_files()
data_acurracy = File().get_persons_divide_each_quizz()

result = ProccesList(data)
print(result.get_winners(2,"Score"))

#print(result.get_percent_greater_than(data_acurracy, 70))