__author__ = 'sloan'

#show how to call .so danymic lib in python

import ctypes

lib = ctypes.cdll.LoadLibrary('../lib/libhello.so')

lib.hello()








