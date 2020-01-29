# 获取源码

``` Bash
wget http://nginx.org/download/nginx-1.16.1.tar.gz
gunzip nginx-1.16.1.tar.gz
tar xf nginx-1.16.1.tar
cd nginx-1.16.1
```

# 配置、编译、安装

``` Bash
sudo apt install build-essential libtool libpcre3-dev zlib1g-dev openssl
./configure # 默认 --prefix=/usr/local/nginx
sudo make && make install
```

# 启动、重启、停止

``` Bash
sudo /usr/local/nginx/sbin/nginx
sudo /usr/local/nginx/sbin/nginx -s reload
sudo /usr/local/nginx/sbin/nginx -s stop
```

<del>
# systemd 及开机自启

``` Bash
# 创建 service 文件
sudo touch /etc/systemd/system/nginx.service
sudo vi /etc/systemd/system/nginx.service

[Unit]
Description=nginx-1.16

[Service]
ExecStart=/usr/local/nginx/sbin/nginx

[Install]
WantedBy=multi-user.target

# 开机自启
sudo systemctl daemon-reload
sudo systemctl enable nginx.service
# systemctl 启动
sudo systemctl start nginx.service
```
</del>
