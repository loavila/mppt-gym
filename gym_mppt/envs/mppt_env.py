import gym
from gym import error, spaces, utils
from gym.utils import seeding
import numpy as np


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
        self.state = None

    def seed(self, seed=None):
        self.np_random, seed = seeding.np_random(seed)
        return [seed]

    def step(self, action):
        pass
        state = self.state
        V0,I0 = state

        # PV model

        T = 28 + 273
        Tr1 = 40  # Reference temperature in degree fahrenheit
        Tr = ((Tr1 - 32) * (5 / 9)) + 273  # Reference temperature in kelvin
        S = 100  # Solar radiation in mW / sq.cm
        ki = 0.00023  # in A / K
        Iscr = 3.75  # SC Current at ref.temp. in A
        Irr = 0.000021  # in A
        k = 1.38065 * 10 ** (-23)  # Boltzmann constant
        q = 1.6022 * 10 ** (-19)  # charge of an electron
        A = 2.15
        Eg0 = 1.166
        alpha = 0.473
        beta = 636
        Eg = Eg0 - (alpha * T * T) / (T + beta) * q  # band gap energy of semiconductor used

        # number of cells in joules
        Np = 4
        Ns = 60

        V0 = (0, 300, 1)

        Iph = (Iscr + ki * (T - Tr)) * ((S) / 100)
        Irs = Irr * ((T / Tr) ^ 3) * np.exp(q * Eg / (k * A) * ((1 / Tr) - (1 / T)))
        I0 = Np * Iph - Np * Irs * (np.exp(q / (k * T * A) * V0/Ns) - 1)
        P0 = V0 * I0

        dP = 0  # PV increment in dt

        wp = 1
        wn = 4

        if dP < 0:
            reward = wp * dP
        elif dP >= 0:
            reward = wn * dP

        return self.state, reward,

    def reset(self):
        pass

    def render(self, mode='human', close=False):
        pass

    def take_action(self, action):
        pass


