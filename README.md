ruiyun-flask-interceptor
==========
[![Build Status](https://travis-ci.com/chuckiefan/ruiyun-flask-interceptor.svg?branch=master)](https://travis-ci.com/chuckiefan/ruiyun-flask-interceptor)

#### 项目介绍

ruiyun-flask-interceptor基于flask，用于restful请求的拦截处理。




#### 安装教程

```shell
pip install ruiyun-flask-interceptor
``` 

#### 使用说明

##### 1. 定义可能请求的平台类型，要求为枚举类型：

```python
from enum import Enum
class Platform(Enum):
    ANDROID = 1,
    VUE = 2,
    MICRO_PROGRAMM = 3
```

##### 2. 定义请求拦截函数：

```python
def before_request(platform,path,request):
    pass
```


##### 3. 引入Ext并初始化：

```python

from flask import Flask
from arch.restful_interceptor import Ext
app = Flask(__name__)
ext = Ext(app, Platform,before_request)

```

##### 4. 对@app.route进行标注，抛出异常：

```python
@ext.annote(suffix='/index', platform=Platform.ANDROID)
@app.route('/index')
def index():
    raise RestfulException('异常测试')
```

#### 参与贡献

1. chuckiefan


