**Installation**
``` bash
    cd mppt-gym
    pip install -e .
```

**Using the environment**

### Unshaded model
Run in a Python script:

``` bash
    import gym
    import gym_mppt
    env = gym.make('mppt-v0')
```

### Partial shaded model
Run in a Python script:

``` bash
    import gym
    import gym_mppt
    env = gym.make('mppt_shaded-v0')
```

