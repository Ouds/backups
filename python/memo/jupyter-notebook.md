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
c.NotebookApp.ip = u'0.0.0.0' # 可以指定ip
c.NotebookApp.port = 8888
c.NotebookApp.notebook_dir = u''  # 指定工作目录
c.NotebookApp.password = u'' # 上面加密生成的password
c.NotebookApp.quit_button = False
c.NotebookApp.open_browser = False
```

### 集成jupytext

> 若jupytext扩展未出现
- jupyter nbextension install --py jupytext [--user]
- jupyter nbextension enable --py jupytext [--user]

``` Python
c.NotebookApp.contents_manager_class = u'jupytext.TextFileContentsManager'
```
