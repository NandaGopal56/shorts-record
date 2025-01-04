from functools import lru_cache

@lru_cache(maxsize=128)
def expensive_computation(x):
    print(f"Computing for {x}...")
    return x * x

print(expensive_computation(4))
print(expensive_computation(4))
print(expensive_computation(5))
