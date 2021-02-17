# to use for getting information about your undelying howrdware and component (architectural information)
import platform

# or import platform as pt
# print(dir(platform))   # to get all the available functions for module platform
# print(help(platform))  # print platfomr module documentation
print(platform.system()) # operating system
print(platform.processor()) # processor
print(platform.python_build())
print(platform.platform()) # multiple information
print(platform.architecture())
print(platform.node())


# Getpass module - it helps gettin user and password from user in a secure manner


import getpass

# print(dir(getpass))
# print(help(getpass))

print(getpass.getuser())     # get userid from environment variables
my_pass=getpass.win_getpass() # promptuser for password in windows in secure way
print("my passwod is:", my_pass) # print password
my_pass(getpass.getpass(prompt="give me your db password:")) # to customize prompt 
