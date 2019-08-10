# Linux修改swap虚拟内存大小

## swap交换分区大小的规则

物理内存 | 交换分区（SWAP）
------ | ------
<= 4G | 至少4G
4~16G | 至少8G
16G~64G | 至少16G
64G~256G | 至少32G

## 查看系统Swap空间使用



``` Bash
bigdata@bdm1:~$ free -m
              total        used        free      shared  buff/cache   available
Mem:           9998        5358        4231           8         408        4355
Swap:          2015           0        923
```

## 创建swap文件

``` Bash
bigdata@bdm1:~$ sudo mkdir /usr/swap
bigdata@bdm1:~$ sudo touch /usr/swap/swapfile1
bigdata@bdm1:~$ cd /usr/swap/
bigdata@bds1:/usr/swap$ ll
total 8
drwxr-xr-x  2 root root 4096 Jun  5 10:55 ./
drwxr-xr-x 11 root root 4096 Jun  5 10:55 ../
bigdata@bdm1:/usr/swap$ sudo dd if=/dev/zero of=/usr/swap/swapfile1 bs=1024 count=20000000
记录了20000000+0 的读入
记录了20000000+0 的写出
20480000000字节(9.20 GB)已复制，15.40277 秒，300 MB/秒
```

注意：if 表示 infile，of 表示outfile，bs=1024 表示写入的每个块的大小为1024B=1KB(1024B字节=1024*8bit位

## 查看创建swap文件的大小

``` Bash
bigdata@bdm1:/usr/swap$ du -sh /usr/swap/swapfile1
20G     /usr/swap/swapfile1
```

## 将目标文件设置为swap分区文件

``` Bash
bigdata@bdm1:/usr/swap$ sudo mkswap /usr/swap/swapfile1
Setting up swapspace version 1, size = 999996 KiB
no label, UUID=7eec8e34-e5d9-48f7-aa71-098900r48e46
```

## 激活swap，立即启用交换分区文件

``` Bash
bigdata@bdm1:/usr/swap$ swapon /usr/swap/swapfile1
Setting up swapspace version 1, size = 999996 KiB
no label, UUID=7eec8e34-e5d9-48f7-aa71-098900r48e46
```

## 开机自启，需修改/etc/fstab中的swap行

``` Bash
bigdata@bdm1:/usr/swap$ sudo vi /etc/fstab
# /etc/fstab: static file system information.
#
# Use 'blkid' to print the universally unique identifier for a
# device; this may be used with UUID= as a more robust way to name devices
# that works even if disks are added and removed. See fstab(5).
#
# <file system> <mount point>   <type>  <options>       <dump>  <pass>
/dev/mapper/bdm1--vg-root /               ext4    errors=remount-ro 0       1
# /boot was on /dev/sda1 during installation
UUID=2b6c48cb-728b-418d-9ddf-e7988d9e0c68 /boot           ext2    defaults        0       2
#/dev/mapper/bdm1--vg-swap_1 none            swap    sw              0       0
/usr/swap/swapfile1         swap            swap    defaults        0       0
/dev/fd0        /media/floppy0  auto    rw,user,noauto,exec,utf8 0       0
~
```

## 重启系统

``` Bash
sync && sudo sync && sudo reboot
```

## 查看系统Swap空间是否生效

``` Bash
bigdata@bdm1:/usr/swap$ free -m
              total        used        free      shared  buff/cache   available
Mem:           9998        5470        4080           8         447        4243
Swap:         19531           0       19531
```
