# develop a script to find for a specific file in your entire system ( operating systenm independent)

"""
### mini script tofind a file in a location ##

import os
req_file=input("please enter filename you want to search")
sys_path="C:\\Users"  # i am just looking in C for non in windows
for root,dir,files in os.walk(sys_path):  # i am separating with walk root, dir and files
    for each_file in files:       # I want to print each file for the given path ( system path for this requirements)
        if each_file==req_file:  # if statement to print just given file
          print(os.path.join(root,each_file))  #print given file with his path


"""

# note with linux operating system to identify your entire sysemt "/" would do for windows you need to use drives ie "C:\\"

# for multiple drives you couls use this logic

import string
import os
import sys
import platform

req_file=input("please enter filename you want to search: ")
print("operating systmem you are using is:", platform.system())
if platform.system()=="Windows":
   drivers_names=string.ascii_uppercase    # get all the letters capitals and lower
   myDrivers_names=[]
   for each_drive in drivers_names:
     if os.path.exists(each_drive+":\\"):  # with if statement print the drives that exist in your system
        print(each_drive)
        myDrivers_names.append(each_drive+":\\")
   print("drivers available in this machine",myDrivers_names)

# now loop into each drive to find your file

   for each_drive in myDrivers_names:      # now for each available drive loop to find your file
     for root,directory,files in os.walk(each_drive):
        for each_f in files:
            if each_f==req_file: # if condition to print just required file
              print(os.path.join(root,each_f))   # print file and path

else:   # block of code for linux
    for root,directory,files in os.walk("/"): #entire operating system in linux
        for each_file in files:
            if each_file==req_file:
                print(os.path.join(root,each_file))


