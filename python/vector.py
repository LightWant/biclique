from ctypes.wintypes import SIZE
import numpy as np

class vector():
    def __init__(self, sz_):
        self.v = np.array(sz_, dtype=np.int32)
        self.sz = sz_
        self.n = 0
    
    def push_back(self, x):
        if self.n == self.sz:
            self.sz *= 2;
            tmpv = np.array(self.sz)

        self.v[self.n] = x
        self.n = self.n + 1
        
