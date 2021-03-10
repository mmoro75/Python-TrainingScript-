# Function is a specific code for a specific operation - it can be reused multiple times in your comde based on requirements
# a Funtion is executed only when it is colled

# how to define a function and how to use it

def display():  # keyword def is used to define your function
# function name is only letters or numbers ( not special charachters)
# function name cannot start with numbers or special char
# do not include any space in function name
    print("this is my display function")
    print("first line of code")
    print("second line of code")
    return None # it is good practice to set up retun null if you are not returning any value

display() # to call your function just use its name (remember to define the function in your sequence before it is called)

# functions are for code reusability
# code mudularity ---->  try always to write your code logic as a function and re use it for your scripting
# ----------there are 2 types of Fucntions
# *Built in Functions - Functions that are included in python (buit-in)
# *User Defined Fucntions - Functions that you create besed on your requirements

#################### Call a Function from another finction and scope of variables ######################################

def myfunction1():
    # local variable#
    name="Marco" # variable inside a Function are local and can only be accessed inside (name won't be accessible from myfunction2)
    print("wlecome",name)
    myfunction2() # you can call function 2 inside fucntion 1
    return None
def myfunction2():
    print("thank you",x)
    return None
#global variable#
x=10 # variable outside the functions are global and can be accessed (define thevariable before calling the function)
myfunction1()

# to write your code all into fucntions it is good practice to start with a main function
def main():
    global x # to make the variable from your manin global
    x=22
    print("my exectution start from main")
    myfunction1()  # your code now will start here by calling function main
    return None
main()

# passing arguments in Functions - Argumens and Parameters

def get_sum(value):
    # The funcion expect to pass a value for the sum and the variable value is called parameter/positional argument
    # and it would sotre the value you pass as an argument
    sum=value+10
    print(f"the result is: {sum}")
    return None
def main2():
    # global num # unless specified is not good to make varible global in your main
    num=eval(input("give me your number: "))
    get_sum(num) # the variable is passed to your get num as an ARGUMENT
    return None
main2()

############# Argeuments and Return value with a Function #####################

def get_sum(c,d): #arguments value are stores in parameters c,d to be used in the function
    result=c+d
    return result # the variable result is returned and it is now accessible to our main function to be printed
    # issue return !=none whwnever you want to access function result somewhere else
def main3():
    a=eval(input("give me your number: "))
    b=eval(input("give me your number: "))
    get_sum(a,b) # the variables a and b is passed to your get num as an ARGUMENT
    sum=get_sum(a,b) # you are stroring the result in sum of the get_sum function by returing the result in the fucntion itself
    print(f"the result is: {sum}") # sum value now is available and it can be printed out
    return None
main3()

################### Function with default Arguments ################################

def add_number(a,b=0):  # note function needs 2 arguments to be executed however we are assining defualt value for b
      # remember default value is position dependent assigning a=0,b is not working as if you pass 1 argument it will always be for a
    result=a+b
    print("the result is:",result)
    return None

add_number(5,6) # function requires to arguments to be passed to get result
add_number(4)  # in this case we can still print the result as we can use default vaule for b
# add_number() # it will give an error as at least a argument is needed

# user for server example

def serv_user_login(user="root"): # defailt user is root for your server
    print("I am logging in as: ",user)
    return None

serv_user_login("mmoro")
serv_user_login()  # it sould give default user

########################## KeyWord based Argument #################################

def display_value(a,b): # remember this a position based argument whoever is passed first get a and sencodn gets b
    print(a,b)
    return None

display_value(a=4,b=3) # we can force the value of the variable to be as we want not depending on position
display_value(b=6,a=8)

##################### variable lenght argument #########################

def display_type(*arg): # *args get n number of argument
    # print(type(arg)) # this result is always a tuple
    for each in arg:  #use for loop to get type of each value in the resulting tuple
        print(type(each))
    return None
display_type()
display_type(1)
display_type(1,2,"dir")

############################  function with variable keyword argument #####################################

def key_val(**karg): # this syntax will give you result of key and value dictionary
    print(karg)  # you basically have a dictionary available in your function based on n number of values from arguments
    return None
key_val(a=1,b="marco",user="root")