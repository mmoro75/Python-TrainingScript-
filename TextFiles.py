# working with text files with Python

# create new file - remember whenever you open a file in write mode the data will always be created from 0
# as new file is created with the provided content included
fo=open("C:\\Test\\test_file.txt","w")  # to create a file you need to use w=write mode
# fo.close()  # close will save the file automatically
print(fo.mode) # to print in which mode your file is open w=write, a=append, r=read
print(fo.readable()) # boolean result ( in this case it is False as the file is open in writing mode
print(fo.writable()) # True in this case
fo.write("this is a test file first line\n") # to write content in your file  ( cursor position start from 1st line position 0)
fo.write("New content in second line") # to go to next line \n
fo.close()

my_content=["test 1\n","test 2\n","test 3"]
fo=open("C:\\Test\\Files\\list file.txt","w")
fo.writelines(my_content)  # i can use a list to write my content in file with writelines function
fo.close()

my_content=["test 1\n","test 2\n","test 3"]
fo=open("C:\\Test\\Files\\loop_file.txt","w")
for each_line in my_content:
   fo.write(each_line+ "n")  # i can use loop towrite in my file each line
fo.close()

# add content to file ( open file in a mode a= append) it won't disrupt existing data
# note append mode and write mode if file is not there are same but if file exist
my_content=["test 1\n","test 2\n","test 3"]
fo=open("C:\\Test\\Files\\loop_file.txt","a")  # im appendmode you will include the data from existing file
for each_line in my_content:
   fo.write(each_line+ "n")  # i can use loop towrite in my file each line
fo.close()

# read content from file ( open in r mode r=read)
fo=open("C:\\Test\\Files\\loop_file.txt","r")
print(fo.read()) # to read data in your file
file_content=fo.read() # store the content in a variable
fo.close()

# read line each line using loop
fo=open("C:\\Test\\Files\\loop_file","r")
file_lines=fo.readlines() # you will get list of coontent in your file ( each line a new element in the list
# now with for loop I want to read first 2 lines I am using index
for each in range(2): # I am using range
    print(file_lines[each])  # I am using variable each to read index in file lines ( remember file_lines is a list)
fo.close()


#### copy content from a file and copy to a new file ###############

source_file=open("C:\\Test\\Files\\sourceFile.txt","r") # open in read mode to get the content
source_content=source_file.read()  # read content from source file and storein cource content variable
source_file.close()

dest_file=open("C:\\Test\\Files\\myDest_File.txt","w")  # open in write mode to copy the data from source
dest_file.write(source_content) # write content from source file into dest file
dest_file.close()

""" 
if would be good to give provide path from sorce adn destination to be clear where you want to pick up and save the files
default location is where you are

path_file=open("c:\\path.txt","w") # safe option is to provide path always to avoid mistakes

remmeber if you do not provide any mode the default is read mode
"""