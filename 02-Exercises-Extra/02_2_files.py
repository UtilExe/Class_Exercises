# Exercise read and write
# 1. create a function in python, that can read all names of files in a folder, when given the full path to the folder
print("Task 1: ")
import os
def readNamesOfFilesInFolder(path):
    entries = os.listdir(path)

    for entry in entries:
        print(entry)

readNamesOfFilesInFolder('C:/Users/Emil/Desktop/Skole/docker');


print("Task 2: ")
import re # used for the regression matcher.. there may be a better way..
#2. create a function, that can read all lines from a file and copy to another file only the lines, that starts with a number


intLines = []
def readLinesToNumb(filename) :
    with open(filename,'r') as file_object:
        lines = file_object.readlines()
    value = 0
    for line in lines:
        if re.match(r"^\d+.*$",line): # was needed to identify if the starting value was a number. isdigit did not work. and int convertion would crash when it was a string. maybe there's a better way?
            intLines.append(line)

def copyToOtherFile(filename, array):
    with open(filename, 'w') as file_object:
        for numb in array:
            file_object.write(numb)

readLinesToNumb('C:/Users/Emil/Desktop/Skole\Python/Materiale/docker_notebooks/notebooks/my_notebooks/02-Exercises-Extra/data.txt')
copyToOtherFile('C:/Users/Emil/Desktop/Skole\Python/Materiale/docker_notebooks/notebooks/my_notebooks/02-Exercises-Extra/datanumbers.txt', intLines)

# 3. create a function that can read all files in folder and all subfolders and print a list of all png files including their full path name
print("Task 3: ")
def readFolderPrintPng(path):
    entries = os.listdir(path) #not sure how to get subfolders.

    for entry in entries: 
        full_path = os.path.join(path, entry) # for the full path name (not sure if correct)
        if entry.endswith('.png'): # make sure we only print the ones containing png
            print(entry, ",Path:",  full_path)
readFolderPrintPng('C:/Users/Emil/Pictures/ta');