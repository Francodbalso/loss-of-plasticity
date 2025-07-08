from lop.envs.slippery_ant import SlipperyAntEnv4


from gym.envs.registration import (
    register,
    load_env_plugins as _load_env_plugins,
)

# Hook to load plugins from entry points
_load_env_plugins()

register(
    id="SlipperyAnt-v4",
    entry_point="lop.envs.slippery_ant:SlipperyAntEnv4",
    max_episode_steps=1000,
    reward_threshold=6000.0,
)