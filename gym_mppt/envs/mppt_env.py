import gym
import numpy as np
from gym import spaces
from gym.utils import seeding
#from pvmodel import Panel
from gym_mppt.envs.pvmodel import Panel


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
        self.state = None

    def seed(self, seed=None):
        self.np_random, seed = seeding.np_random(seed)
        return [seed]

    def step(self, action):
        pass
        state = self.state 
        # I,V,P = state

        tension = 10
        # PV model
        pv = Panel()
        state = pv.calc_pv(tension)

        r = self.seed()

        reward = r

        # return  next_state, reward, done, info

        return self.state, reward,

    def reset(self):
        pass

    def render(self, mode='human', close=False):
        pass

    def take_action(self, action):
        pass
