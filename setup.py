#!/usr/bin/env python
#coding=utf8

try:
    from  setuptools import setup, find_packages
except ImportError:
    from distutils.core import setup

setup(
        name = 'pyobject',
        version = '1.0',
        install_requires = [], 
        description = 'my python base object',
        url = 'https://github.com/zhouxianggen/pyobjec.git', 
        author = 'zhouxianggen',
        author_email = 'zhouxianggen@gmail.com',
        classifiers = [ 'Programming Language :: Python :: 3.7',],
        packages = ['pyobject'],
        data_files = [ ],  
        entry_points = { }   
        )
