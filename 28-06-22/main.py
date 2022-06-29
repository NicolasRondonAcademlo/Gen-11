# https://realpython.com/working-with-files-in-python/#filename-pattern-matching+
import os

entries = os.listdir("sub_dir")
for entry in entries:
    print(entry)

entries = os.scandir("../../")
for entry in entries:
    print(entry.is_file(), entry.name)


from pathlib import Path
entries = Path("./")
print(entries.absolute())
entries = Path("")
for entry in entries.iterdir():
    print(entry.name)

print("-------")
print("-------")
print("-------")
print("-------")


for entry in os.listdir("./"):
    print(os.path.join("./", entry))
    if os.path.isfile(os.path.join("./", entry)):
        print(entry)

entries = os.scandir("../")
for entry in entries:
    if entry.is_file():
        print(entry.name, 777)


