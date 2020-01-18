from gym_mppt.envs.pvmodel import Panel
import numpy as np
import matplotlib.pyplot as plt

# Parameters
T = 25  # in celsius degrees
Iscr = 3.75  # SC Current at ref. temp in A
Iscr_sh = 0.375
Voc = 21  # volts
Mp = 10  # Modules in parallel
Ms = 1  # Modules in series
Ng = [40, 38, 22]  # Parallel-connected series assemblies
SH = [4, 10, 7, 10, 10, 10]  # Shaded modules
G = [1000, 100]  # Irradiance
G_ar = np.array(G)

# Solar radiation in mW/sq.cm
V0 = list(range(0, Voc*Mp+1))
IUN = []
ISH = []
Vpv = V0
Ipv = []
Vpv_ar = np.array(Vpv)

pv = Panel()

b = len(list(range(len(SH))))/2
c = list(range(0, int(b)))

for j in (range(len(c))):
    IUN.append([])
    ISH.append([])
    for i in range(len(V0)):
        IUN_i = pv.calc_pv(G_ar[0], T, Vpv[i], SH[j*2])[0]
        IUN[j].append(IUN_i)
        ISH_i = pv.calc_pv(G_ar[1], T, Vpv[i], SH[j*2+1])[0]
        ISH[j].append(ISH_i)

        if IUN[j][i] < 0:
            IUN[j][i] = 0
        if ISH[j][i] < 0:
            ISH[j][i] = 0


for j2 in (range(len(c))):
    Ipv.append([])
    for i2 in range(len(Vpv)):
        if IUN[j2][i2] > Iscr_sh:
            Ipv_i = IUN[j2][i2]
            Ipv[j2].append(Ipv_i)
        else:
            Ipv_i = ISH[j2][i2]
            Ipv[j2].append(Ipv_i)

Ipv_ar=np.array(Ipv)

# Figure 1 (Characteristics of the PV modules under different insolation levels)
plt.subplot(1, 2, 1)
plt.plot(Vpv_ar/SH[0], IUN[0][:])
plt.plot(Vpv_ar/SH[1], ISH[0][:])
plt.xlabel('Voltage (V)')
plt.ylabel('Current (A)')
plt.subplot(1, 2, 2)
plt.plot(Vpv_ar/SH[0], IUN[0][:]*Vpv_ar/SH[0])
plt.plot(Vpv_ar/SH[1], ISH[0][:]*Vpv_ar/SH[1])
plt.xlabel('Voltage (V)')
plt.ylabel('Power (W)')
plt.show()

# Figure 2 (Characteristics of series assemblies with different insolation levels)
plt.subplot(1, 2, 1)
plt.plot(Vpv_ar, Ipv_ar[0])
plt.plot(Vpv_ar, Ipv_ar[1])
plt.plot(Vpv_ar, Ipv_ar[2])
plt.plot()
plt.xlabel('Voltage (V)')
plt.ylabel('Current (A)')
plt.subplot(1, 2, 2)
plt.plot(Vpv_ar, Ipv_ar[0]*Vpv_ar)
plt.plot(Vpv_ar, Ipv_ar[1]*Vpv_ar)
plt.plot(Vpv_ar, Ipv_ar[2]*Vpv_ar)
plt.xlabel('Voltage (V)')
plt.ylabel('Power (W)')
plt.show()

# Figure 3 (Characteristics of the groups)
plt.subplot(1, 2, 1)
plt.plot(Vpv_ar, Ipv_ar[0]*Ng[0])
plt.plot(Vpv_ar, Ipv_ar[1]*Ng[1])
plt.plot(Vpv_ar, Ipv_ar[2]*Ng[2])
plt.plot()
plt.xlabel('Voltage (V)')
plt.ylabel('Current (A)')
plt.subplot(1, 2, 2)
plt.plot(Vpv_ar, Ipv_ar[0]*Vpv_ar*Ng[0])
plt.plot(Vpv_ar, Ipv_ar[1]*Vpv_ar*Ng[1])
plt.plot(Vpv_ar, Ipv_ar[2]*Vpv_ar*Ng[2])
plt.xlabel('Voltage (V)')
plt.ylabel('Power (W)')
plt.show()

# Figure 4 (Output characteristics of the array)
plt.subplot(1, 2, 1)
plt.plot(Vpv_ar, Ipv_ar[0]*Ng[0]+Ipv_ar[1]*Ng[1]+Ipv_ar[2]*Ng[2])
plt.plot()
plt.xlabel('Voltage (V)')
plt.ylabel('Current (A)')
plt.subplot(1, 2, 2)
plt.plot(Vpv_ar, Ipv_ar[0]*Ng[0]*Vpv_ar+Ipv_ar[1]*Ng[1]*Vpv_ar+Ipv_ar[2]*Ng[2]*Vpv_ar)
plt.xlabel('Voltage (V)')
plt.ylabel('Power (W)')
plt.show()