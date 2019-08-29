# coding: utf8 
import logging
from logging.handlers import RotatingFileHandler
from datetime import datetime


class PyObject(object):
    def __init__(self, log_name='', log_path='', log_level=logging.INFO):
        self.setup_log(log_name, log_path, log_level)
        
    
    def setup_log(self, name='', path=None, level=logging.INFO):
        log = logging.getLogger(name or self.__class__.__name__)
        log.setLevel(level)
        log.propagate = False
        for hdlr in log.handlers:
            log.removeHandler(hdlr)

        fmt = ('[%(name)-15s %(threadName)-10s %(levelname)-8s '
                '%(asctime)s] %(message)s')
        if path:
            hdlr = RotatingFileHandler(
                    path, maxBytes=1024*1024*64, backupCount=10)
        else:
            hdlr = logging.StreamHandler()
        hdlr.setFormatter(logging.Formatter(fmt))
        log.addHandler(hdlr)
        self.log = log


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

