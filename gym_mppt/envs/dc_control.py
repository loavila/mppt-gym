import numpy as np


class DCcontrol(object):

    def __init__(self):
        pass

    def dcdc(self, type_dc, Vg, alpha):
        self.type_dc= type_dc  # instance variable unique to each instance

        if self.type_dc == "boost":
            V = Vg / (1-alpha)
        elif self.type_dc == "buck":
            V = Vg * alpha
        elif self.type_dc == "buck-boost":
            V = Vg * (alpha / (1-alpha))

        return V
