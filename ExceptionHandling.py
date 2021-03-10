# how to handle excpetion in python - an exeption is an error in your cade that will stop the execution

""" errors are 2 types 1) syntax error 2) runtime errors ( example dividing by 0, file not present,index out of range or import error etc)
syntax errors cannot be handled instead runtime errors can be handled """

# example with no existing file
"""
fo=open("File.txt") >>> File "C:/Users/u6017127/PycharmProjects/AutomationTraining.py/venv/ExceptionHandling.py", 
this command gives an error as file do not exist, to handle this runtime error you need to use "try,except" the code is:"""

try:                      # try to run this block of code
    fo=open("file.txt")
    print(fo.read())
    fo.close()
except Exception as e:   # if there is an exception print error
    print(e)    #  >>>>> [Errno 2] No such file or directory: 'file.txt'


# exception handling for known errors "NameError","Type Error","FileNotFoundError","ZeroDivisionError"

try:
    print(a)
except NameError:   # we can handle exception this way as we know that in case varible a do notexist the error is NameError type
    print("variable not defined")

try:
    print("no error on this line")
    import fabric  # remember whenever getting exception the rest of code in try block will not execute
    print(4/0)
except ZeroDivisionError:   # we can handle exception this way as we know that in case varible a do not exist the error is ZeroDivisionError type
    print("you cannot divede by 0")
except ModuleNotFoundError:   # we can handle exception this way as we know that in case module a do not exist the error is ModuleNotFoundError type
    print("your module do notexist")
except Exception as e:  # you can add extra layer in case of any other not predictable error ( this line always at the end as the execution is sequential
    print(e)
finally:
    print("this code will always execute")  # you can use finally module to run additional code , the code in finally will always execute after try catch


# Try Execpt else and try except and finally error handling differencies

try:
    print("there is no error in try block")
    # print(a)  #if you cause an exeption in try block else will not execute
except Exception as e:
    print(e)
else:
    print("this block of code will execute only if no error in try block")  # as oppose to finally that is always executed

########################## Raise user defined Exeptions   ###############################################

# what is custome exeption - it is errorcreated by user to display an error, it can be created with "rise" and "assert"

# raise = to raise an existing Excpetion when we want

"""raise Exception("this is an exeption")"""

# to use in real time let's write an if condition if flase instead of print I want to raise an exception and stop the code

age=34
if age<33:
    print("the age range is correct")
else:
    raise ValueError("the age is not in the defined range")  # raise an exception and stop the code

# Assert = to create an AssertionError - assert will raise exceltion if condition is false

assert(1>5)  # condition is false AssertError is created and code will stop

try:
    assert(1>5)
except Exception as e:
    print(" the error is: ",e)
