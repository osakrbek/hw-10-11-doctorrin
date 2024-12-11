"""
💎 Exercise-1: Memoized Fibonacci
Implement a memoized version of the Fibonacci sequence. The function "memoized_fibonacci(n: int) -> int" should return the nth number in the Fibonacci sequence, and it should use a cache to improve performance on subsequent calls.

Example:
memoized_fibonacci(10) -> 55
"""


def memoized_fibonacci(n: int) -> int:
    cache = {}

    def fib(n):
        if n in cache:
            return cache[n]
        if n <= 1:
            return n
        cache[n] = fib(n - 1) + fib(n - 2)  # Memoize the result
        return cache[n]

    return fib(n)


"""
💎 Exercise-2: Currying Function
Write a function "curry(func, *args)" that implements currying. The function should return a new function that when called will return the result of applying the input function to the provided arguments, followed by the new arguments.

Example:
def add_three_numbers(a, b, c):
    return a + b + c
add_five_and_six = curry(add_three_numbers, 5, 6)
add_five_and_six(7) -> 18
"""


def curry(func, *args):
    def curried(*more_args):
        return func(*args, *more_args)  # Combine the pre-applied args and new args

    return curried


"""
💎 Exercise-3: Implement zip() using map() and lambda
Write a function "my_zip(*iterables)" that takes in multiple iterables and returns an iterator that aggregates elements from each of the iterables.

Example:
my_zip([1, 2, 3], [4, 5, 6]) -> [(1, 4), (2, 5), (3, 6)]
"""


def my_zip(*iterables):
    return map(lambda *args: tuple(args), *iterables)  # Use map and lambda to aggregate


"""
💎 Exercise-4: Caching Decorator
Write a decorator "caching_decorator(func)" that caches the results of the function it decorates.

Example:
@caching_decorator
def expensive_function(x, y):
    # Simulate an expensive function by sleeping
    import time
    time.sleep(5)
    return x + y
"""


def caching_decorator(func):
    cache = {}

    def wrapper(*args, **kwargs):
        key = (args, tuple(kwargs.items()))
        if key not in cache:
            cache[key] = func(*args, **kwargs)  # Cache the result
        return cache[key]

    return wrapper


"""
💎 Exercise-5: Recursive Flattening
Write a function "recursive_flatten(input_list: list) -> list" that takes a nested list and flattens it.

Example:
recursive_flatten([1, [2, [3, 4], 5]]) -> [1, 2, 3, 4, 5]
"""


def recursive_flatten(input_list: list) -> list:
    result = []
    for item in input_list:
        if isinstance(item, list):
            result.extend(recursive_flatten(item))  # Recursively flatten nested lists
        else:
            result.append(item)
    return result


"""
💎 Exercise-6: Decorator for Checking Function Arguments
Write a decorator "check_args(*arg_types)" that checks the types of the arguments passed to the function it decorates.

Example:
@check_args(int, int)
def add(a, b):
    return a + b
"""


def check_args(*arg_types):
    def decorator(func):
        def wrapper(*args, **kwargs):
            for i, (arg, arg_type) in enumerate(zip(args, arg_types)):
                if not isinstance(arg, arg_type):
                    raise TypeError(
                        f"Argument {i + 1} must be of type {arg_type.__name__}"
                    )
            return func(*args, **kwargs)

        return wrapper

    return decorator
