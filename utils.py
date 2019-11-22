import numpy as np
import sympy as sp

def int2bin(a, lenght):
    return list(bin(a)[2:].zfill(lenght))
    

class QuasiGroup(object):
    def __init__(self, power):
        super(QuasiGroup, self).__init__()
        self.power = power
        self.order = 2 ** power
        self.table = np.zeros((2 ** power, 2 ** power))
        self.bin_table = np.zeros((2 ** power, 2 ** power, power))
        
    def set_table(self, q):
        self.table = np.array(q)
        for i in range(self.order):
            for j in range(self.order):
                a = int2bin(q[i][j], lenght=self.power)
                self.bin_table[i,j,:] = a
    

        