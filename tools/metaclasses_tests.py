from collections import abc


class Meta(type):
    def some_method(cls):
        return "some_string"


class Something(metaclass=Meta):
    attr = 42


class WithoutMeta():
    pass


print(type(Something))  # <class '__main__.Meta'>
print(type(Meta))  # <class 'type'>
print(type(WithoutMeta))  # <class 'type'>
print(Something.some_method())
# print(Something().some_method())  #  AttributeError: 'Something' object has no attribute 'some_method'
print(issubclass(list, abc.Sequence))  # True
print(isinstance([], abc.Hashable))  # False


def flatten(obj):
    for item in obj:
        if isinstance(item, abc.Iterable):
            yield from flatten(item)
        else:
            yield item