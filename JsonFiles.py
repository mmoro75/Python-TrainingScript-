# working with Json files in python (javascrip objet notation) commonly used to represent structured data

import json # default module in python

# remember for python {} delimiter are dictionaries in JSON files content in {} is an objet

# read content in json file

myfile="C:\\Test\\Files\\jsonFileSample.json"

fo=open(myfile,"r")  # open file fo in read mode
print(json.load(fo)) # to print out data in python format use json.load for your fo file and you will get data in dictionary format
# now you can use the dictionary opetations with your data like json.load(fo).get() etc etc

fo.close()


# write content in jason file ( remember to wirte in your json file data has to be passed as dictionary format)
myfile2="C:\\Test\\Files\\jsonSkills.json"

my_dictionary={"name":"Marco","skills":"[aws,python,qa,html]"} # sample data in dictionary formato to pass to json

fo=open(myfile2,"w")  # open file fo in write mode
json.dump(my_dictionary,fo,indent=4) # to write into the file you use the fuinction dump and you include your data in dictionary format
# by default you won't get indentaion it has to be specified in this example 4 spaces
fo.close()