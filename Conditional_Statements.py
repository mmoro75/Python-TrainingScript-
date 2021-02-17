# if is called simple conditional statement use to control the execution of set of lines or block of code

'''
if expression:
   statement1
   stetement2

   you can use
   -comparison operators
   -identity operators
   -memebership operators
   -logical operators

'''

# if and Else conditional statement to be used only if the conditions are 2 yes or no

my_string=input("do you want your number in letter? please enter yes or no:")

if my_string=="yes":
    print("your number will be converted in letters in the next scrip")
else:
    print("thank you for your time")





# for multiple conditions the option is using "elif"  - else if

print("we are going to conert number in range 1 to 5 in letters")
a=eval(input("enter your number 1 to 5:"))

if a not in [1,2,3,4,5]:
  print("number out of range")
elif a ==1:
  print("one")
elif a ==2:
  print("two")
elif a ==3:
  print("three")
elif a ==4:
  print("four")
else:
  print("five")


# to optimize the code and print the number in letter you could use dictionary

print("we are going to conert number in range 1 to 5 in letters")
a=eval(input("enter your number 1 to 5:"))
num_dic={1:"one",2:"two",3:"three",4:"four",5:"five"}   # define dictionary value-keys

if a not in [1,2,3,4,5]:
    print("number out of range")
else:
    print(num_dic.get(a))   # use grt to print value of given key