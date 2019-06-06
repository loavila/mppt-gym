import gym
import tensorflow as tf
import numpy as np
from gym.utils import seeding

from gym.envs.registration import register
register(
    id='mppt-v0',
    entry_point='gym_mppt.envs:MpptEnv',
    #kwargs={"type_panel": 1}
)

env = gym.make('mppt-v0')


# Training Parameters
ACTOR_LEARNING_RATE = 0.0001
CRITIC_LEARNING_RATE =  0.001
# Soft target update param
TAU = 0.001
DEVICE ='/cpu:0'
#Utility Parameters
RANDOM_SEED = 11543521#1234
SIMULATION_LENGHT = 700


def mppt(epochs=1000):
    print('hola muchaches', epochs)

    A = 1. #observar que el punto es porque es un float...si no pongo nada, asume que es un integer y se arma quilombo
    print(type(A))

if __name__ == '__main__':

    mppt()
