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
if __name__=="__main__": # it will execute the code only if running from this script. it execution comes from anothe script it won't as var name won't be main anymore but scriptname
   main3()