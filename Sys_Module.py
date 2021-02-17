# sys module is used to worl with payton runtime environment

import sys

# print(dir(sys))
# print(help(sys))
# print(sys.path) # system environemtn path for python
# sys.exit() # stop python script

""" sys.argv it returns list ofcommand line arguments passed to a python script
 by running python scrip from command line "python yourscript.py enter your name" 
the extra information are called command line arguments  in order to pass them to your script  you need to use sys.argv"""

import sys
print(sys.argv)
# now run from command line python Sys_Module Marco 1 2 3" and observe the output
# you get the command line arguments in a list note that they are all strings and index 0 is always your script name
"""
prompt=input("Please enter your string")
action=input("how would you like to display your string : upper/lower or title format?")

if action=="upper":
    print(action.upper())
elif action=="lower":
    print(action.lower())
elif action=="title":
    print(action.title())
else:
    print("please enter a valid action upper/lower or title")
    """

# now let's rewrite this script in a non interactive mode by passing arguments with sys.argv and run from command line passing arguments

# ****** run from command line "pyton Sys_Module.py your string action"
import sys

if len(sys.argv) !=3: # for this script proper arguments are 3 ( 0 script name, 1 is desired string , 2 action)
    print("to properly use:") # instruction for the user
    print(f"{sys.argv[0]} <your required string>, <upper,lower,title>") #give user the instructions
    sys.exit()  # exit the script without error if the correct arguments are not passed

prompt=sys.argv[1] # argument 1 in index 1 is the string
action=sys.argv[2] # argument 2 in index 2 is the action ( always remember index 0 is script name

if action=="upper":
    print(prompt.upper())
elif action=="lower":
    print(prompt.lower())
elif action=="title":
    print(prompt.title())
else:
    print("please enter a valid action upper/lower or titl")