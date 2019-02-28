class Descr:
    def __get__(self, instance, owner):
        print("instance:{}\towner:{}".format(instance, owner))

    def __set__(self, instance, value):
        print("instance:{}\tvalue:{}".format(instance, value))

    def __delete__(self, instance):  # not "__del__" because "__del__" is destructor
        print("instance:{}".format(instance))


class cached_property():
    def __init__(self, method):
        self._method = method

    def __get__(self, instance, owner):
        if instance is None:
            return self
        value = self._method(instance)
        setattr(instance, self._method.__name__, value)
        return value


class A:
    attr = Descr()

    @cached_property
    def f(self):
        print("counting f property")
        return 11


class B(A):
    pass


if __name__ == '__main__':
    _ = A.attr
    # instance:None	owner:<class '__main__.A'>
    _ = B.attr
    # instance:None owner: < class '__main__.B'>
    _ = A().attr
    # instance:<__main__.A object at 0x0147F510>	owner:<class '__main__.A'>
    _ = B().attr
    # instance:<__main__.B object at 0x0398F810>	owner:<class '__main__.B'>
    A().attr = 42
    # instance:<__main__.A object at 0x0337F810>	value:42
    A.attr = 22  # replace descriptor
    ex = A()
    print (ex.f)
    print (ex.f)
