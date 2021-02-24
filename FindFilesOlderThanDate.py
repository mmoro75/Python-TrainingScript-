# we are going to create a script to find files older than a specific date
import os
import sys
import datetime

age=1  # how many days we want to print files for
req_path=input("enter your path: ")
if not os.path.exists(req_path):
    print("enter an existing path")
    sys.exit(1)
if os.path.isfile(req_path):
    print("please enter a direcory path")
    sys.exit(2)
else:
    print("your path is invalid enter a valid path")

print(os.listdir(req_path))
today=datetime.datetime.now()    # today date
for each_file in os.listdir(req_path):
    each_file_path=os.path.join(req_path,each_file)
    if os.path.isfile(each_file_path):
       # print(each_file_path,datetime.datetime.fromtimestamp(os.path.getatime(each_file_path)))
           # function getatime gives you seconds when file is created and function fromtimestamp will convert to date
        file_creat_date=datetime.datetime.fromtimestamp(os.path.getatime(each_file_path)) # store file creation date in variable
     #   print("files and Date=" ,each_file_path,today-file_creat_date)  # print filelist and today date - file creation date and see difference
     #  print("file days= ",each_file_path, (today - file_creat_date).days) # print also how many days are the file there
        dif_days=(today - file_creat_date).days # store days creation minus today date in a variable
        if dif_days < age: # if dif days is minus than age variable print file
            print("search result= ", each_file_path,dif_days)
              # ifyou want to remove files older than 3 days use os.remove and use if condition
