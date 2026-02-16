import sys
import gym
import numpy as np

def test_gym_initialization():
    try:
        # Create a classic environment
        env = gym.make('CartPole-v1')
        obs = env.reset()
        
        # In modern NumPy 2.0, legacy code that checks 'np.bool' or 'np.float' 
        # inside the gym engine will throw an AttributeError.
        # We also verify the observation is a valid numpy array.
        if isinstance(obs, np.ndarray) and obs.shape == (4,):
            print("✅ Validation Passed: Gym CartPole initialized correctly.")
            return True
        else:
            print("❌ Validation Failed: Observation format mismatch.")
            sys.exit(1)
            
    except AttributeError as e:
        print(f"❌ Validation Failed: NumPy 2.0+ incompatibility detected. {e}")
        sys.exit(1)
    except Exception as e:
        print(f"❌ Validation Failed: Runtime error. {e}")
        sys.exit(1)

if __name__ == "__main__":
    test_gym_initialization()