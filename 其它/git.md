# `git`相关

## `git`参数配置

``` Bash
# 个人标识
git config --global user.name "***"
git config --global user.email "****"

# 凭据参数
git config --global credential.helper store
```

## `github`提速配置（清除`DNS`污染）

从https://ipaddress.com查询`github.com`、`assets-cdn.github.com`、`github.global.ssl.fastly.net`三个`github`相关域名的对应`IP`，配置在`hosts`中。如下示例：

``` Markdown
192.30.253.112 github.com
192.30.253.113 github.com

185.199.108.153 assets-cdn.github.com
185.199.109.153 assets-cdn.github.com
185.199.110.153 assets-cdn.github.com
185.199.111.153 assets-cdn.github.com

151.101.185.194 github.global.ssl.fastly.net
```
