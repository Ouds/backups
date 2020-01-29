# 获取源码

``` Bash
wget https://ftp.postgresql.org/pub/source/v12.1/postgresql-12.1.tar.gz
gunzip postgresql-12.1.tar.gz
tar xf postgresql-12.1.tar
cd postgresql-12.1
```

# 配置、编译、安装

``` Bash
sudo apt install libreadline6-dev zlib1g-dev
./configure # 默认 --prefix=/usr/local/pgsql
sudo make && make install
# contrib 工具，建议安装
cd contrib
sudo make && make install
```

# 用户及权限

``` Bash
sudo deluser postgres
sudo adduser postgres
sudo chown -R postgres:postgres /usr/local/pgsql
```

# 用户环境变量

``` Bash 
su - postgres
vi ~/.profile

export PGHOME=/usr/local/pgsql
export PGDATA=$PGHOME/data
export PGHOST=/tmp
export PATH=$HOME/bin:$HOME/.local/bin:$PATH:$PGHOME/bin
export MANPATH=$PGHOME/share/man:$MANPATH
export LANG=zh_CN.utf8
export DATE=`date +"%Y-%m-%d %H:%M:%S"`
export LD_LIBRARY_PATH=$PGHOME/lib:$LD_LIBRARY_PATH
```

# 启动数据库

``` Bash
initdb -D /usr/local/pgsql/data
pg_ctl -D /usr/local/pgsql/data -l logfile start
```

# systemd 及开机自启

``` Bash
sudo cp ~/postgresql-12.1/contrib/start-scripts/linux /usr/local/pgsql/postgresql
sudo vi /usr/local/pgsql/postgresql # 检查环境变量
sudo chmod a+x /usr/local/pgsql/postgresql
# 验证
/usr/local/pgsql/postgresql start
/usr/local/pgsql/postgresql stop
# 创建 service 文件
sudo touch /etc/systemd/system/postgresql.service
sudo vi /etc/systemd/system/postgresql.service

[Unit]
Description=PostgreSQL-12.1

[Service]
ExecStart=/usr/local/pgsql/postgresql start

[Install]
WantedBy=multi-user.target

# 开机自启
sudo systemctl daemon-reload
sudo systemctl enable postgresql.service
# systemctl 启动
sudo systemctl start postgresql.service
```

# init.d（不推荐）

``` Bash
sudo cp ~/postgresql-12.1/contrib/start-scripts/linux /etc/init.d/postgresql
sudo vi /etc/init.d/postgresql # 检查环境变量
sudo chmod a+x /etc/init.d/postgresql
# 验证
service postgresql start
service postgresql stop
```
