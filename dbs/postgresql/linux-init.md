# 安装 PostgreSQL

适用于 `Bionic(Ubuntu 18.04)`

``` Bash
sudo touch /etc/apt/sources.list.d/pgdg.list
sudo vi /etc/apt/sources.list.d/pgdg.list
```

添加一行 `deb http://apt.postgresql.org/pub/repos/apt/ bionic-pgdg main`

``` Bash
wget --quiet -O - https://www.postgresql.org/media/keys/ACCC4CF8.asc | sudo apt-key add -
```

若添加 `OpenPGP key` 出现错误：`gpg: no valid OpenPGP data found.`

``` Bash
sudo apt install ca-certificates

sudo apt update
sudo apt install -y postgresql-1*
```

# 修改系统 postgres 用户密码

PostgreSQL 会创建一个默认的 linux 用户 postgres，修改该用户密码的方法如下：

- 步骤一：删除用户 postgres 的密码
- 步骤二：设置用户 postgres 的密码

``` Bash
sudo  passwd -d postgres
sudo -u postgres passwd
Enter new UNIX password:
Retype new UNIX password:
passwd: password updated successfully
```
 
# 修改数据库默认用户 postgres 密码

PostgreSQL 数据库创建一个 postgres 用户作为数据库的管理员，密码随机，所以需要修改密码，方式如下：

- 步骤一：登录 PostgreSQL
- 步骤二：修改登录 PostgreSQL 密码

``` Bash
sudo -u postgres psql
postgres=# ALTER USER postgres WITH PASSWORD 'postgres*';
```

# 查看 PostgreSQL 配置文件位置

``` Bash
sudo -u postgres psql
postgres=# select name, setting from pg_settings where category='File Locations';
```
