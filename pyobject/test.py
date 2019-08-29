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
a.setup_log(name="xman")
a.log.info('who am i')
a.setup_log(name="xman2", path="/logs/xman2")
a.log.info('who am i 2')
a.setup_log(name="xman3", path=None)
a.log.info('who am i 3')

