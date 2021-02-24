# while loop it is useful to repeat untill a condition is true and then stop when condition is false
'''
while True:
    print("monitor the machine")  # this is an example of infinite loop as the condition for while is always true
'''

# now we want to see scenarios where we need to stop by using while
value=10
while value<=100:  # loop will stop once get to 100
    print(value)
    value=value+2  #increase value by 2 each iteration

# for while and for loop you can use some conditions like: continue,stop and pass

for each_value in [1,2,3,4,5]:
    print(each_value)
    break # break will stop your loop ( in this example you are getting only 1 iteration)

for each_value in [1,2,3,4,5]:
    print(each_value)
    if each_value==3:
        break # break will stop your loop ( in this example you are stopping when getting value 3)
        #once your condition is true the loop will stop and won't iterate fully as it is not needed

for each_number in range(1,20):
    if each_number==7:
        continue     # if the above condition is true the remaining block of code in the if condition is skipped
        print("next number")
    print(each_number) # note this print statement is outside the if condition and will be executed every iteration

# pass will simply skip where you are suppose to get an error

while True:
    pass  # no error is displays but simplu pass ( block of code was expected