import os
from typing import List
import csv
class File():
    
    def all_files(self, root_path="./") -> List:
        """Get all files names by an especified root_path

        Args:
            root_path (str, optional):  Defaults to "./".

        Returns:
            List: List with all files names
        """
        files = os.listdir(root_path)
        files = [file_name for file_name in files if file_name.endswith(".csv")]
        return files

    def open_file(self, file_name:str) -> List:

        """Open csv file and generate a list 
        with csv rows

        Args:
            file_name (str): Name of file

        Returns:
            List: list of csv rows
        """
        with open(file_name, 'r', encoding="utf-8") as csv_file:
            data = csv.DictReader(csv_file)
            result = []
            for person in data:
                result.append(person)
        return result

    def join_csv_files(self, root_path:str=None):
        files =  self.all_files(root_path=root_path)
        lista= []
        for file_name in files:
            items =self.open_file(file_name) 
            lista += items
        return lista

    def get_persons_divide_each_quizz(self, root_path:str=None):
        files =  self.all_files(root_path=root_path)
        lista= []
        for file_name in files:
            items =self.open_file(file_name) 
            lista.append(items)
        return lista

class ProccesList():
    def __init__(self, persons, extra_points=None) -> None:
        self.persons = persons
        self.__concatenate_persons()
        self.extra_points =self.sum_extra_points(extra_points)
        

    def sum_extra_points(self, values=None):
        return values

    def __concatenate_persons(self):
        for person in self.persons:
            person["name"] = str(person["First Name"] + " "  + person["Last Name"]).upper()
            del person["First Name"]
            del person["Last Name"]

    def get_winners(self, total_winners, value):
        persons = self.persons
        result = {}
        extra_points=self.extra_points
        for person in persons:
            if person["name"] not in result.keys():
                result[person["name"]] = int(person[value])
                try:
                    if person["name"] in extra_points.keys():
                        result[person["name"]] = int(person[value]) + extra_points[person["name"]]
                except AttributeError:
                    pass
            else:
                result[person["name"]] +=  int(person[value])
        try:
            result = sorted(result.items(), key=lambda x:x[1], reverse=True)
        except:
            result = []
        return result[0:total_winners]

    def get_percent_greater_than(self,persons, value):
        result = []
        for person in persons:
            for person_inner in person:
                value_percent = person_inner["Accuracy"].split()
                if int(value_percent[0])> value:
                    result.append(person_inner)
        return result
