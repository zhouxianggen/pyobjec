# coding: utf8 
import logging
from datetime import datetime


class PyObject(object):
    def __init__(self, logLevel=logging.INFO):
        self.log = logging.getLogger(self.__class__.__name__)
        self.log.setLevel(logLevel)
        self.log.propagate = False
        if not self.log.handlers:
            fmtStr = ('[%(name)-15s %(threadName)-10s %(levelname)-8s '
                    '%(asctime)s] %(message)s')
            handler = logging.StreamHandler()
            handler.setFormatter(logging.Formatter(fmtStr))
            self.log.addHandler(handler)

    @classmethod
    def took(cls, func):
        def wrapper(*args, **kwargs):
            obj = args[0]
            start = datetime.now()
            r = func(*args, **kwargs)
            td = datetime.now() - start
            v = (td.microseconds + (td.seconds + td.days * 24 * 3600)
                 * 10**6) / 1000.0
            obj.log.info('%s.%s took %.2f ms' % ( 
                    obj.__class__.__name__, func.__name__, v)) 
            return r
        return wrapper

