# итераторы по умолчанию
class Identity:
    def __getitem__(self, i):
        if i > 5:
            raise IndexError(i)
        return i


def chain(*iterables):
    for iterable in iterables:
        yield from iterable
        # same as:
        for i in iterable:
            yield i


def unique(iterable, seen=None):
    seen = set(seen or [])
    for item in iterable:
        if item not in seen:
            seen.add(item)
            yield item


def recieving_send():
    got = yield 1
    print(got)
    yield

# will newer raise stop iteration exception
def grep_coroutine(pattern):
    print("looking for {!r}".format(pattern))
    while True:
        line = yield
        if pattern in line:
            print(line)

def main():
    for a in Identity():
        print(a)
    print("len:{}".format(len(list(Identity()))))

    some_iterator = iter([1, 2, 3])
    for x in some_iterator: pass
    print(list(some_iterator))
    print(list(chain([1, 2, 3, 4], ["a", "b", "c"])))
    print(list(enumerate("abcd")))
    print(list(x*x for x in range(10) if x % 2 == 1))
    generator = recieving_send()
    next(generator) #= generator.send(None)
    generator.send("ololo")
    coroutine = grep_coroutine("star")
    next(coroutine) # initializing generator
    coroutine.send("snow")
    coroutine.send("stars")
    from itertools import count
    print(list(zip(count(),"abcd")))


if __name__ == "__main__":
    main()
