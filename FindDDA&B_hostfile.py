
import paramiko
import re

try:
    ssh=paramiko.SSHClient() # create ssh client
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    ssh.connect(hostname="10.167.47.1",username="root",password="Reuters1",port=22)

    ftp=ssh.open_sftp()
    print("ftp connection established")
    ftp.get("/etc/hosts","C:\\Users\\u6017127\\Documents\\Eikon\\Project\\TestPython\\hosts.txt")
    ftp.close()
    ssh.close() # close connection
    # patt=r"\d{1-3}.\d{1-3}.\d{1-3}.\d{1-3}" # patt tofind ip addresses
    patt = r"DDN[AB]"
    fo = open("C:\\Users\\u6017127\\Documents\\Eikon\\Project\\TestPython\\hosts.txt", "r") # open host file in read mode
    files_lines = fo.readlines() # readlines create a list with each line of the file
    # print(files_lines)
    for each_line in files_lines:     # loop into list crreated
        if re.findall(patt, each_line):   # only print when you fine key word DDNA or DDNB
            print("the result is: ", each_line)
    fo.close()

except Exception as e:
    print(e)



















 #if __name__=="__main__":
  #  main()
