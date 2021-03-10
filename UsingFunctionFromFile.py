# lets see how to re-use Functions defined in another python scrip file
# import Functions  # I am importing all the functions defined in Functions script

# Functions.display_type("Gino") # now I can access the functions from the other script and just call them up
# notice python will execute all the code from Functions script

#  you are not suppose to execute code in Functions scrip however python will execute all script 1 first
# it is good practce to run the code always from a main fucntion in every script and execute from main
# in each script make sure with if statements you are running from sript itself not from another if "__name__=="__main__: then execute main

import MarcoFunctions as f  # it will execute script MarcoFunctions ( no output in our execution this occasion as if name is no longer main

def main():
    f.get_sum(1,2) # I am executing imported function from MarcoFunctions
    result=f.get_sum(1,2)
    print(result)
    return None

if __name__=="__main__":  # it will prevent to run code from MarcoFunctions
    main()

""" this structure is aways applicable when writing pytong script
1) import whatever you want to import
2) main to execute the script
3) if __name__=="__main__": 
    main()
"""
