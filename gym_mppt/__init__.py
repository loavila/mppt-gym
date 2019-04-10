from gym.envs.registration import register

register(
    id='mppt-v0',
    entry_point='gym_mppt.envs:MpptEnv',
)
