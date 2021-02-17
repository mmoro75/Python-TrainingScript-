# Lists - [] (list as oppose to strings are mutable)
my_list=[3,2,"Marco",5.6]   #list structure
print(my_list)
print(my_list[2:3])    #print list from an indet to another
print(my_list[2][0])   # print list index and access specific index of internal string
my_list[0]=4           # change a list value based on index
print(my_list[:])
dir(my_list)
print(my_list.index(2))  # to find a values  in the list and see whic index is stored ( for multiple values use indexs sub chunck)
print(my_list.count(2))  # count how many times the vaules is in the list
# my_list.clear()   # clear the entire list
my_new_list=my_list.copy()  # to create a copy of your list in anotther memory allocation
my_new_list.append(12)  # append value
print(my_new_list)
my_new_list.insert(1,55)  # insert  value 55 based on index position 2
print(my_new_list)
my_list.extend(my_new_list) # to extend to list with values from another list
print(my_list)
my_list.remove(12)   # remove a specific value in the list
print(my_list)
my_list.pop(2)       # remove value in index 2 in the list
print(my_list)
print("new operations")
print(my_new_list,"original")
my_new_list.reverse()   # reverse list order
print(my_new_list,"reversed")
my_new_list.pop(2)
my_new_list.sort()      # sort list in ascending order
print(my_new_list,"sorted")
print(bool(my_list))    # convert full list to boolean gives true empty list gives false
my_empty_list=[]
print(bool(my_empty_list))
print(len(my_new_list),"lenght of my list")

#Tuples - () ( tuples are immutable - operations are notpermitted - only the entire data is, like delete and recreate)
my_tuple=(3,2,5,[1,2,3])  # tuple containing a list
my_tuple0=()
print(bool(my_tuple0))
print(my_tuple[3][1])  # access sendo index in tuple list based on tuple indexes
print(len(my_tuple),"lenth of my tuple ")
#Dictionralies - {} with key value pair
my_dict={"fruit":"apple","car":"ferrari",2:"two",1:1}
print(my_dict["fruit"]) # acces value by key
print(my_dict.get(2))  # get value from key
my_dict["country"]="Italy"  # add value in dictionary based on key ( if no exist will be created if existing willbe changed
print(my_dict)
print(my_dict.keys())   #print keys
print(my_dict.values())  #print values
print(my_dict.items())   #print items

x=my_dict.copy()  # create a copy in new memory location
print(x)

new_dic={"name":"gino"}
my_dict.update(new_dic)  #update dictionary with another dictionary
print(my_dict)
my_dict.pop("name")  # remove key pairs value

keys=[1,2,3,4,5,6]
my_key_dic=dict.fromkeys(keys)  # create a new dictionary from keys
print(my_key_dic)

#Sets - {}  - set gives the data in ascendind orderand remove duplicates

my_set={8,4,5,7,8,3,3,4,2,0,3,3}
print(my_set)
new_set={9,1,3}
list=[1,7,5,3,3,4,9,2,2,9,9]
print(set(list),"set list")   # convert list into a set

print(my_set.union(new_set),"union")   # unions
print(my_set.intersection(new_set),"intersection") # intersecion


