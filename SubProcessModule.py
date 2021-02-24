# Subprocess Module is useful to execute operating commands on your system (default module in python)

'''
note even "os.system("dir") can execute commands on your system however you cannot store results in variables like:
a=os.system("dir") -----> result is always a print out and not stored it will only store 0=command executed or 1=command fail
'''

import subprocess

"""
# with subprocess you can run command and store in variables the result

sp=subprocess.Popen(cmd,shell=True/False,stdout=subprocess.PIPE,stderr=subprocess.PIPE,universal_newlines=True) # syntax to run command
# if your command is astring you have to set shell=True (cmd="dir")
# if not and it is a list for example you nee to set shell=False (cmd=["ls -ltr","dir","pwd"])
#universal_newline=True to get result as a string as oppose to bytes ( by default result is in bytes
rc=sp.wait()  # set wait time for command to execute and store result to variable rc ( if 0 success if 1 fail)
out,err=sp.communicate()  # store result in 2 varibale out or error
print(f"the output is: {out}")  # print output result
print(f"Error is: {err}") # print errorresult
"""

cmd=input("provide the command you want to run: ")
sp=subprocess.Popen(cmd,shell=True,stdout=subprocess.PIPE,stderr=subprocess.PIPE,universal_newlines=True) # syntax to run command note shell=True
rc=sp.wait()
out,err=sp.communicate()
print(f"the command fails code is {rc}") # print error code
print(f"the output is: {out}")
print(f"Error is: {err}")
# if you need the result as list you can use splitlines
print(f"Command Reuslt in List is: {out.splitlines()}")


##### FOR WINDOWS ALWAYS USE SHELL=TRUE AND COMMAND AS STRING###

''' note this block ofcodewon't work on windows######
cmds=input("provide list of commands you want to run: ")
cmds.split() #convert your command to a list or pass the command as a list directly
print(type(cmds))
sp=subprocess.Popen(cmds,shell=False,stdout=subprocess.PIPE,stderr=subprocess.PIPE,universal_newlines=True) # shell=fale to run list of commands
rc = sp.wait()
out, err = sp.communicate(
print(f"the command fails code is {rc}")  # print error code
print(f"the output is: {out}")
print(f"Error is: {err}")
# if you need the result as list you can use splitlines
print(f"Command Reuslt in List is: {out.splitlines()}")


# raccomandation is where you are working with environment variables pass command as a string and shell=True othervise pass command as a list and shell=False
# shell=true open a shell and program is havier and slower. so simple commadn pass as command as List
'''

# using Sub Process find Java version on your system

cmd_java=input("enter command to find Java Version: ")
sp=subprocess.Popen(cmd_java,shell=True,stdout=subprocess.PIPE,stderr=subprocess.PIPE,universal_newlines=True) # shell=fale to run list of commands
rc = sp.wait()
o,e = sp.communicate()
if rc==0:
    if bool(o)==False and bool(e)==True:  # this if statement make you print the error message for sucesfull command as bool of o is False
      print(f"your result is: {e.splitlines()}")  # java command output is only for error messagge
else:
    print(f"your command fails with error {e}: ")

for each_line in e.splitlines():
    if each_line.startswith("java version"): # or if "version in each_line: or you can combine if "version" in each line and "java" in each_line:
        print(each_line.split()[2].strip("\"")) # print only index 2 of each line converted in list to get only java version
        break                      # strip will remove also the quatation in your otput

