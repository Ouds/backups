### 模块导入问题

配置：`export PYTHONPATH=/home/bigdata/cqbigdata_analysis/src:$PYTHONPATH`

### cron任务中模块导入问题

``` Bash
crontab -e
PYTHONPATH=/home/bigdata/cqbigdata_analysis/src:$PYTHONPATH
MAILTO="linshi@budshome.com"
```
