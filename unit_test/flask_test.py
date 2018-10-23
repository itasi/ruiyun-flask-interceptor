from flask import Flask,abort
from arch.restful_interceptor import Ext
from arch.raise_for_restful_exception import RestfulException
from enum import Enum


class Platform(Enum):
    ANDROID = 1,
    VUE = 2,
    MICRO_PROGRAMM = 3


def before_request(key,path,request):
    print('test')
    pass


app = Flask(__name__)
ext = Ext(app, Platform,before_request)


@ext.annote(suffix='/index', platform=Platform.ANDROID)
@app.route('/index')
def index():
    # raise RestfulException('异常测试')
    return 'index'


@ext.annote(suffix='/user/aaa/<name>', platform=Platform.ANDROID)
@app.route('/user/aaa/<name>')
def user(name):
    return name


@app.route('/indexx')
def test():
    # abort(404)
    return 'test'


if __name__ == '__main__':
    app.run(debug=True)
