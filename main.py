import os
import shutil
dirname = input("enter the file you want to sort: ")
li = os.listdir(dirname)
listOfSat = ("SAT","New","mock")
for i in li:
    fileName, extension = os.path.splitext(i)
    extension = extension[1:]
    filespli = fileName.split(" ")[0]




    #if extension == "":
       # continue
    #if filespli in listOfSat:
        #shutil.move(dirName + "/" + i, dirName + "/SAT" + i)
    #else:
        #continue



    if os.path.exists(dirname + "/" + extension):
        shutil.move(dirname + "/" + i, dirname + "/" + extension + "/" + i)
    else:
        os.makedirs(dirname + "/" + extension)
        shutil.move(dirname + "/" + i, dirname + "/" + extension + "/" + i)
    print(fileName)



