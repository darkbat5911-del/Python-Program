import time

def cache(func):
    cached_results = {}
    print("Cache initialized")
    def wrapper(*args):
        if args in cached_results:
            return cached_results[args]
        result = func(*args)
        cached_results[args] = result
        return result
    return wrapper

@cache
def long_computation(a,b):
    time.sleep(5)  # Simulate a long computation
    return a + b

print(long_computation(3, 4))  # First call, will take time
print(long_computation(3, 5))  # Second call, should return cached result