import functools
import sys
import time
import warnings

__author__ = 's.rozhin'
trace_on = True


def trace(func):
    @functools.wraps(func)
    def inner(*args, **kwargs):
        print(func.__name__, args, kwargs)
        return func(*args, **kwargs)

    return inner if trace_on else func


def timethis(func):
    @functools.wraps(func)
    def inner(*args, **kwargs):
        start = time.clock()
        res = func(*args, **kwargs)
        print("Func time is %f" % (time.clock() - start))
        return res
    return inner


def call_count(func):
    @functools.wraps(func)
    def inner(*args, **kwargs):
        inner.calls_count += 1
        print("%s calls count %d" % (func.__name__, inner.calls_count))
        return func(*args, **kwargs)
    inner.calls_count = 0
    return inner


def once(func):
    @functools.wraps(func)
    def inner(*args, **kwargs):
        if not inner.called:
            inner.result = func(*args, **kwargs)
            inner.called = True
        return inner.result
    inner.called = False
    inner.result = None
    return inner


def obsolete(func):
    code = func.__code__
    warnings.warn_explicit(
        func.__name__ + " is obsolete.",
        category=DeprecationWarning,
        filename=code.co_filename,
        lineno=code.co_firstlineno + 1)
    return func


def handeled_trace(handle):
    def decorator_factory(func):
        @functools.wraps(func)
        def inner(*args, **kwargs):
            inner.calls += 1
            handle.write("Calls count {}\n".format(inner.calls))
            handle.write("%s args is %d %d\n" % (func.__name__, len(args), len(kwargs.items())))
            return func(*args, **kwargs)
        inner.calls = 0

        return inner if trace_on else func

    return decorator_factory


def pre_validate(cond, message):
    def decorator_factory(func):
        @functools.wraps(func)
        def inner(*args, **kwargs):
            assert cond(*args, **kwargs), message
            return func(*args, **kwargs)
        return inner
    return decorator_factory


def post_validate(cond, message):
    def decorator_factory(func):
        @functools.wraps(func)
        def inner(*args, **kwargs):
            res = func(*args, **kwargs)
            assert cond(res), message
            return res
        return inner
    return decorator_factory


@call_count
@handeled_trace(sys.stderr)
def simple_func(x):
    print("I'm a simple func")
    return x + 2


@timethis
def sleeping_func():
    time.sleep(1)
    return 1


@obsolete
def obsolete_func():
    print("ololo")


@pre_validate(lambda num: num is not None, "num should be digit")
def print_num(num):
    print(num)


def sum_two(one, two):
    return one + two

sum_one = functools.partial(sum_two, 42)


@post_validate(lambda x: x is not None, "Should not return None")
def return_none():
    return None


# @functools.singledispatch # doesn't work in 2.7
def print_type(obj):
    type_name = type(obj).__name__
    print("Unknown type name" + type_name)


# @print_type.register(int)  # doesn't work in 2.7
def _(obj):
    print("Type is int")


# @print_type.register(str)  # doesn't work in 2.7
def _(obj):
    print("Type is string")


if __name__ == '__main__':
    print(simple_func(22))
    print(simple_func(6))
    print(simple_func.__name__)
    print(sleeping_func())
    obsolete_func()
    print_num(1)
    # print_num(None) # AssertionError: num should be digit
    # return_none() # AssertionError: Should not return None
    print(sum_one(33))
    print_type(22)
    print_type("aa")
    print_type(22.3)
    print(functools.reduce(lambda acc, x: acc - x, [1, 2, 3, 4], 0))
