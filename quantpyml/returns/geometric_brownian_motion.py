# implementation of geometric brownian motion

import numpy as np

def geometric_brownian_motion(nsims=10, ksteps: "number of time steps"=1000, t: "time step" = 1, mu: "drift or mean" = 0.0001, sigma: "scaling or standard deviation" = 0.02):
    """
    Weiner process: W(t) ~ N(0,t)
    Brownian Motion: X(t) = X0 + mu*t + sigma*W(t)
    Standard Brownian Motion: X(t) = X0 + W(t)
    Geometric Brownian Motion: X(t) = X0 + exp((u-sigma^2/2)*t + sigma*W(t))
    """
    def X():
        return (mu-sigma**2/2)*t + sigma*np.random.normal(loc=0, scale=np.sqrt(t), size=ksteps)
    x = np.array([i*t for i in range(ksteps)])
    sims = []
    for i in range(nsims):
        y = np.exp(np.cumsum(X()))
        sims.append(y)
    return sims, x

