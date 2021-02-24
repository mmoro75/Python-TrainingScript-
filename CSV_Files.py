# how to deal with CSV Files - ( CSV = comma separated values) used to store table separated data (rows and columns)

# to read or write on your CSV file you need to import defualt module CSV

import csv

# read your CSV  file

my_csv="C:\\Test\\Files\\Table.csv"

fo=open(my_csv,"r")   # I am opening file in reading mode
content=csv.reader(fo)  # i am using csv reader to print the lines to get output in colimn otherwise with simple file reader I will get a string
# you can also specifiy a delimiter if different of coma "content=csv.reader(fo.delimiter="yourdelimiter")
for each in content:
    print(each)

fo.close()  # remember to always close the file at the end

# lets see how to get just the header and see how many rows are in the file


fo=open(my_csv,"r")   # I am opening file in reading mode
content=csv.reader(fo)
#print(list(content)) # it will print your content in a list ( cotaining sublists of each row)
# first row is always first row
print(f"your header is\n: {list(content)[0]}") # it will print index 0 = first row
#print(next(content)) # you could use the defualt operation next it will print the first line as initially the cursor is at first position in the file
# with the function next you also send curson to ext line and then you can print the remaining of csv rows
#print("the number of rows in the file are:" len(list(content))) #to kow how many lines are in the file just print length of the list of content variable that sotres your fi
#header=next(content)

for each in content:
    print(each) # it will print remaining lines

fo.close()

# creating a csv file
new_table="C:\\Test\\Files\\new_table.csv"
fo=open(new_table,"w",newline="") # open file in write mode ( newline="" empty will get rid of empty lines when creating lines)
writer=csv.writer(fo) # use the function csv writer to write in my opened file fo (if you want to specify another delimiter "csv.writer(fo.delimiter="yourdelimiter")
# now if you want to store data into your file the format is a list for each row with coma delimiter (unless delimiter is different)
writer.writerow(["number","name","addres","telephone"]) #use writerow to insert data in first row as a list (remember coma in list is not the delimiter)
writer.writerow(["1","Marco","stree1","07595234555"])
# to write more rows togheter use the writerows and provide list oflists
writer.writerows([["2","Stefan","Stree2","099876699"],["3","Gino","Street3","0099887766"],["4","Maik","Street4","646535838"]])

fo.close()
