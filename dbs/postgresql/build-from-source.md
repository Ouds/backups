# 获取 PostgreSQL 源码

``` Bash
wget https://ftp.postgresql.org/pub/source/v12.1/postgresql-12.1.tar.gz
gunzip postgresql-12.1.tar.gz
tar xf postgresql-12.1.tar
cd postgresql-12.1
```

# 配置、编译，安装

``` Bash
sudo apt install libreadline6-dev zlib1g-dev
./configure # 默认 --prefix=/usr/local/pgsql
sudo make && make install
# contrib 工具，建议安装
cd contrib
sudo make && make install
```

# 创建用户，赋予权限

``` Bash
sudo deluser postgres
sudo adduser postgres
sudo chown -R postgres:postgres /usr/local/pgsql
```

# 配置 postgres 用户环境变量

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

# 设置开机自启动

``` Bash
sudo cp ~/postgresql-12.1/contrib/start-scripts/linux /etc/init.d/postgresql
sudo vi /etc/init.d/postgresql # 检查环境变量
sudo chmod a+x /etc/init.d/postgresql
# 验证
service postgresql stop
service postgresql start
```
