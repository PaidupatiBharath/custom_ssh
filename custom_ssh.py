import paramiko
from subprocess import Popen 
from time import sleep

def custom_ssh_client(hostname,port=22,user=None,passwd=None):
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    ssh.connect(hostname,port,user,passwd)
    stdin,stdout,stderr=ssh.exec_command('iperf3 -s -1 -i 1 >> A.txt')
    ssh.close()

details = custom_ssh_client('192.168.15.10',user='user',passwd='user')

