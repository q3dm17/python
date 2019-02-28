import functools
from os.path import dirname


class Counter:
    """Here is the description of the class"""
    all_instances = []
    _internal_attribute = "123"
    __very_internal_attribute = "*"

    def __init__(self, initial=0):
        self.value = initial
        Counter.all_instances.append(self)

    def inc(self):
        self.value += 1

    def get(self):
        return self.value


print(Counter()._Counter__very_internal_attribute)
print(Counter()._internal_attribute)
print(Counter.__doc__)
print(Counter.__name__)
print(Counter.__module__)
print(Counter().__dict__)
# print Counter.__class__
print(Counter.__dict__)

from collections import deque


class DictWithHistory(dict):
    history = deque(maxlen=10)

    def __init__(self, iterable=None, **kwargs):
        self.instance_history = deque(maxlen=10)
        super(DictWithHistory, self).__init__([] if iterable is None else iterable, **kwargs)

    def set(self, key, value):
        self.history.append(key)
        self.instance_history.append(key)
        self[key] = value

    def get_history(self):
        return [self.history, self.instance_history]


one_d = DictWithHistory()
sec_d = DictWithHistory()
one_d.set("a", 1)
sec_d.set("b", 2)
print(sec_d.get_history())
print(DictWithHistory.__bases__)
print(vars(DictWithHistory()))


class StrictTypedClass(object):
    __slots__ = ["only_attribute"]


ex = StrictTypedClass()
ex.only_attribute = 22
print(ex.only_attribute)


#  Fails:
#  ex.another_attribute = 23
#  print ex.another_attribute

class Path:
    def __init__(self, current):
        self.current = current

    def __repr__(self):
        return "Path:({})".format(self.current)

    @property
    def parent(self):
        return Path(dirname(self.current))


p = Path("C:/Users/admin/file.txt")
print(p.parent())


class SomeDataModel(object):
    def __init__(self):
        self._params = []

    @property
    def params(self):
        return self._params

    @params.setter
    def params(self, new_params):
        assert all(map(lambda p: p > 0, new_params))
        self._params = new_params

    @params.deleter
    def params(self):
        del self._params


datas = SomeDataModel()
datas.params = [1, 2, 3.2]
print(datas.params)


# datas.params = [1, -2, 3.2] throws an error


class Parent(object):
    def __init__(self):
        print("Initiating parent")
        self.name = "Name from parent"


class Child(Parent):
    def get_name(self):
        return self.name


class AnotherChild(Parent):
    def __init__(self):
        print("Initiating AnotherChild")
        super(AnotherChild, self).__init__()
        print("Initiated AnotherChild")


child = Child()
# Looks for attribute in exemplar, than in class, then same for parent class
print(child.name)
another_child = AnotherChild()
print(isinstance(another_child, Parent))
print(isinstance(another_child, Child))
print(AnotherChild.mro())


def singleton(cls):
    instance = None

    @functools.wraps(cls)
    def inner(*args, **kwargs):
        instance = [None]
        if instance[0] is None:
            instance[0] = cls(*args, **kwargs)
        return instance[0]

    return inner


@singleton
class NoClass:
    def __init__(self):
        pass


print(id(NoClass()))
print(id(NoClass()))
setattr(NoClass(), "some_attr", 23)
print(getattr(NoClass(), "some_attr", 2))
print(getattr(NoClass(), "some_other_attr", 2))


class Noop:
    def __getattr__(self, item):
        return item


print(Noop().some_unexisting_attribute)

print("".__eq__("a"))


@functools.total_ordering
class Money:
    def __init__(self, rubles, kopeck):
        self.rub = rubles
        self.kop = kopeck

    def __eq__(self, other):
        return self.rub == other.rub and self.kop == self.kop

    def __lt__(self, other):
        if self.rub == other.rub:
            return self.kop < other.kop
        else:
            return self.rub < other.rub

    def __str__(self):
        return "{}.{:02d}".format(self.rub, self.kop)

    def __format__(self, format_spec):
        return str(self)

    def __nonzero__(self):
        return self.rub > 0 or (self.rub == 0 and self.kop > 0)

    def __len__(self):
        return 0

    # not do like this because of mutability
    def __hash__(self):
        return hash(self.kop) + hash(self.rub)


print(Money(11, 2) >= Money(11, 4))
print(Money(11, 4) >= Money(11, 4))
print(Money(11, 4))
print(Money(11, 43))
print(hash(Money(11, 43)))
if not Money(-1, -21):
    print("Have no money((")

if Money(1, 21):
    print("Have a money!")
