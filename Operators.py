# Arithmatic and Assignment Operators - bot input and output is a value
'''
+ - addition operator
- - minus operatior
* - moltiplication operator
/ - division operator
%  - modulo operator - gives the reminder for the operation
// - floor division ( rounds the number divided )
** - power of  operaror exponenatial
=  - assign operator
'''

# #Comparison , Identity and Membership Operators - input value output boolean True or False

'''
> - greater than 
< - less than 
== - equal 
!= - noteqal 
>= -  greater or equal to
<= - less or equal to 
'''

# to compare strings find out the ASCII code assigned to each letter with "ord("anycharachter") or "chr("anuwalue") it then compares characted by charater for the given strings


#~~~~~~~ Logical operators - input Boolean output boolean true or false ~~~~~~~~~~~~~~#

#identity  is used to find typpe of variable Class/object/type

x=6.5
print(type(x))
y="marco"
print(type(y))

print(type(x) is type(y))
print(type(x) is not type(y))

# Membershipoperators are to validate the membership of a value

allowed_age=[41,42,43,44,45,46,47,48,49]
your_age=eval(input("how old are you?"))

if your_age in allowed_age:
     print("you are allowed to enter")
else:
     print(" you are not allowed to enter ")

# not even not in can be evaluated


# ~~~~~~~~~~~~~~~~Bitwise operators - both input and output is value but output is in binary ~~~~~~~~~~~~~~~~~~~~~~~#

#useful to combine multiple conditions

print(3>4 and 1 in [1,2,3])  # and both the conditions have to be true

print(3>4 or 1 in [1,2,3])  # at leat one condition has to be true

print(not 1 in [1,2,3]) # not fo true will give false and not of false will give true
print(not 4 in [1,2,3])

print(all([2<3,4<5,5<6,6<7,7<8]),"all is true") # with all you can club all the contitions together without repeating and operator
print(any([2<3,4<5,5<6,6<7,7<8]),"all is true") # with any you can club all the contitions together without repeating or operator

print(not all([2<3,4<5,5<6,6<7,7<8]),"all is true")  # even not all or not any can be used 
print(not any([2<3,4<5,5<6,6<7,7<8]),"all is true")