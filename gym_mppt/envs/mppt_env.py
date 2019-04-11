import gym
from gym import error, spaces, utils
from gym.utils import seeding


class MpptEnv(gym.Env):
  metadata = {
    'render.modes': ['human']
  }

  def __init__(self):
    pass

  def step(self, action):
    """
    Parameters
    ----------
    action :

    Returns
    -------
    ob, reward, episode_over, info : tuple
        ob (object) :
            an environment-specific object representing your observation of the environment.
        reward (float) :
            amount of reward achieved by the previous action.
        episode_over (bool) :
            whether it's time to reset the environment again.
        info (dict) :
             diagnostic information useful for debugging. It can sometimes
             be useful for learning.
    """
    # self._take_action(action)
    # self.status = self.env.step()
    # reward = self._get_reward()
    # ob = self.env.getState()
    # episode_over = self.status != 0
    # return ob, reward, episode_over, {}
    pass

  def reset(self):
    pass

  def render(self, mode='human', close=False):
    pass

  def take_action(self, action):
    pass

  def get_reward(self):
    if self.status == 0:
      return 1
    elif self.status == 1:
      return self.somestate ** 2
    else:
      return 0
    ...
