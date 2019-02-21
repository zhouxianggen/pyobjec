# coding: utf8 
import time
from pyobject import PyObject


class MyObject(PyObject):
    def foo(self):
        # 使用自带的log
        self.log.info('foo')

    @PyObject.took
    def bar(self):
        # 使用took修饰符显示函数运行耗费时间
        time.sleep(1.2)

a = MyObject()
a.foo()
a.bar()

