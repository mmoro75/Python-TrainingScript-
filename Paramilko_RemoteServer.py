# paramiko python module is usefull to work with linux remote server ( to use this module on your local machine you shpuld have ssh2 )
# paramiko mudule establish an SSH2 conncetion wil remote server and by then you are allowed to execute command, upload/downlod files and so on


import paramiko   # piramiko is not defual module it has to be installed with "pip.exe install paramiko"

"""
paramiko module use two ways to establish connection with remote server 
   - username and password
   - user name and cryptographic key
   
we can connect Linux/Windows  <-> Windows/Linux
"""

########### Linux to Linux ###################################

# check if you have ssh by running ssh on your command line ( if not yum install ssh)

ssh=paramiko.SSHClient() # create ssh client
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy()) # to autenticate automatically without asking yes or no permission
ssh.connect(hostname="ipaddress/hostname",username="root",password="Reuters1",port=22)  # connect with username and password
# now to run commands we use the blow syntax in order to have variable for= stdout=output, stderr=error and stdin=for additional imput
stdin, stdout, stderr=ssh.exec_command("yourcommand")  # exec command will execute the command

print("the output is: ", stdout.read())  # the variable are files so you need read to see the content
print("The erros is: " ,stderr.read())

ssh.close() # close connection

# sytax to conncet with you private key
# ssh.connect(host="ip/hostname",username="username",key_filename="your_private_key_file",port=22)

################################# Windows to Linux ##################################################################

ssh=paramiko.SSHClient() # create ssh client
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
ssh.connect(hostname="ipaddress/hostname",username="root",password="Reuters1",port=22,)
stdin, stdout, stderr=ssh.exec_command("yourcommand")

print("the output is: ", stdout.read())  # the variable are files so you need read to see the content
print("The erros is: " ,stderr.read())

ssh.close() # close connection

########################################## transfer of dowload file from to remote server #############################

ssh=paramiko.SSHClient() # create ssh client
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
ssh.connect(hostname="ipaddress/hostname",username="root",password="Reuters1",port=22)

sftp_client=ssh.open_sftp() # open sftp connection to deal with files
sftp_client.get("path/filename","destination_Path/filename") # to download the file
# if you do not want to specify the path you can use the command sftp_client.chdir("location") to move to desired location
# print(sftp_client.getcwd()) it will print location where you are in remote server

sftp_client.put("location/filename", "destination_Location/filename")

# sftp_client.close() # close ftp client
ssh.close() # close connection


