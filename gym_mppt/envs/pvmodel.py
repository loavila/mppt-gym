import numpy as np


class Panel(object):

    def __init__(self):
        self.T = 28 + 273
        self.Tr1 = 40  # Reference temperature in degree fahrenheit
        self.S = 100  # Solar radiation in mW / sq.cm
        self.ki = 0.00023  # in A / K
        self.Iscr = 3.75  # SC Current at ref.temp. in A
        self.Irr = 0.000021  # in A
        self.k = 1.38065e-23  # Boltzmann constant
        self.q = 1.6022e-19  # charge of an electron
        self.A = 2.15
        self.Eg0 = 1.166
        self.alpha = 0.473
        self.beta = 636
        # number of cells in joules
        self.Np = 4
        self.Ns = 60

    def calc_pv(self, vx):

        Tr = ((self.Tr1 - 32) * (5 / 9)) + 273  # Reference temperature in kelvin
        Eg = self.Eg0 - (self.alpha * self.T * self.T) / (self.T + self.beta) * self.q  # band gap energy of semiconductor used4
        Iph = (self.Iscr + self.ki * (self.T - Tr)) * (self.S / 100)
        Irs = self.Irr * ((self.T / Tr) ** 3) * np.exp(self.q * Eg / (self.k * self.A) * ((1 / Tr) - (1 / self.T)))
        I = self.Np * Iph - self.Np * Irs * (np.exp(self.q / (self.k * self.T * self.A) * vx / self.Ns) - 1)
        V = vx
        P = vx * I

        return I,V,P