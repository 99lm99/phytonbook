from os.path import exists
from CSV_creating import creating
from File_writting import writing_scv
from File_writting import writing_txt


path = 'Phonebook.csv'
valid = exists(path)
if not valid:
    creating()

writing_scv()
writing_txt()