from gym_mppt.envs.pvmodel import Panel
from gym_mppt.envs.dc_control import DCcontrol

Vg = 10

pv = Panel()
Ig, Vg, Pg = pv.calc_pv(Vg)

dc_controller = DCcontrol()
alpha = 0.5

V1 = dc_controller.dcdc("buck", Vg, alpha)
V2 = dc_controller.dcdc("boost", Vg, alpha)
V3 = dc_controller.dcdc("buck-boost", Vg, alpha)

print(V1, V2, V3)