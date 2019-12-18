from gym_mppt.envs.pvmodel import Panel
import numpy as np
import matplotlib.pyplot as plt

Iscr = 3.75 # SC Current at ref. temp. in A
Iscr_sh = 0.375
Voc = 21 # volts
Mp = 10 # modules in parallel
Ms = 1 # modules in series

Vg = np.linspace(0,Voc*Mp,Voc*Mp+1)
Ipv = np.zeros(len(Vg))
Vpv = Vg

SM = [4,10] # shaded modules
G=[1000,100] # irradiance
T=25 # ambient temperature

pv = Panel()

# for j = 1:numel(G)
#     for i = 1:numel(V0)
#         Iph = (Iscr+ki*(T-Tr))*(G(j)/100);
#         Irs = Irr*((T/Tr)^3)*exp(q*Eg/(k*A)*((1/Tr)-(1/T)));
#         I0(j,i) = Np*Iph-Np*Irs*(exp(q/(k*T*A)*V0(i)*(1/SH(j))/Ns)-1);
#         if I0(j,i)< 0, I0(j,i)=0; end
#     end
# end

for i in range(G):
    for j in range(len(Vg)):

ISH = pv.calc_pv(G[0],T,Vg)[0]
for i in range(len(ISH)):
    if ISH[i]<0 : ISH[i]=0

IUN = pv.calc_pv(G[1],T,Vg)[0]
for i in range(len(IUN)):
    if IUN[i]<0 : IUN[i]=0

for i in range(len(Ipv)):
    if IUN[i] > Iscr_sh: Ipv[i] = IUN[i]
    else: Ipv[i] = ISH[i]

plt.plot(Vg, ISH, Vg, IUN)
# plt.ylim(ymax= 5, ymin = 0)
# plt.xlim(xmin=0)
plt.show()