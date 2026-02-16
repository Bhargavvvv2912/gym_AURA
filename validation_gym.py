import sys
import numpy as np

def test_gym_death_loop():
    try:
        import gym
        env = gym.make('CartPole-v1')
        
        # 1. Handle the return tuple
        res = env.reset()
        obs = res[0] if isinstance(res, tuple) else res
        
        # 2. THE TRIPWIRE: 
        # Legacy code often checks against these specific NumPy attributes.
        # In NumPy 2.0, 'np.bool' and 'np.int' were removed entirely.
        # If the environment was built against 1.x logic, this will crash.
        
        legacy_type_check = np.bool_  # This is the modern way
        try:
            # THIS IS THE ATTACK POINT:
            # Older scripts (and some gym internals) call np.bool or np.int
            # We simulate that legacy dependency here:
            fail_check = np.bool  # <--- CRASHES in NumPy 2.0
        except AttributeError:
            print("❌ Validation Failed: NumPy 2.0 API Removal detected (np.bool is gone)!")
            sys.exit(1)

        if isinstance(obs, np.ndarray):
            print("✅ Validation Passed: Gym is functional.")
            return True

    except Exception as e:
        print(f"❌ Validation Failed: Runtime crash. {e}")
        sys.exit(1)

if __name__ == "__main__":
    test_gym_death_loop()