import abc  # ABC stands for 'Abstract' Base Class
import numpy as np
import scipy.stats as ss

'''
This is an example abstrac base class for all model class
Below, define all methods that any option pricing model should have
'''

class ModelBase(abc.ABC):
    @abc.abstractmethod
    def price(self): pass
    
    @abc.abstractmethod
    def delta(self): pass
    
    @abc.abstractmethod
    def vega(self): pass

'''
The subclass inheriting an ABC should implement all abstract methods
'''

class Model(ModelBase):
    texp, vol, intr, divr = None, None, None, None
    n_path = 10000
    
    def __init__(self, texp, vol, intr=0, divr=0):
        self.texp = texp
        self.vol = vol
        self.intr = intr
        self.divr = divr
    
    def price(self, strike, spot, texp=None, vol=None, cp_sign=1):
        # pas vol and texp if you don't want to use values stored in class
        vol = self.vol if(vol is None) else vol
        texp = self.texp if(texp is None) else texp
        price_t = spot + vol*np.sqrt(texp)*np.random.normal(size=self.n_path)
        
        price = np.mean(np.fmax(cp_sign*(price_t - strike), 0))
        return price
    '''
    def delta(self):
        return 0
    
    def vega(self):
        return 0
    '''