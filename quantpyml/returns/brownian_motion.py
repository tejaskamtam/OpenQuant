# implementation of arithmetic brownian motion

import numpy as np

def brownian_motion(nsims=10, ksteps: "number of time steps"=10000, t: "time step" = 0.01, mu: "drift or mean" = 0, sigma: "scaling or standard deviation" = 1):
    """
    Weiner process: W(t) ~ N(0,t)
    Brownian Motion: X(t) = mu*t + sigma*W(t)
    Standard Brownian Motion: X(t) = W(t)
    Geometric Brownian Motion: X(t) = exp[(mu-sigma^2/2)*t + sigma*W(t)]
    """
    def X():
        return mu*t + sigma*np.random.normal(loc=0, scale=np.sqrt(t), size=ksteps)
    x = np.array([i*t for i in range(ksteps)])
    sims = []
    for i in range(nsims):
        y = np.cumsum(X())
        sims.append(y)
    return sims, x
