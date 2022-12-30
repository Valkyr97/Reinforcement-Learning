import gymnasium as gym
import sys

def run_gym_env(env_name: str, iterations: int, mode: str = 'human', *args):
    env = gym.make(env_name, render_mode=mode)
    observation, info = env.reset()
    for _ in range(int(iterations)):
        action = env.action_space.sample()
        observation, reward, terminated, truncated, info = env.step(action)

        if terminated or truncated:
            observation, info = env.reset()
    env.close()
    
if __name__ == "__main__":
    run_gym_env("Acrobot-v1", 1000)