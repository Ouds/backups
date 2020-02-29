# 执行收集

## ubuntu-apt

``` Bash
sudo apt autoremove --purge; sudo apt autoclean; sudo apt clean; sudo apt update; sudo apt upgrade -y; sudo apt full-upgrade -y; sudo apt autoremove --purge; sudo apt autoclean; sudo apt clean; sudo shutdown -h now
```

## root - ssh

启用root账号（若未开启）：`sudo passwd root`

编辑配置文件：`sudo vi /etc/ssh/sshd_config`

找到如下配置——

``` Markdown
# Authentication:
#LoginGraceTime 120
#PermitRootLogin prohibit-password
#StrictModes yes
```

更改为——

``` Markdown
# Authentication:
LoginGraceTime 120
#PermitRootLogin prohibit-password
PermitRootLogin yes
StrictModes yes
```

重启ssh：`sudo service ssh restart`

## linux命令

``` Bash
# uname -a # 查看内核/操作系统/CPU信息 
# head -n 1 /etc/issue # 查看操作系统版本 
# cat /proc/cpuinfo # 查看CPU信息 
# hostname # 查看计算机名 
# lspci -tv # 列出所有PCI设备 
# lsusb -tv # 列出所有USB设备 
# lsmod # 列出加载的内核模块 
# env # 查看环境变量资源 
# free -m # 查看内存使用量和交换区使用量 
# df -h # 查看各分区使用情况 
# du -sh <目录名> # 查看指定目录的大小 
# grep MemTotal /proc/meminfo # 查看内存总量 
# grep MemFree /proc/meminfo # 查看空闲内存量 
# uptime # 查看系统运行时间、用户数、负载 
# cat /proc/loadavg # 查看系统负载磁盘和分区 
# mount | column -t # 查看挂接的分区状态 
# fdisk -l # 查看所有分区 
# swapon -s # 查看所有交换分区 
# hdparm -i /dev/hda # 查看磁盘参数(仅适用于IDE设备) 
# dmesg | grep IDE # 查看启动时IDE设备检测状况网络 
# ifconfig # 查看所有网络接口的属性 
# iptables -L # 查看防火墙设置 
# route -n # 查看路由表 
# netstat -lntp # 查看所有监听端口 
# netstat -antp # 查看所有已经建立的连接 
# netstat -s # 查看网络统计信息进程 
# ps -ef # 查看所有进程 
# top # 实时显示进程状态用户 
# w # 查看活动用户 
# id <用户名> # 查看指定用户信息 
# last # 查看用户登录日志 
# cut -d: -f1 /etc/passwd # 查看系统所有用户 
# cut -d: -f1 /etc/group # 查看系统所有组 
# crontab -l # 查看当前用户的计划任务服务 
# chkconfig –list # 列出所有系统服务 
# chkconfig –list | grep on # 列出所有启动的系统服务程序 
# rpm -qa # 查看所有安装的软件包
```

## sudoer文件修改错误

如欲在sudoers文件中添加user ALL=(ALL) ALL这条语句，只添加了user,未添加ALL=(ALL) ALL就保存退出了，并切换到了普通用户。此时，如果普通用户在此使用sudoer su命令时，系统提示sudoers文件中有语法错误，导致命令不能执行，所以不能进入root权限,而sudoers又只能在root权限下才能修改。

### 解决方法

1. 重启系统；
1. 启动时按`shift`,选择`recovery mode`,此时就是以`root`权限进入系统了，在这里对`/etc/sudoers`文件进行修改；
1. `/etc/sudoers`默认是只读文件，所以先改变他的属性，输入`chmod 440 /etc/sudoers`；
1. 如果提示没有权限，或者不允许修改，就先输入`mount -o remount rw /`，然后更改权限即可；
1. 如果内容有错误，可以`vi /etc/sudoers`进入修改；或者将以前添加的错误部分删除再保存。
