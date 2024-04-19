# first of all I want to say, fuck Python

import os

contains = input("File contains: ")
dir = input("Directory or Folder path: ")

directoryList = [dir]
cursor = 0

def deleteFiles() :
    for directory in directoryList:
        files = os.listdir(directory)

        for f in files:
            filepath = dir + '/' + f
            if(os.path.isdir(filepath)):
                directoryList.append(filepath)
                deleteFiles()
            elif contains in f:
                os.remove(filepath)
                print('Deleted '+f)


    

print(directoryList)