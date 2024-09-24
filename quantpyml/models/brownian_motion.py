# implementation of arithmetic brownian motion
import torch
from torch.nn.functional import relu

class BrownianMotion:
    @staticmethod
    def weiner_process(dt: float, T: int, N=1) -> torch.Tensor:
        """
        A purely stochastic process, equivalent to Brownian motion.

        dt: time step size
        T: number of time steps
        N: number of simulations
        """
        return torch.normal(torch.tensor(0), torch.sqrt(torch.tensor(dt)), size=(N, T))

    @staticmethod
    def ito_proces(dt: float, T: int, drift: float, volatility: float, N: int) -> torch.Tensor:
        """
        The solution of the SDE for the returns of an asset described by a time series s.t. dS = mu*dt + sigma*dW. https://en.wikipedia.org/wiki/It%C3%B4_calculus

        dt: time step size
        T: number of time steps
        mu: Drift coefficient (mean return)
        sigma: Volatility coefficient (stdev of returns)
        N: number of simulations
        t: time span
        """
        t = torch.cumsum(torch.ones(T), dim=0)
        W = BrownianMotion.weiner_process(dt, T, N).cumsum(dim=1)
        return drift*t + volatility*W
    
    @classmethod
    def brownian_motion(cls, init_price: float=0, N=1, dt=1.0, T=365) -> list[torch.Tensor]:
        """
        A purely stochastic processs, equivalent to the Weiner process. Does not depend on the underlying return or volatility. The solution of the SDE modeling such an asset's returns is St = S0 + Wt.

        init_price: initial price (S0)
        mean_return: mean of returns
        stdev_return: standard deviation of returns
        N: number of simulations
        dt: time step size
        T: number of time steps
        """
        timespan = torch.cumsum(torch.ones(T), dim=0)
        W = BrownianMotion.weiner_process(dt, T, N)
        price = relu(init_price + W, inplace=True)
        return timespan, price

    @classmethod
    def arithmetic_brownian_motion(cls, init_price: float, mean_return: float, stdev_return: float, N=1, dt=1.0, T=365) -> list[torch.Tensor]:
        """
        A stochastic process that describes the evolution of an asset's price over time given drift and volatility. The price of the asset is expected to be normally distributed with a mean return and standard deviation of returns. The SDE that describes the modeled asset's returns is dS = mu*dt + sigma*dW, where dW is the Weiner process. The solution of this SDE is St = S0 + mu*t + sigma*Wt. https://en.wikipedia.org/wiki/Geometric_Brownian_motion

        init_price: initial price (S0)
        mean_return: mean of returns
        stdev_return: standard deviation of returns
        N: number of simulations
        dt: time step size
        T: number of time steps
        """
        timespan = torch.cumsum(torch.ones(T), dim=0)
        price = relu(init_price + BrownianMotion.ito_proces(dt, T, mean_return, stdev_return, N), inplace=True)
        return timespan, price
    
    @classmethod
    def geometric_brownian_motion(cls, init_price: float, mean_return: float, stdev_return: float, N=1, dt=1.0, T=365) -> list[torch.Tensor]:
        """
        A stochastic process that describes the evolution of an asset's price over time given drift and voltility. The price of the asset is expected to be log-normally distributed with a mean return and standard deviation of returns. The SDE that describes the modeled asset's returns is dS = mu*S*dt + sigma*S*dW, where dW is the Weiner process. This SDE has the following solution for St (Price) by Itô's lemma: St = S0*exp((mu - sigma^2/2)*t + sigma*Wt). https://en.wikipedia.org/wiki/Geometric_Brownian_motion#Solving_the_SDE

        init_price: initial price (S0)
        mean_return: mean of returns for the time period (T)
        stdev_return: standard deviation of returns for the time period (T)
        N: number of simulations
        dt: time step size
        T: number of time steps (period)
        """
        timespan = torch.cumsum(torch.ones(T), dim=0)
        ito_process = BrownianMotion.ito_proces(dt, T, mean_return - stdev_return**2/2, stdev_return, N)
        price = relu(init_price*torch.exp(ito_process), inplace=True)
        return timespan, price
