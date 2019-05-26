### generate config

``` Bash
jupyter notebook --generate-config
jupyter notebook password
```

### edit config

``` Bash
vi jupyter_notebook_config.py
```

``` Python
c.NotebookApp.ip='0.0.0.0' # 可以指定ip
c.NotebookApp.password = u'sha1:9b23ce21f3cf:78fe4dc3e506525727... # 上面生成的password'
c.NotebookApp.open_browser = False
c.NotebookApp.port = 8888
c.NotebookApp.quit_button = False
```

### 集成jupytext

> 若jupytext扩展未出现
- jupyter nbextension install --py jupytext [--user]
- jupyter nbextension enable --py jupytext [--user]

``` Python
c.NotebookApp.contents_manager_class = "jupytext.TextFileContentsManager"
```
