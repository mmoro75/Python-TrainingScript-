# this scrip will allow you to use portblocker on remote server

import paramiko
import re
import time
import datetime
import subprocess


def portbloker():
    global today
    global eth1,eth2,eth3,eth4
    global path
    print("!!!WARNING: make sure 'portblocker.tar' is available in your working path!!! ")
    path = input("Please provide your working path: ")
    hostname = input("please provide hostname-ip address: ")
    install_port_blocker(hostname,path)
    server_eth = collect_NICs(hostname,path)
    eth1="".join(server_eth.get('eth1'))
    eth2="".join(server_eth.get('eth2'))
    eth3="".join(server_eth.get('eth3'))
    eth4="".join(server_eth.get('eth4'))
    block_Ports(hostname, eth1, eth2, eth3, eth4)
    cmd = "del C:\\Users\\u6017127\\Documents\\Eikon\\Project\\TestPython\\hosts.txt"
    sp = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, universal_newlines=True)
    return None


def install_port_blocker(hostname,path):
    try:
        ssh = paramiko.SSHClient()  # create ssh client
        ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        ssh.connect(hostname=hostname, username="root", password="Reuters1", port=22)
        ftp = ssh.open_sftp()
        print("ftp connection installing portblocker")
        print(path + "\\portblocker.tar")
        ftp.put(path+"\\portblocker.tar", "/root/portblocker.tar")
        time.sleep(15)
        ftp.close()
        print("Upload file completed ")
        stdin, stdout, stderr = ssh.exec_command("tar -vxf portblocker.tar")
        print("portblocker.tar unzipped checking version:")
        stdin, stdout, stderr = ssh.exec_command("chmod a+x portblocker")
        stdin, stdout, stderr = ssh.exec_command("chmod a+x PortBlocker_Eng.ko")
        stdin, stdout, stderr = ssh.exec_command("./portblocker -version")

        file_out = stdout.readlines()
        for line in file_out:
            if line in file_out:
                print(line)
        file_err = stderr.readlines()
        for err in file_err:
            if err in file_err:
                print(
                    f"{err}\n Portblocker in not installed on your machine\n make sure 'portblocker.tar' file is in your working path")
        return None
    except Exception as e:
        print(e)


def collect_NICs(hostname,path):
    try:
        ssh = paramiko.SSHClient()  # create ssh client
        ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        ssh.connect(hostname=hostname, username="root", password="Reuters1", port=22)
        ftp = ssh.open_sftp()
        print("ftp colletting server NICs information")
        ftp.get("/etc/hosts", path+"\\hosts.txt")
        ftp.close()
        ssh.close()  # close connection
        # patt=r"\d{1-3}.\d{1-3}.\d{1-3}.\d{1-3}" # patt tofind ip addresses
        patt1 = r"\bDDNA-eth\d"
        patt2 = r"\bDDNB-eth\d"
        patt3 = r"\bEXCHIPA-eth\d"
        patt4 = r"\bEXCHIPB-eth\d"
        fo = open(path+"\\hosts.txt",
                  "r")  # open hosts file in read mode
        files_lines = fo.readlines()  # readlines create a list with each line of the file
        server_eth = {"eth1": [], "eth2": [], "eth3": [], "eth4": []}
        for each_line in files_lines:  # loop into list created
            if re.findall(patt1, each_line):  # only print when you fine key word DDNA
                server_eth["eth1"].append(each_line[-5] + each_line[-4] + each_line[-3] + each_line[-2])
            elif re.findall(patt2, each_line):
                server_eth["eth2"].append(each_line[-5] + each_line[-4] + each_line[-3] + each_line[-2])
            elif re.findall(patt3, each_line):
                server_eth["eth3"].append(each_line[-5] + each_line[-4] + each_line[-3] + each_line[-2])
            elif re.findall(patt4, each_line):
                server_eth["eth4"].append(each_line[-5] + each_line[-4] + each_line[-3] + each_line[-2])
        fo.close()
        print(f"NIC Card for DDNA is {server_eth.get('eth1')}")
        print(f"NIC Card for DDNB is {server_eth.get('eth2')}")
        print(f"NIC Card for EXCHA is {server_eth.get('eth3')}")
        print(f"NIC Card for EXCHB is {server_eth.get('eth4')}")
        return server_eth
    except Exception as e:
        print(e)


def block_Ports(hostname,eth,eth2,eth3,eth4):
    try:
        ssh = paramiko.SSHClient()  # create ssh client
        ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        ssh.connect(hostname=hostname, username="root", password="Reuters1", port=22)
        print("Connected to remote host")
        a = input("Please provide NIC Card to block: DDN or EXCH?: ").upper()
        b = input("Please provide protocol you want to block UDP, TCP, BOTH: U,T,B: ").upper()
        wait=eval(input("how many seconds to you want to keep Cards blocked? ebeter value in seconds: "))
        seconds = str(wait)
        if a == "DDN" and b=="B":
            stdin, stdout, stderr = ssh.exec_command(
                "./portblocker -i " + eth1 + " -j " + eth2 + " -r B -s B -d B -e B -t " + seconds + " -f 1 -a")
            print(f"All DDN NIC cards traffic is blocked for {wait} seconds")
            time.sleep(wait + 10)
            print("Completed all the blocked channles are back on line ")
            ssh.close()
            print("Portblocker stopped all the traffic is now restored")
        elif a == "DDN" and b== "U":
            stdin, stdout, stderr = ssh.exec_command(
                "./portblocker -i " + eth1 + " -j " + eth2 + " -r U -s U -d B -e B -t " + seconds + " -f 1 -a")
            print(f"All UPD Traffic is blocked on DDN NIC for {wait} seconds")
            time.sleep(wait + 10)
            print("Completed all the blocked channles are back on line ")
            ssh.close()
            print("Portblocker stopped all the traffic is now restored")
        elif a == "DDN" and b == "T":
            stdin, stdout, stderr = ssh.exec_command(
                "./portblocker -i " + eth1 + " -j " + eth2 + " -r T -s T -d B -e B -t " + seconds + " -f 1 -a")
            print(f"All TCP Traffic is blocked on DDN NIC for {wait} seconds")
            time.sleep(wait + 10)
            print("Completed all the blocked channles are back on line ")
            ssh.close()
            print("Portblocker stopped all the traffic is now restored")
        elif a == "EXCH" and b == "B":
            stdin, stdout, stderr = ssh.exec_command(
                "./portblocker -i " + eth3 + " -j " + eth4 + " -r B -s B -d B -e B -t " + seconds + " -f 1 -a")
            print(f"All Exchange NIC cards traffic is blocked for {wait} seconds")
            time.sleep(wait + 10)
            print("Completed all the blocked channles are back on line ")
            ssh.close()
            print("Portblocker stopped all the traffic is now restored")
        elif a == "EXCH" and b== "U":
            stdin, stdout, stderr = ssh.exec_command(
                "./portblocker -i " + eth3 + " -j " + eth4 + " -r U -s U -d B -e B -t " + seconds + " -f 1 -a")
            print(f"All UPD Traffic is blocked on Exchange NIC for {wait} seconds")
            time.sleep(wait + 10)
            print("Completed all the blocked channles are back on line ")
            ssh.close()
            print("Portblocker stopped all the traffic is now restored")
        elif a == "DDN" and b == "T":
            stdin, stdout, stderr = ssh.exec_command(
                "./portblocker -i " + eth3 + " -j " + eth4 + " -r T -s T -d B -e B -t " + seconds + " -f 1 -a")
            print(f"All TCP Traffic is blocked on Exchange NIC for {wait} seconds")
            time.sleep(wait + 10)
            print("Completed all the blocked channles are back on line ")
            ssh.close()
            print("Portblocker stopped all the traffic is now restored")
        else:
            print(f"WRONG SELECTIONS\n Your current selection is:\n NIC Cards to Block={a}\n Protocol:{b},please check all the inforamtion are correct")
            block_Ports(hostname,username,password,eth,eth2,eth3,eth4)
        ssh.close()
        return None
    except Exception as e:
        print(e)

portbloker()

if __name__=="__portblocker__":
    ErrorLogs()