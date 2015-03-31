# -*- coding: utf-8 -*-
#! /usr/bin/env python
import paramiko
import threading

#该方法实现ssh登陆远程机器执行命令
def sshcmd(ip,user,passwd,cmd):
    try:
        ssh = paramiko.SSHClient()
        ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        #ssh登陆目标主机
        ssh.connect(ip,22,user, passwd,timeout=5)
        #cmd命令
        stdin, stdout, stderr = ssh.exec_command(cmd)
        out = stdout.readlines()
        #打印出执行命令后的结果
        print "ip:%s conten:%s"%(ip,out)
        # for o in out:
        #     print(o)
        #关闭ssh
        ssh.close()
    except:
        print("ip为%s未登录成功"%ip)

def sshkey(ip,user,passwd,cmdkey):
    try:
        ssh = paramiko.SSHClient()
        ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        #ssh登陆目标主机
        ssh.connect("10.6.2.124",22,user, passwd,timeout=5)
        #cmd命令
        stdin, stdout, stderr = ssh.exec_command(cmdkey)

        out = stdout.readlines()
        #打印出执行命令后的结果
        print "ip:%s"%ip
        # for o in out:
        #     print(o)
        #关闭ssh
        ssh.close()
    except:
        print("ip为%s未登录成功"%ip)

if __name__=='__main__':
    ips = ["10.6.2.125","10.6.2.126","10.6.2.127","10.6.2.128","10.6.2.129","10.6.2.130","10.6.2.131",\
          "10.6.2.132","10.6.2.134","10.6.2.135","10.6.2.136"]
    user = "lw"
    passwd = "root"
    cmd ="sudo reboot"

    for ip in ips:
        try:
            # cmdkey ="ssh-copy-id -i /home/lw/.ssh/id_rsa.pub %s"%ip
            # print(ip)
            a = sshkey(ip,user,passwd,cmd)
            # a=threading.Thread(target=sshkey,args=(ip,user,passwd,cmd))
            # a.start()
        except:
            print("ip为%s未登录成功"%ip)
            continue