import gym
import numpy as np
from gym import spaces
from gym.utils import seeding
from gym_mppt.envs.pvmodel import Panel
from gym_mppt.envs.dc_control import DCcontrol
import random

class MpptEnv(gym.Env):
    metadata = {
        'render.modes': ['human']
        # normal = AI plays, renders at 35 fps (i.e. would be used to watch AI play)
        # human = Human plays the level to get better acquainted with level, commands, and variables
    }

    def __init__(self):

        self.reward_range = (-float('inf'), float('inf'))
        # spec = None

        self.min_action = -20.0
        self.max_action = 20.0

        self.max_stateValue = 1000.
        self.min_stateValue = -1000.

        self.state_dim = 3
        self.action_dim = 1

        self.action_space = spaces.Box(low=self.min_action, high=self.max_action,
                                       shape=(self.action_dim,), dtype=np.float32)
        self.observation_space = spaces.Box(low=self.min_stateValue, high=self.max_stateValue,
                                       shape=(self.state_dim,), dtype=np.float32)

        self.seed()
        self.state = np.zeros((3)) # state = [[V,P,I]]
        #self.dt = 0.1 #seconds (it will be used for the reward computing)
        self.epsilon = 0.5 #It is the bandwith for the reward computing

        self.Temp = 25
        self.Irr = 100
        
    def seed(self, seed=None):
        self.np_random, seed = seeding.np_random(seed)
        return [seed]

    def step(self, action):

        # leer valor instantaneo de una serie de tiempo
        G = self.Irr #read irradiance # Solar radiation in mW / sq.cm
        T = self.Temp #read temperature (ºC) # ojo con kelvin 273

        # aca supongo que solo vamos a tener disponibles los ultimos dos valores
        '''
        sim_length = 2
        pv_current = self.state[sim_length, 0]
        pv_voltage = self.state[sim_length, 1]
        pv_power = self.state[sim_length, 2]
        '''
        pv_voltage = self.state[0]

        v0 = pv_voltage + action # valor anterior de V mas la accion dV
        v1 = max(v0,0.)
        V = min(v1,40.)

        # PV and dc-dc models
        pv = Panel()
        #self.state = pv.calc_pv(G,T,V)
        I_new, V_new, P_new = pv.calc_pv(G,T,V)  #new_state = [I,V,P]

    

        # dc_controller = DCcontrol()
        # alpha = action
        # V = dc_controller.dcdc("buck", pv_voltage, alpha)

        '''
        # aca supongo que solo vamos a tener disponibles los ultimos dos valores
        dP = self.state[1, 2] - self.state[0, 2] # pv_power(i) - pv_power(i-1)
        dV = self.state[1, 1] - self.state[0, 1] # pv_voltage(i) - pv_voltage(i-1)
        '''
        
        dV = V_new - self.state[0] # pv_voltage(i) - pv_voltage(i-1)
        dP = P_new - self.state[1] # pv_power(i) - pv_power(i-1)
        P = P_new

        #print('dv =', dV, 'dP = ', dP, 'P =', P)

               

        # ojo con el reward por que:
        # dP/dV = 0 at MPP
        # dP/dV > 0 left of MPP
        # dP/dV < 0 right of MPP

        # asi esta en el car-on-a-hill continuo
        # done = true termina el episodio

        ''' Ojo luis, porque con el done asi, el dP/Dv puede ser negativo y da que termina el episodio. Solo comenté esto. Lo hago abajo para que quede mas facil...
        done = bool(dP/dV <= epsilon)
        if done: #(dP/dV >= 0) and (dP/dV < epsilon):
            reward = wp * dP
        else:
            reward = wn * dP

        
        '''
        epsilon = self.epsilon
        #done = bool(0<= dP/dV <= epsilon)
        #done = bool(np.abs(dP/dV) <= epsilon and P>0)
        done = bool(np.abs(dP) <= epsilon and P>0)
        #print('dP/dV = ', dP/dV, 'P =', P)
        reward = self.reward_function1(dP, P,done) #Poniendo aca una funcion, despues es mas facil para jugar..porque cambiamos el nombre de la funcion y listo...y vamos agregando abajo, tantas como se nos cante...
        
        #The next state is:
        #self.state = np.array([[V_new,P_new,I_new]]) #por ahora dejamos I en el estado, pero la podriamos sacar...eventualmete la vamos guardando en una matriz variable del self, por ej: self.currents y chau (esto es por si necesitamos por algo...)
        self.state = np.array([V_new,P_new,dV])

        info = np.array([I_new,T,G,action])

        return self.state, reward, done, info


    def reset(self):
        state_dim = np.size(self.state)
        
        self.state = np.zeros(state_dim)
        
        irradiancias = list([100., 200., 300., 400., 500., 600., 700., 800., 900., 1000])
        temperaturas = list([13.5, 15., 17.5, 20., 22.5, 25., 27.5, 30., 32.5, 35])
        self.Temp = random.sample(temperaturas,1)[0] #(Elegir un random de estos) o dejar fija la T y solo variar la irr pa empezar a probar...
        self.Irr = random.sample(irradiancias, 1)[0] #random.sample(irradiancias,1) # [0.1 0.2 0.3 0.4 0.5 0.6 0.7 0.8 0.9 1.0] (Elegir un random de estos)
        return self.state

    def render(self, mode='human', close=False):
        pass

    def take_action(self, action):
        pass

    def reward_function1(self, dP, P, done):
        wp = 2.
        wn = 4.

        if done: #(dP/dV >= 0) and (dP/dV < epsilon):
            r = wp * P**2
        elif dP > 0:
            r = wp * dP
        elif P <= 0:
            r = -100000
        else:
            r = wn * dP

        return r

    def reward_function2(self, dP, P, done):
        wp = 5.
        wn = 2.

        if done: #(dP/dV >= 0) and (dP/dV < epsilon):
            r = wp * dP
        else:
            r = wn * dP

        return r

    def reward_function3(self, dP, P, done):
        #por ej usamos una gaussiana o lo q sea....

        r = 0

        return r


      

      
