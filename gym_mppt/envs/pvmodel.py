import numpy as np


class Panel(object):

    def __init__(self):
        self.T = 28 + 273 # cell temperature
        self.Tr1 = 40  # Reference temperature in degree fahrenheit
        self.S = 100  # Solar radiation in mW / sq.cm
        self.ki = 0.00023  # in A / K
        self.Iscr = 3.75  # SC Current at ref.temp. in A
        self.Irr = 0.000021  # in A
        self.k = 1.38065e-23  # Boltzmann constant
        self.q = 1.6022e-19  # charge of an electron
        self.A = 2.15 # ideality factor
        self.Eg0 = 1.166 # band gap energy
        self.alpha = 0.473
        self.beta = 636
        # panel composed of Np parallel modules each one including Ns photovoltaic cells connected
        self.Np = 4
        self.Ns = 60

    def calc_pv(self, vx):
        # cell reference temperature in kelvin
        Tr = ((self.Tr1 - 32) * (5 / 9)) + 273
        # band gap energy of semiconductor
        Eg = self.Eg0 - (self.alpha * self.T * self.T) / (self.T + self.beta) * self.q
        # generated photocurrent
        Iph = (self.Iscr + self.ki * (self.T - Tr)) * (self.S / 100)
        # cell reverse saturation current
        Irs = self.Irr * ((self.T / Tr) ** 3) * np.exp(self.q * Eg / (self.k * self.A) * ((1 / Tr) - (1 / self.T)))
        # panel output current
        I = self.Np * Iph - self.Np * Irs * (np.exp(self.q / (self.k * self.T * self.A) * vx / self.Ns) - 1)
        # panel output voltage
        V = vx
        # panel power
        P = vx * I

        return I,V,P