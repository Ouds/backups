### 获取Python

``` Bash
wget https://www.python.org/ftp/python/3.7.3/Python-3.7.3.tgz
tar -xvf Python--3.7.3.tgz
cd Python--3.7.3
```

### configure

``` Bash
./configure --with-ssl --enable-loadable-sqlite-extensions --enable-optimozations
```

- pip-ssl: `./configure --with-ssl`
- sqlite: `./configure --enable-loadable-sqlite-extensions`
- optimozations(包括bz2): `./configure --enable-optimozations`

### make

``` Bash
sudo make

sudo -H make install
```

all-dependencies: `sudo apt install 
build-essential zlib1g-dev libffi-dev openssl libssl-dev libsqlite3-dev libbz2-dev`

- build error: `sudo apt install build-essential`
- zipimport.ZipImportError: `sudo apt install zlib1g-dev`
- ModuleNotFoundError: No module named '_ctypes': `sudo apt install libffi-dev`
- SSL error: `sudo apt install openssl libssl-dev`
- sqlite error: `sudo apt install libsqlite3-dev
bz2 error: sudo apt-get install libbz2-dev`

### path

``` Bash
sudo cp /usr/local/bin/python3 /usr/local/bin/python
sudo cp /usr/local/bin/pip3 /usr/local/bin/pip
```

### upgrade

``` Bash
sudo apt upgrade python3
```
