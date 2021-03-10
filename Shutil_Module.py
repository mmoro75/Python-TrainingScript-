# shutil module is a python integrated module and provide capabilities for operations on file and folders like: copy, move , remove

import shutil

print(dir(shutil))   # shutil module is more advanced than OS module for such operations

########## copy files or directories ################################

src="sorcefile"
dest="destfile"
shutil.copyfile(src,dest)  # providing source and destination will copy file from source to dest ( no premissions preserved)
shutil.copy(src,dest) # this operation will also copy file from source to destination but it woul also keep same permissions
shutil.copy2(src,dest)  # this operation will keep also metadata of your original file ( ex same permission and timestamp)
shutil.copymode(src,dest) # it will give permissions from source file to destinantion file ( it is a a copy permission not file content)
shutil.copystat(src,dest) # it will copy metadata from source file to destination file ( it is a metadata copy not file content)

fo1=("filename1","r") #open file in read mode
fo2=("filename2", "w") # open file in write mode
shutil.copyfileobj(fo1,fo2)  # copy content file 1 to file 2 with shutil function

dirsrc="directory to copy"
dirdest="destination directory"
shutil.copytree(dirsrc,dirdest) # it will copy entire directory structure into source directory (including permissions and metadate)

shutil.rmtree(dirdest) # it will remove all the direcotry tree



