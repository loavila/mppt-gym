from gym.envs.registration import register

register(
    id='mppt-v0',
    entry_point='gym_mppt.envs:MpptEnv',
    #kwargs={"type_panel": 1}
)

register(
    id='mppt-v1',
    entry_point='gym_mppt.envs:MpptEnv1',
    #kwargs={"type_panel": 1}
)

register(
    id='mppt-v2',
    entry_point='gym_mppt.envs:MpptEnv2',
    #kwargs={"type_panel": 1}
)
