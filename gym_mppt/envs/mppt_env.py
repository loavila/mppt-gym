import gym
from gym import error, spaces, utils
from gym.utils import seeding
import numpy as np
#


class MpptEnv(gym.Env):
    metadata = {
        'render.modes': ['human']
        # normal = AI plays, renders at 35 fps (i.e. would be used to watch AI play)
        # human = Human plays the level to get better acquainted with level, commands, and variables
    }

    def __init__(self, type_panel):

        if type_panel == 1:
            self.Vocr = 36.6
            self.Iscr = 7.97
            self.Vmppr = 29.3
            self.Imppr = 7.47
            self.niscT = .0010199
            self.nvocT = -.00361
        elif type_panel == 2:
            self.Vocr = 73.2
            self.Iscr = 7.97
            self.Vmppr = 58.6
            self.Imppr = 7.47
            self.niscT = .0010199
            self.nvocT = -.00361
        elif type_panel == 3:
            self.Vocr = 73.2
            self.Iscr = 15.94
            self.Vmppr = 58.6
            self.Imppr = 14.94
            self.niscT = .0010199
            self.nvocT = -.00361
        elif type_panel == 4:
            self.Vocr = 366
            self.Iscr = 71.73
            self.Vmppr = 293
            self.Imppr = 67.23
            self.niscT = .0010199
            self.nvocT = -.00361


        self.reward_range = (-float('inf'), float('inf'))
        # spec = None

        self.min_action = -1.0
        self.max_action = 1.0

        self.action_space = spaces.Box(low=self.min_action, high=self.max_action,
                                       shape=(1,), dtype=np.float32)
        self.observation_space = None

        self.seed()

    def seed(self, seed=None):
        self.np_random, seed = seeding.np_random(seed)
        return [seed]

    def step(self, action):
        """
        Parameters
        ----------
        action :

        Returns
        -------
        ob, reward, episode_over, info : tuple
            ob (object) :
                an environment-specific object representing your observation of the environment.
            reward (float) :
                amount of reward achieved by the previous action.
            episode_over (bool) :
                whether it's time to reset the environment again.
            info (dict) :
                 diagnostic information useful for debugging. It can sometimes
                 be useful for learning.
        """
        # self._take_action(action)
        # self.status = self.env.step()
        # reward = self._get_reward()
        # ob = self.env.getState()
        # episode_over = self.status != 0
        # return ob, reward, episode_over, {}
        pass

    def reset(self):
        pass

    def render(self, mode='human', close=False):
        pass

    def take_action(self, action):
        pass

    def get_reward(self):
        if self.status == 0:
            return 1
        elif self.status == 1:
            return self.somestate ** 2
        else:
            return 0
        ...
