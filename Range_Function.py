# range() function is python built in function to generate integers as a list

# examples
# syntax is range(start,stop,step) - single value is stop last and defailt value is 0
print(range(5))        # display stop and start value
print(list(range(5)))  # in python 3 you need to use also list funcion

print(list(range(3,60,3))) # in this example for pyton 3 gives a list starting from 3 step by 3 till max-step number

print(list(range(60,0,-2))) # example to obtain the reverse see step is minus and stop is lower than start

# your range number is iterable in a for loop

for each in range(4):
    print(each)

# with the help of range you can find index value for your list without counting

new_list=[1,5,7,"gino","marco"]

print(list(range(len(new_list))))  # in the example total indexes are 4

# now with the help of for loop let's print all the value for each index in my list

for each_index in range(len(new_list)):
    print(f"index ---> {each_index} value= {new_list[each_index]}")





