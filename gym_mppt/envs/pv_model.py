import numpy as np
import matplotlib.pyplot as plt


# PV model

T = 28 + 273
Tr1 = 40  # Reference temperature in degree fahrenheit
Tr = ((Tr1 - 32) * (5 / 9)) + 273  # Reference temperature in kelvin
S = 100  # Solar radiation in mW / sq.cm
ki = 0.00023  # in A / K
Iscr = 3.75  # SC Current at ref.temp. in A
Irr = 0.000021  # in A
k = 1.38065e-23  # Boltzmann constant
q = 1.6022e-19  # charge of an electron
A = 2.15
Eg0 = 1.166
alpha = 0.473
beta = 636
Eg = Eg0 - (alpha * T * T) / (T + beta) * q  # band gap energy of semiconductor used

# number of cells in joules
Np = 4
Ns = 60
sim_len = 35

V0 = np.linspace(0, sim_len)
I0 = np.zeros(len(V0))
P0 = np.zeros(len(V0))


def pv(vx):
    Iph = (Iscr + ki * (T - Tr)) * (S / 100)
    Irs = Irr * ((T / Tr) ** 3) * np.exp(q * Eg / (k * A) * ((1 / Tr) - (1 / T)))
    I = Np * Iph - Np * Irs * (np.exp(q / (k * T * A) * vx / Ns) - 1)
    P = vx * I
    return I, P


for x in range(sim_len):
    I0[x], P0[x] = pv(x)

plt.subplot(211)
plt.plot(V0,I0)
plt.subplot(212)
plt.plot(V0,P0)
plt.show()
