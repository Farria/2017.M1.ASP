    # -*- coding: utf-8 -*-
"""
Created on Tue Oct 16

@author: jaehyuk

Class inheritance
"""

import numpy as np
#import scipy.stats as ss
#import scipy.optimize as sopt
from .bsm import Model as ModelBsm

'''
Now we want to define a class using inheritance
Put the base class name in ().
So ModelBsm is base (or parent) class
Model is derived (or child) class
'''

class Model(ModelBsm):
    ''' 
    Basic rule that the definition of the base class is implicitly given, 
    so you only redefine(override) what you need to change.
    '''

    # texp, vol, intr, divr = None, None, None, None <-- all comes from the base class
    shift = None
    
    ''' from the base class (bsm.py)
    def __init__(self, texp, vol, intr=0, divr=0):
        self.texp = texp
        self.vol = vol
        self.intr = intr
        self.divr = divr
    '''

    def __init__(self, texp, vol, shift=0, intr=0, divr=0):
        super().__init__(texp, vol, intr=intr, divr=divr)
        self.shift = shift # <-- new
        
    def price(self, strike, spot, texp=None, vol=None, cp_sign=1):
        return super().price(strike + self.shift, spot + self.shift, texp, vol, cp_sign=cp_sign)
    
    def delta(self, strike, spot, texp=None, vol=None, cp_sign=1):
        return super().delta(strike + self.shift, spot + self.shift, texp, vol, cp_sign=cp_sign)

    '''
    Here I redefine vega 
    '''
    def vega(self, strike, spot, texp=None, vol=None, cp_sign=1):
        return 3.14
    
    ''' 
    I didn't define gamma here. See what happens
    def gamma(self, strike, spot, texp=None, vol=None, cp_sign=1):
        return 0
    '''
    def impvol(self, price_in, strike, spot, texp=None, cp_sign=1):
        return super().impvol(price_in, strike + self.shift, spot + self.shift, texp, cp_sign=cp_sign)
