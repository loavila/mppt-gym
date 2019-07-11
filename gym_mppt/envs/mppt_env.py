import gym
import numpy as np
from gym import spaces
from gym.utils import seeding
from gym_mppt.envs.pvmodel import Panel
from gym_mppt.envs.dc_control import DCcontrol


class MpptEnv(gym.Env):
    metadata = {
        'render.modes': ['human']
        # normal = AI plays, renders at 35 fps (i.e. would be used to watch AI play)
        # human = Human plays the level to get better acquainted with level, commands, and variables
    }

    def __init__(self):

        self.reward_range = (-float('inf'), float('inf'))
        # spec = None

        self.min_action = -1.0
        self.max_action = 1.0

        self.action_space = spaces.Box(low=self.min_action, high=self.max_action,
                                       shape=(1,), dtype=np.float32)
        self.observation_space = None

        self.seed()
        self.state = np.zeros((2, 3))
        #self.dt = 0.1 #seconds (it will be used for the reward computing)
        
    def seed(self, seed=None):
        self.np_random, seed = seeding.np_random(seed)
        return [seed]

    def step(self, action):

        # leer valor instantaneo de una serie de tiempo
        G = 100 #read irradiance # Solar radiation in mW / sq.cm
        T = 28 #read temperature # ojo con kelvin 273

        # aca supongo que solo vamos a tener disponibles los ultimos dos valores
        sim_length = 2
        pv_current = self.state[sim_length, 0]
        pv_voltage = self.state[sim_length, 1]
        pv_power = self.state[sim_length, 2]

        V = pv_voltage + action # valor anterior de V mas la accion dV

        # PV and dc-dc models
        pv = Panel()
        self.state = pv.calc_pv(G,T,V)

        # dc_controller = DCcontrol()
        # alpha = action
        # V = dc_controller.dcdc("buck", pv_voltage, alpha)

        # aca supongo que solo vamos a tener disponibles los ultimos dos valores
        dP = self.state[1, 2] - self.state[0, 2] # pv_power(i) - pv_power(i-1)
        dV = self.state[1, 1] - self.state[0, 1] # pv_voltage(i) - pv_voltage(i-1)

        epsilon = 0.1
        wp = 5.
        wn = 2.

        # ojo con el reward por que:
        # dP/dV = 0 at MPP
        # dP/dV > 0 left of MPP
        # dP/dV < 0 right of MPP

        if (dP/dV <= epsilon): #(dP/dV >= 0) and (dP/dV < epsilon):
            reward = wp * dP
        else:
            reward = wn * dP

        done = False
        return self.state, reward, done, {}


    def reset(self):
        self.state = np.zeros((2, 3))
        return self.state

    def render(self, mode='human', close=False):
        pass

    def take_action(self, action):
        pass
