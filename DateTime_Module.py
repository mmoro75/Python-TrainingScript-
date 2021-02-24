# Datetime module buil in in python it to work with date an time

import datetime
print(dir(datetime))  # for abailable operations in
# print(help(daytime)) # for ducumentation

print(datetime.datetime.now())  # get time now
print(datetime.datetime.today()) # today datetime both this operation will give time based on your timezone set in your host

# we can also get only the info we need
print(datetime.datetime.now().day)
print(datetime.datetime.now().hour)
print(datetime.datetime.now().month)   # we can store this information in variables

# with the help of string format time we can build the infor we need about dates and time

print(datetime.datetime.now().strftime("%y-%m-%d")) #  print year month day example
print(datetime.datetime.now().strftime("%Y-%M-%D")) # capitalletter will give 4 digits output

# use this website "https://strftime.org/" to find out meaning about each letter

import pytz # by importing this submodule now you can get time for any zone not just your host ( import with pip )
print(dir(pytz))
ist=pyt.timezone("Europe/Rome")
print(datetime.datetime.now(ist)) # by passing this object you can get that timezone

