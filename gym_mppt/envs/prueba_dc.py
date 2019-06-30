from gym_mppt.envs.pvmodel import Panel
from gym_mppt.envs.dc_control import DCcontrol
#rama1
Vg = 10

pv = Panel()
state = pv.calc_pv(Vg)

dc_controller = DCcontrol()
alpha = 0.5

V1 = dc_controller.dcdc("buck", state[1], alpha)
V2 = dc_controller.dcdc("boost", state[1], alpha)
V3 = dc_controller.dcdc("buck-boost", state[1], alpha)

print(V1, V2, V3)