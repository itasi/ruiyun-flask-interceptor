# -*- coding: utf-8 -*-
from setuptools import setup, find_packages

with open('requirements.txt') as requirement_file:
    requirements = [line for line in requirement_file.read().splitlines() if line]

setup(
    name='ruiyun-flask-interceptor',
    version='0.0.2',
    long_description='对restful接口统一进行拦截处理',
    keywords=['flask', 'restful', 'interceptor', 'AOP'],
    description='基于flask扩展的拦截框架',
    license="MIT Licence",

    url='https://gitee.com/akenz/flask-ext',
    author='chuckiefan',
    author_email='chuckiefan@163.com',
    packages=['arch'],
    install_requires=requirements
)
