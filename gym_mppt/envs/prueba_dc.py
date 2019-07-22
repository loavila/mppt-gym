from gym_mppt.envs.pvmodel import Panel
from gym_mppt.envs.dc_control import DCcontrol
G = 19
T = 19
Vg = 10

pv = Panel()
I, V, P = pv.calc_pv(G,T,Vg)

print('I =',I,'V =', V, 'P =', P)


#Probamos el entorno gym 'mppt-v0'
import gym
ENV_NAME = 'mppt-v0'

env = gym.make(ENV_NAME)

V = 50

estado, recompensa, done, b =env.step(V)

print('estado',estado,'DimSt = ',estado.shape, 'reward', recompensa, 'reward.shape:', recompensa.shape)
exit()


dc_controller = DCcontrol()
alpha = 0.5

V1 = dc_controller.dcdc("buck", state[1], alpha)
V2 = dc_controller.dcdc("boost", state[1], alpha)
V3 = dc_controller.dcdc("buck-boost", state[1], alpha)

print(V1, V2, V3)