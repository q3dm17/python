import dis


def min(first, *args):
    """Takes minimum of args"""
    result = first
    for arg in (first,) + args:
        if arg < result:
            result = arg
    return result


def arg_test(num, **kwargs):
    for key, value in kwargs.iteritems():
        if num == value:
            print key


if __name__ == '__main__':
    print min(-8)
    print min(1, 2, 3)
    print min(*(1, 2, 3))
    print min.__doc__
    print min.__defaults__
    print 22 < 44 < 128

    arg_test(1, atat=22, ff=1)
    arg_test(2, **{"one": 22, "two": 2})
    print dict(one=22, two=2)

    x = 1
    y = 2
    print x, y
    x, y = y, x
    print x, y
    one, two, tree = "123"
    print one, two, tree
    a, (b, c) = 1, (2, 3)

    dis.dis("22<24")
    dis.dis("x=**(1,2,3)")
