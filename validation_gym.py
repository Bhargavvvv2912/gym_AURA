import sys
import numpy as np

def test_gym_initialization():
    try:
        import gym
        env = gym.make('CartPole-v1')
        
        # Handle the Gym 0.26+ API change (Tuple vs Array)
        reset_result = env.reset()
        if isinstance(reset_result, tuple):
            obs = reset_result[0] # New API: (obs, info)
        else:
            obs = reset_result    # Old API: obs
            
        # The REAL test for NumPy 2.0: 
        # Does the observation remain a valid NumPy array? 
        # (NumPy 2.0 shifts internal types that often break legacy C-extensions)
        if isinstance(obs, np.ndarray):
            print(f"✅ Validation Passed: Gym initialized. Obs Type: {type(obs)}")
            return True
        else:
            print(f"❌ Validation Failed: Observation is {type(obs)}, not ndarray.")
            sys.exit(1)

    except AttributeError as e:
        # This is the "Attack" signature we are looking for in NumPy 2.0
        print(f"❌ Validation Failed: NumPy API Removal detected! {e}")
        sys.exit(1)
    except Exception as e:
        print(f"❌ Validation Failed: Runtime crash. {e}")
        sys.exit(1)

if __name__ == "__main__":
    test_gym_initialization()