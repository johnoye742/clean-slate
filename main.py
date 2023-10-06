import os

contains = input("File contains: ")
dir = input("Directory or Folder path: ")

files = os.listdir(dir)

for f in files:
    filepath = dir + '/' + f
    if(os.path.isdir(filepath)):
            li = os.listdir(filepath)
            for f1 in li:
                filepath = dir + '/' + f1
                if contains in f1:
                    os.remove(filepath)
                    print('Deleted '+f1)

    if contains in f:
            os.remove(filepath)
            print('Deleted '+f)