from typing import Generator
from functools import lru_cache


# fibonacci with recursion (index starts at 0) - lru cache decorator for optimisation / memoization

@lru_cache()
def fib_with_recursion(n: int) -> int:
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fib_with_recursion(n - 1) + fib_with_recursion(n - 2)


result = fib_with_recursion(6)
assert result == 8


# fibonacci with generator (index starts at 1)

def fib_with_generator(n: int) -> Generator[int, None, None]:
    last = 0
    next = 1
    for a in range(n):
        yield last
        last, next = next, last + next


results = [i for i in fib_with_generator(6)]
assert results == [0, 1, 1, 2, 3, 5]


# calculate pi using π = 4/1 - 4/3 + 4/5 - 4/7 + 4/9 - 4/11...
# time complexity  O(n)
def calculate_pi(n: int):
    numerator: int = 4
    denominator: int = 1
    operator: int = 1
    pi: float = 0

    for i in range(n):
        pi += operator * (numerator / denominator)
        denominator += 2
        operator *= -1
    return pi


result = calculate_pi(100)
