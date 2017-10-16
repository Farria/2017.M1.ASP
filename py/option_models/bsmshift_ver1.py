    # -*- coding: utf-8 -*-
"""
Created on Tue Oct 16

@author: jaehyuk
"""

import numpy as np
from . import bsm

class Model:
    texp, vol, intr, divr = None, None, None, None
    shift = None # <-- new
    
    def __init__(self, texp, vol, shift=0, intr=0, divr=0):
        self.texp = texp
        self.vol = vol
        self.intr = intr
        self.divr = divr
        self.shift = shift # <-- only shift is new. The rest is already in bsm.Model class definition

    def price(self, strike, spot, texp=None, vol=None, cp_sign=1):
        '''
        The implementation should be very similar to that of BSM model class.
        The only difference is to add shift to strike and spot.
        Basically you want to 'reuse' the BSM price code and call something like
        
          bsm.price(strike+shift, spot+shift, texp, vol, intr=self.intr, divr=self.divr, cp_sign=cp_sign)
        '''
        return bsm.price(strike+shift, spot+shift, texp, vol, intr=self.intr, divr=self.divr, cp_sign=cp_sign)
    
    def delta(self, strike, spot, texp=None, vol=None, cp_sign=1):
        ''' 
        Same here! You want to reuse the BSM delta !!
        '''
        return 0

    def vega(self, strike, spot, texp=None, vol=None, cp_sign=1):
        ''' 
        Same here! You want to reuse the BSM delta !!
        '''
        return 0

    def gamma(self, strike, spot, texp=None, vol=None, cp_sign=1):
        ''' 
        Same here! You want to reuse the BSM delta !!
        '''
        return 0

    def impvol(self, price_in, strike, spot, texp=None, cp_sign=1):
        ''' 
        Same here! You want to reuse the BSM delta !!
        '''
        return 0