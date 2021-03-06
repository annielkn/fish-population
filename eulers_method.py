import numpy as np
import matplotlib.pyplot as plt


# solution for dP/dt = 0.7 * P

Dt = 0.1
P_init = 10
t_init = 0
t_end = 5
n_steps = int(round((t_end-t_init)/Dt))

P_arr = np.zeros(n_steps + 1)
t_arr = np.zeros(n_steps + 1)

P_arr[0] = P_init
t_arr[0] = t_init

for i in range (1, n_steps + 1):
    P = P_arr[i-1]
    t = t_arr[i-1]
    dPdt = 0.7*P
    P_arr[i] = P + Dt * 0.7 * P
    t_arr[i] = t + Dt
    
