from gym.envs.registration import register

register(
    id='mppt-v0',
    entry_point='gym_mppt.envs:MpptEnv',
)
''' register(
    id='mppt-extrahard-v0',
    entry_point='gym_mppt.envs:MpptExtraHardEnv',
)
'''
