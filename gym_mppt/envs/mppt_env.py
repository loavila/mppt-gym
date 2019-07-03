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
        self.state = np.zeros(3)
        #self.dt = 0.1 #seconds (it will be used for the reward computing)
        

    def seed(self, seed=None):
        self.np_random, seed = seeding.np_random(seed)
        return [seed]

    def step(self, action,Vg):

        pv_current = self.state[0] # Paara que se usa?
        pv_voltage = self.state[1] #es el Vg? de ser asi...ver linea 43 y 50...no me cierra
        pv_power = self.state[2] # Paara que se usa?

        #Vg = 10 # este deberiamos pasarlo como parametro o en cuando se inicia en la clase en una variable self...veremos....

        # PV and dc-dc models
        pv = Panel()
        self.state = pv.calc_pv(Vg)
        dc_controller = DCcontrol()
        alpha = action
        V = dc_controller.dcdc("buck", pv_voltage, alpha)

        # wp, wn = 1, 4
        # dP = (pv_power(i+1)-pv_power(i)) / dt
        # if dP < 0
        #    reward = wp * dP
        # elif dP >= 0
        #    reward = wn * dP

        # return  next_state, reward, done, info
        reward = 0
        done = False
        return self.state, reward, done, {}


    def reset(self):
        self.state = np.zeros(3)
        return self.state

    def render(self, mode='human', close=False):
        pass

    def take_action(self, action):
        pass
