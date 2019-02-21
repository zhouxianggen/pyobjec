pyobject
![](https://img.shields.io/badge/python%20-%203.7-brightgreen.svg)
========
> my python base object

## `Install`
` pip install git+https://github.com/zhouxianggen/pyobject.git`

## `Upgrade`
` pip install --upgrade git+https://github.com/zhouxianggen/pyobject.git`

## `Uninstall`
` pip uninstall pyobject`

## `Basic Usage`
```python
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

```
