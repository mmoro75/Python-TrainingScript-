# by using the for loop we want to find all the files in a directory with given extension and create a list

import os
import sys

path=input("enter your path: ")
  #you could also create another if check to see if the paath is empty or not or if the path is valid of file but this is optional
if os.path.exists(path):
  ext = input("please provide your file extension: ")
  print(os.listdir(path))   # print list of all your files in the given path
  my_file_List=os.listdir(path)
  Files = []  # define an empty list for your files outside loop
  for each_file in my_file_List:
         if each_file.endswith(ext):
          Files.append(each_file) # add your value in your list
  if len(Files)==0:    # if length of your list is 0 meaning empty print the satement
           print("there are no files with the given extension in your path")
  else:
     print("the list ofyour file is:", Files)
     print("there are:", len(Files),"file with", ext, "extension")

else:
  print("your path is not valid!")


