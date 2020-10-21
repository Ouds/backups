# 问题收集

## rustup 不能编译

安装 gcc/g++

## `note: /usr/bin/ld: cannot find -lpq`

安装 `libpq-dev`

## error: failed to run custom build command for `openssl-sys v...`

安装 `pkg-config`（重要）、`libssl-dev`

## 仅限 WSL1 `vscode-remote: Permission denied(os error 13)`

配置 `settings.json`——

``` json
    "files.watcherExclude": {
        "**/target/": true
    }
```
