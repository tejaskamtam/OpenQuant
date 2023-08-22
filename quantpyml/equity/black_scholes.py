
from scipy.stats import norm
import numpy as np

class BlackScholes:
    def __init__(self, price, strike, expiration: "T-days", vol: "annualized constant volatility", rate: "risk free rate" = 0.03, div: "dividend"=0):
        self.S = price
        self.K = strike
        self.T = expiration/365
        self.r = rate
        self.sigma = vol
        self.q = div
        
    
    @staticmethod
    def N(x):
        return norm.cdf(x)
    
    @property
    def params(self):
        return {'S': self.S, 
                'K': self.K, 
                'T': self.T, 
                'r':self.r,
                'q':self.q,
                'sigma':self.sigma}
    
    def d1(self):
        return (np.log(self.S/self.K) + (self.r -self.q + self.sigma**2/2)*self.T) / (self.sigma*np.sqrt(self.T))
    
    def d2(self):
        return self.d1() - self.sigma*np.sqrt(self.T)
    
    def _call_value(self):
        return self.S*np.exp(-self.q*self.T)*self.N(self.d1()) - self.K*np.exp(-self.r*self.T) * self.N(self.d2())
                    
    def _put_value(self):
        return self.K*np.exp(-self.r*self.T) * self.N(-self.d2()) - self.S*np.exp(-self.q*self.T)*self.N(-self.d1())
    
    def price(self, type_: "call (C), put (P), or both (B)" = 'C'):
        if type_ == 'C':
            return self._call_value()
        if type_ == 'P':
            return self._put_value() 
        if type_ == 'B':
            return  {'call': self._call_value(), 'put': self._put_value()}
        else:
            raise ValueError('Unrecognized type')

