# OS module allows you to interact with your operating system and automate tasks like create/remove directory and more

import os

# print(dir(os)) -  available functions
# print(help(os)) -  documentation

print(os.getcwd()) # get current work directory
os.chdir("c:\\Users\\u6017127") # change directory remember in windowsalways \\ separator for paths some \n \u are special charachters
print(os.getcwd())
os.chdir("c:\\Users\\u6017127\\PycharmProjects\\AutomationTraining.py\\venv")
print(os.listdir())  # print list directory output is a list
# print (os.listdir(path)) you can provide path is required
# os.mkdir("c:\\Users\\u6017127\\Documents\\GinoLatino") # create directory
# os.rmdir("c:\\Users\\u6017127\\Documents\\GinoLatino") # remove direcotry
# s.makedirs("c:\\Users\\u6017127\\Documents\\Aloah\\day1")  # create directory and subdirectory
# os.removedirs("c:\\Users\\u6017127\\Documents\\Aloah\\day1") # remove direcotry and sub directory
# os.rename(source, destination) rename
#print(os.environ) # get environmet info
# print(os.getuid())  # get user id
print(os.getpid())  # get process id

# OS.PATH submodule it is used to workon paths

print(dir(os.path))
print(os.path.sep) # separator for your operating system
path="c:\\Users\\u6017127\\PycharmProjects\\AutomationTraining.py\\venv"
print(os.path.basename(path)) #basename last part of your path
print(os.path.dirname(path))  # path name till basename
# os.path.join(path1,path2) to join 2 paths together
print(os.path.split(path)) # get path head and tail ina tuple
print(os.path.getsize(path))
print(os.path.exists(path)) # to see if exist result in boolean
print(os.path.isdir(path))  # see if path is a directory result in boolean
print(os.path.isfile(path)) # see if ptah is a file result in boolean
print(os.path.islink(path)) # to check if it is a link or not result in boolean

# OS.System function to execute operating system commands

print(os.system("dir")) # the output will be displayed on the screen alongside execution code 0=command sucesfull any other code command failed

# if you assign the execution to a variable only execution result will be stored and you can determine if the result is good or not

cmd_res=os.system("dir")      # in this example the command is executed

if cmd_res ==0:
    print("your command is executed ")
else:
    print("Your command failed")

# OS.WALK(path) it is used to generate file and directory in a direcotry tree by walking ( for example find a file it will find on given path and all sub directory )

path1="C:\\Users\\u6017127\\Documents\\Eikon\\Project\\LSE Maintenance Release"
print(list(os.walk(path1)))
'''
to understand the concept we are going to generate a list for the given path
 result will give a list containing a tuple the tuple contains 3 values each value is a lists: 
 1) your path 
 2) list of direcotris in your path 
 3) list of files in your direcotry
 
 for each sub directory for the given path it would generate another tuple with same values 
 and so on to cover up all the direcotry and files
'''

# you can separate the tuples with a for loop

print("---------------------------------------")

for each in os.walk(path1):
    print(each)       # result would separate tuples and give it in separate lines ( see output )

print("now I want to get list separated")

for root,dir,files in os.walk(path1):
    if len(path1) !=0: # i want to exclude empty paths
      # print(root,files)  - I am separating roor path and files in 2 variables and prin them
      print(files) # print just files

print("now I want each file with his path printed out")

for root,dir,files in os.walk(path1):
    if len(path1) !=0: # i want to exclude empty paths
      # print(root,files)  - I am separating roor path and files in 2 variables and prin them
      #print(files) # print just files
      for each_file in files:
           print(os.path.join(root,each_file))  # now print root and each file associated