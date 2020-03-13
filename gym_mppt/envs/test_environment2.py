import gym
import gym_mppt
import numpy as np
#from stable_baselines.common.policies import MlpPolicy
#from stable_baselines.ddpg.policies import MlpPolicy #For DDPG uncomment this line and comment the previous one
#from stable_baselines.common.vec_env import DummyVecEnv
#from stable_baselines import PPO2,DDPG
#import argparse
import matplotlib.pyplot as plt
#import pickle
#from guardar_datos import DATOS


class DATOS(object):


	def __init__(self,init_state,Temp_0,Irr_0,accion_0=0.):

		v=init_state[0]
		self.V = list([v])
		p=init_state[1]
		self.P = list([p])
		deltav=init_state[2]
		self.deltaV = list([deltav])
		self.I = list([0.])
		self.Temp = list([Temp_0])
		self.Irr = list([Irr_0])
		self.acciones = list([accion_0])
		
	def add(self,v,p,dv,i,T,irr,accion):
		self.V.append(v)
		self.P.append(p)
		self.deltaV.append(dv)
		self.I.append(i)
		self.Temp.append(T)
		self.Irr.append(irr)
		self.acciones.append(accion)



	def plotear(self):
		plt.plot(self.V,self.P)
		plt.xlabel('V (v)')
		plt.ylabel('P (w)')
		plt.title('V-P curve')
		#plt.savefig('VPcurve' + '.png')
		plt.show()

		plt.plot(self.V,self.I)
		plt.xlabel('V (v)')
		plt.ylabel('I (A)')
		plt.title('V-I curve')
		#plt.savefig('VIcurve' + '.png')
		plt.show()


		plt.plot(self.V)
		plt.xlabel('t')
		plt.ylabel('V (v)')
		#plt.savefig('Tesion' + '.png')
		plt.show()

		plt.plot(self.I)
		plt.xlabel('t')
		plt.ylabel('I (a)')
		#plt.savefig('Corriente' + '.png')
		plt.show()

		plt.plot(self.P)
		plt.xlabel('t')
		plt.ylabel('P (w)')
		#plt.savefig('Potencia' + '.png')
		plt.show()

		plt.plot(self.acciones)
		plt.xlabel('t')
		plt.ylabel('acciones (\deltaV)')
		plt.title('actions')
		#plt.savefig('Acciones' + '.png')
		plt.show()

		plt.plot(self.Temp)
		plt.xlabel('t')
		plt.ylabel('(ºC)')
		plt.title('Temperature profile')
		#plt.savefig('Temperatura' + '.png')
		plt.show()

		plt.plot(self.Irr)
		plt.xlabel('t')
		plt.ylabel('(Irradiance)')
		plt.title('Solar irradiance profile')
		#plt.savefig('Irradiancia' + '.png')
		plt.show()


   






if __name__ == '__main__':
	

	'''
	parser = argparse.ArgumentParser('deepid')
	parser.add_argument('--total_timesteps', type=int, default=2000)
	parser.add_argument('--test_steps', type=int, default=2000)
	parser.add_argument('--test_number', type=int)
	#parser.add_argument('--verbose', type=int, default=0)
	args = parser.parse_args()



	# Load the trained agent:
	#model = PPO2.load('ppO2_TrainedModel') #uncomment this line for ppo2 test
	model = DDPG.load('ddpg_TrainedModel') #uncomment this line for ddpg test
	#model = TRPO.load('trpo_TrainedModel') #uncomment this line for trpo test
	'''

	#Testing the model:
	env1 = gym.make('mppt_shaded-v0')
	#env1 = DummyVecEnv([lambda: env1])  # The algorithms require a vectorized environment to run

	init_state = env1.reset()


	Temp_0 = 25. # 25 # 25 # 27.5 # 27.5 # 29.0 # 29.0 #23. #23. # 23. 
	Irr_0 = 1000. # 1000 # 500 #1000 # 500 # 900. # 600. #800. #400 # 100.

	obs = env1.setTempIrr(init_state,Temp_0,Irr_0)

	'''
	try:
	  #f = open("demofile.txt")
	  #f.write("Lorum Ipsum")
	  obs = np.load('last_state.npy')
	  print("LEVANTO EL ULTIMO ESTADO!! ")
	except:
	  print("Something went wrong when load the last state")
	  obs = env1.reset()
	'''
	print('init_state =', obs, 'forma:',obs.shape, 'tipo', type(obs))
	datos = DATOS(obs, Temp_0, Irr_0) #tomo obs[0] dado que el estado está "empaquetado" y es una matriz de 1x3, entonces me quedo con un vector pa no cambiar grafos.
	
	action = 0 #delta V
	P=[]
	#V = []
	#I = []

	#np.save('cant_pruebas.npy',args.test_number)
	for i in range(21000):
		print ('i:',i, 'action:', action)


		#print('accion shape= ', action.shape, type(action))
		next_state, rewards, dones, info = env1.step(action) 
		#info = [{'Corriente': I_new, 'Temperatura':T, 'Irradiancia':G,'Accion':action}] es una lista con un dict adentro!! (que quilombo!!!)
		#print('******HASTA ACAAA OK!******')
		#exit()

		informacion = info #me quedo con el dict de info
		print('next_state:',next_state,next_state.shape)
		
		datos.add(next_state[0], next_state[1], next_state[2], informacion['Corriente'], informacion['Temperatura'], informacion['Irradiancia'], informacion['Accion'])
		action =0.01
		P.append(next_state[1])
		#V.append(next_state[0])
		#I.append(informacion['Corriente'])


		


		
		print('vamos bien, por la i=',i,'la corriente es:',informacion['Corriente'],'Tension:',next_state[0])
		#np.save('last_state.npy',obs)
		# y si quisiera levantar tal variable x, hacemos:
		#variable_levantada = np.load('x.npy')

	P_max = np.max(P)

	print('Pmax* = ', P_max)

	datos.plotear()



	'''
		if i==(args.test_steps-1):
			np.save('last_state.npy', next_state)
			
			#guardo el objeto:
			Name = 'obj'+ str(args.test_number) + '.save'
			#f = open(Name, 'wb')
			#cPickle.dump(datos, f)
			#f.close()

			with open(Name, 'wb') as data_file:
				pickle.dump(datos, data_file)
			
			print('Listo!')
			break

	'''



	