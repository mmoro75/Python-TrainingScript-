# for loop will iterate for the number of time for the given value

'''
syntax

for "any variable" in "value" *** valus can be any from list,Tuple, Dictionary, total number of iterations depends on number of indexes
'''

# read a path and identify all the directories and path in the given path
import os
import sys

path=input("enter your path: ")
if os.path.exists(path):
  print(os.listdir(path)) # print the list of the files in your directory in a list
  my_file_List=os.listdir(path)
  for each_file in my_file_List:   # for loop will store in "each" variable the number of values for the number of values stored in indexes of the value you provided
     files=os.path.join(path,each_file)    # for loop will "Iterate" and execute the block of code underneath fot the numer of time for the given value then exit:
     if os.path.isfile(files):   # value can be any: String , List , Tuple , Dictionary ect ect ( in this example is a list)
         print(files, "is a file")
     else:
         print(files,"is a directory")


else:
  print("your path is not valid!")
 # sys.exit()

# use for loop to print a string and corresponding index
string=input("provide a string: ")
index=0 # give a reference value foryour variable to take at first iteration(this variable has to be defined before the loop)
for each in string:
    print(each.index(each))
    print(each,"--->",index)
    index=index+1  # increase index number +1 every iteration


# for loops with Dictionary, tuple, list

tu_list=[(1,2),(4,5),(8,9)]   # list contians tuple as values ( it could also be a list containing other lists)

for each_value in tu_list:
    print(each_value)   # with this loop you are unpacking the list and variable each value will get the tuple

for fr,sd in tu_list:  # by assigning 2 variables in the for loop you can unpack the tuple values and print them out separatley
    print(fr)  # print only first value of tuple
print("-------------------------")
for fr,sd in tu_list:
    print(sd)  # print second value of tuple

#this scenario is very important when working with disctionary

my_dic={"0:1","2:3","4:m"}

for each_item in my_dic:
    print(each_item)  # in this scenrio with a single variable you are going to get only key values ofyour dictionary

for key,value in my_dic:
    print(key,value)  # with 2 variables you can get key and value in your dictionary ( or print them separatley)
