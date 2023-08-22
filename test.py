from quantpyml import brownian_motion
import matplotlib.pyplot as plt
import numpy as np

sims, x = brownian_motion()
# sims, x = geometric_brownian_motion()
for i in range(len(sims)):
    plt.plot(x, sims[i])
# plot a trend line for all the simulations
plt.plot(x, np.mean(sims, axis=0), color='black', linewidth=3, label='trend')
plt.xlabel('Time')
plt.ylabel('Value')
plt.title('Brownian Motion')
plt.legend()
plt.show()

