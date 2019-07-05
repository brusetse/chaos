#coding:utf-8
import os
import shutil
import re
import paramiko  #先运行 pip install paramiko安装
import time


server_list = ['ORP_Approval_Service','ORP_Financial_Service','ORP_Partner_Service','ORP_System_Service'
    ,'ORP_Task_Service','ORP_Report_Service','ORP-Api-Wap']

tomcat_war_list = ['Web_ORP','Web_ORP_Resources']


deploy_base_path = "/opt/orp"

current_file_path = os.path.dirname(os.path.abspath(__file__))

def git_mvn():
    """
    git 拉取代码与maven打包
    :return:
    """
    print("git pull mvn package ...")
    gitpath = "/home/xbc/IdeaProjects/orp"

    os.chdir(gitpath)
    os.system("git checkout develop")
    os.system("git pull")
    os.chdir(gitpath+"/ORP")
    os.system("mvn clean")
    os.system("mvn install")
    print "git pull mvn package finish!"

    os.chdir(gitpath+"/ORP/Wap-ORP-Vue")
    try:
        shutil.rmtree(gitpath+"/ORP/Wap-ORP-Vue/dist")
    except:
        pass

    os.system("npm install")
    os.system("npm run build")
    """
        删除原来的文件夹
    """
    print "删除原来的文件"

    try:
        shutil.rmtree(current_file_path+"/deploy/service")
        shutil.rmtree(current_file_path + "/deploy/webapp")
        shutil.rmtree(current_file_path + "/deploy/dist")
    except:
        pass

    print "删除完成"

    """
        复制新的文件夹
    """
    print "开始复制"

    for server in server_list:
        shutil.copytree(gitpath+"/ORP/"+server+"/target/lib",current_file_path+"/deploy/service/"+server+"/lib")
        shutil.copy(gitpath + "/ORP/" + server + "/target/"+server+".jar"
                        ,current_file_path + "/deploy/service/" + server + "/"+server+".jar")


    for war in tomcat_war_list:
        shutil.copytree(gitpath+"/ORP/"+war+"/target/"+war,current_file_path + "/deploy/webapp/"+war)


    shutil.copytree(gitpath+"/ORP/Wap-ORP-Vue/dist",current_file_path + "/deploy/dist")
    print "复制完成"






def deploy_local():
    """
    本地发布
    """
    os.chdir(deploy_base_path + "/service/execute")
    os.system("./orp_server.sh stop")
    print "服务停止成功"

    """
    删除原来的服务
    """
    for server in server_list:
        try:
            shutil.rmtree(deploy_base_path + "/service/"+server)
        except:
            pass
    """
        复制新的服务
    """
    for server in server_list:
        shutil.copytree(current_file_path + "/deploy/service/" + server,deploy_base_path + "/service/"+server)

    print "复制成功"

    # os.system("./orp_server.sh start")

    print "local deploy ok"


def dev_deploy():
    hostname = '192.168.1.83'
    port = 22
    username = 'ivyb2b'
    password = 'IvyB2B@2018'
    deploy(hostname, password, port, username)
    print "dev deploy ok"





def uat_deploy():
    hostname = '192.168.1.25'
    port = 22
    username = 'ivyb2b'
    password = 'ivyb2b2018!@#'
    deploy(hostname, password, port, username)
    print "dev uat ok"


def prod_deploy():
    hostname = '120.79.35.94'
    port = 22888
    username = 'orpapp'
    password = 'yuwcfbX82kb6OMORP7COIGajJs0IUivy11'
    deploy(hostname, password, port, username)
    print "dev prod_deploy ok"




def deploy(hostname, password, port, username):
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy)
    ssh.connect(hostname=hostname, port=port, username=username, password=password)
    stdin, stdout, stderr = ssh.exec_command("cd " + deploy_base_path + "/service/execute;./orp_server.sh stop")
    for line in stdout:
        server_cid = line.strip("\n")
        print server_cid

    stdin, stdout, stderr = ssh.exec_command("cd " + deploy_base_path + "/service/execute;./orp_wap_api.sh stop")
    for line in stdout:
        api_cid = line.strip("\n")
        print api_cid

    print "服务停止成功"
    """
       移动原来的服务
       """
    #ssh.exec_command("cd " + deploy_base_path + "/service")
    for server in server_list:
        ssh.exec_command("rm -rf " + deploy_base_path + "/backup/service/" + server)
        backup_server = "mkdir -p " + deploy_base_path + "/backup/service"
        print backup_server
        ssh.exec_command(backup_server)
        backup_server = "mv " + deploy_base_path + "/service/" + server + " " + deploy_base_path + "/backup/service"
        print backup_server
        ssh.exec_command(backup_server)

    """
        复制新的服务
    """

    #休眠2秒使上面异步命令执行完
    time.sleep(10)

    os.chdir(current_file_path)
    os.system("./expect_scp "+hostname+" "+str(port)+" "+username+" "+password+" "
              +current_file_path+"/deploy/service "
              +deploy_base_path)





    print "复制服务成功"

    ssh.exec_command("cd " + deploy_base_path + "/service/execute;./orp_server.sh start")

    """
        复制war
    """
    stdin, stdout, stderr = ssh.exec_command("ps -ef|grep tomcat-8300 |grep -v \"grep\" |awk '{print $2}'")
    for line in stdout:
        tomcat_cid = line.strip("\n")
        if tomcat_cid:
            break
    print tomcat_cid
    if tomcat_cid:
        ssh.exec_command("kill -9 " + tomcat_cid)

    for war in tomcat_war_list:
        ssh.exec_command("rm -rf " + deploy_base_path + "/backup/webapp/" + war)
        backup_server = "mkdir -p " + deploy_base_path + "/backup/webapp"
        print backup_server
        ssh.exec_command(backup_server)
        ssh.exec_command("mv " + deploy_base_path + "/webapp/tomcat-8300/webapps/" + war + " " + deploy_base_path + "/backup/webapp")

    


    # 休眠2秒使上面异步命令执行完
    time.sleep(10)

    os.chdir(current_file_path)
    for war in tomcat_war_list:
        filename = current_file_path + "/deploy/webapp/" + war
        remote_filename = deploy_base_path + "/webapp/tomcat-8300/webapps"
        print filename
        print remote_filename
        os.system("./expect_scp " + hostname + " "+str(port)+" " + username + " " + password + " "
                  + filename+" "
                  + remote_filename)

    print "复制应用成功"

    time.sleep(10)
    #复制ui
    ssh.exec_command("rm -rf " + deploy_base_path + "/backup/dist/")
    backup_ui = "mkdir -p " + deploy_base_path + "/backup/dist"
    print backup_ui
    ssh.exec_command(backup_ui)
    ssh.exec_command("mv " + deploy_base_path + "/webapp/orp" + " " + deploy_base_path + "/backup/dist")

    os.system("./expect_scp " + hostname + " " + str(port) + " " + username + " " + password + " "
              + current_file_path + "/deploy/dist"  + " "
              + deploy_base_path + "/webapp/orp")

    ssh.close()



def Main():
    v = raw_input("是否要拉取develop代码（y/n）")
    if v == 'y':
        git_mvn()

    s = raw_input("请输入要发布的环境（1.local，2.dev，3.uat，4.prod）")
    if s:
        if s == '1':
            deploy_local()
        elif s == '2':
            dev_deploy()
        elif s == '3':
            uat_deploy()
        elif s == '4':
            prod_deploy()


if __name__ == '__main__':
    Main()








