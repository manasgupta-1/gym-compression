from gym.envs.registration import register

register(
    id='compression-v0',
    entry_point='gym_compression.envs:CompressionEnv',
)