# access charaters in your strring pointing indexies"
a="Marco Moro"
print(a)
print(a[0],a[6])
# last characters is always -1#
print(a[-1])
# get from to characters #
print(a[0:5])
# length of a string
print(f"length of your string is: {len(a)}")
# concatenate 2 strings
b="gino"
c="latino"
e=" "  #to add a space#
d=b+e+c
print(d)
# String case cobversion #
a="String Convesrion"
print(a)
print(a.lower())
print(a.upper())
# print available operation for a string
print(dir(a))
# boolean with string
f="Moro"
print(f.startswith("M"))
print(f.endswith("oro"))
print(f.isspace())
# joints for strings
h="join"
j=" ".join(h)
print(j)
# centre
print(h.center(40))
print(f"{h.center(20)} \n{f.center(20)}")
# Zfill for strings
print(h.zfill(10))
#Strip (removes spaces left or right or any charachter if is start or end
y="   gino latino   "
print(y)
print(y.strip())
k="Aloahh"
print(k.strip("A"))
print(k.strip("hh"))
# Strip left or right
l="Marco Roma is not original Marco"
print(l.lstrip("Marco"))
print(l.rstrip("Marco"))
#miltiple stips
print(l.lstrip("Marco").rstrip("Marco"))
#Split it splits the string based on spaces and gives a list or splits based on given charachters
print(l.split())
print(l.split("is"))
# Count how many given characters are included in the string
print(l.count("is"))
print(l.count("M"))
#index
print(l.count("M",12))  # count from index 12
print(l.count("M",0))  # count from index 0
#find -1 result means value is not found in any index
print(l.find("M",12))  # find from index 12 and gives index position
print(l.find("M",0))  # find from index 0 and gives index position
print(l.find("Roma",0))  # find from index 0 and gives index position
print(l.find("x",0))  # find from index 0 and gives index position
# display string centre , left or right
# mode -gives you size of the row in windows terminal

'''
import os   #import module 
os.get_terminal_size()  
os.get_terminal_size().columns
os.get_terminal_size().row
print(os.get_terminal_size())
'''

