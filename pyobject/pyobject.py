# coding: utf8 
import logging
from logging.handlers import RotatingFileHandler
from datetime import datetime


class PyObject(object):
    def __init__(self, logLevel=logging.INFO, logPath=''):
        self.log = logging.getLogger(self.__class__.__name__)
        self.log.setLevel(logLevel)
        self.log.propagate = False
        if not self.log.handlers:
            fmtStr = ('[%(name)-15s %(threadName)-10s %(levelname)-8s '
                    '%(asctime)s] %(message)s')
            if logPath:
                handler = RotatingFileHandler(
                        logPath, maxBytes=1024*1024*32, backupCount=10)
            else:
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


class BaseError(Exception):
    def __init__(self, error_code, error_desc=''):
        self.error_code = error_code
        self.error_desc = error_desc
        super(BaseError, self).__init__(error_code + error_desc)

