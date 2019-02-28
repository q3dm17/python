# coding=utf-8
from collections import namedtuple

date = "October", 12
print date
print ("string")  # не кортеж
print ("str",)  # кортеж
person = ("George", "Washington", "May", 12, 1822)
name, birthday = person[:2], person[2:]
print name
print birthday
NAME, BIRTHDAY = slice(2), slice(2, None)
print NAME
print BIRTHDAY
print person[NAME]
print person[BIRTHDAY]

print (1, 2, 3)[::-1]
print tuple(reversed((1, 2, 3)))

xs, xy = (1, 2), (3, 4)
print (id(xs), id(xy), id(xs + xy))
print (1, 2, 3) < (1, 2, 5)
print (1, 2, 3) < (1, 2)
print (1, 2, 3) < (1, 2, "4")
print (1, 2, 3) < (1, 2, "2")
print 3 < "2"
Pers = namedtuple("Pers", ["name", "age"])
warrior = Pers("Warrior", age=42)
print warrior._fields
print warrior.name
print warrior.age
print warrior._asdict()
paladin = warrior._replace(name="Paladin")
print paladin
print paladin + warrior  # трэш

print ["ss"] * 2
chunks = [[0]] * 2
chunks[0][0] = 42
print chunks

# нужно подумать
# [[0]] for i in range(2):

print chunks
chunks[0][0] = 24
print chunks
xs = [1, 2, 4]
xs[:2] = [0] * 2
print xs
xs.insert(-1, 3)
print xs
first = [0, 1, 2]
id_f_before = id(first)
second = [3, 4, 5]
id_s_before = id(second)
first += second
print "id_f_before {} id(first)".format("!= " if id(first) != id_f_before else "==")
print "id_s_before {} id(second)".format("!= " if id(second) != id_s_before else "==")


def f(xs):
    xs += [42]


f(xs)
f(xs)

x_empty = []
f(x_empty)
print xs

xs = [1, 2, 3]
del xs[-1:]
print xs
print xs.pop(1)

xs = [1, 2, 3]
print xs.reverse() is None
print xs
print sorted(xs)

from collections import deque

dq = deque([0], maxlen=4)
dq.append(2)
dq.appendleft(1)
print dq
print dq.popleft()
print dq.pop()
dq.append(7)
dq.append(8)
dq.append(9)
dq.append(10)
dq.append(11)
print dq

xs, ys = {1, 2}, {2, 3}
print set.intersection(xs, ys)
print xs & ys
print set.difference(xs, ys)
print xs | ys >= ys
print set.isdisjoint({1, 2}, {1, 5})
print set.isdisjoint({4, 2}, {1, 5})
some_set = {1, 3, 4}
some_set.update([7], [8, 9])
print some_set
some_set.discard(2222)
# some_set.remove(2222) throws exception
sets = {frozenset([1, 2]), frozenset([4, 5])}
print sets

d = dict(key="value")
print d
print id(d)
print id(dict(d))
print dict(d, k="v")
generated = {ch: [] for ch in "abcd"}
print generated

some_dict = {"k": "v"}
for k in set(some_dict):
    some_dict[k + "__"] = some_dict[k]
print some_dict
print some_dict.get("not_existed_key", 404)
print some_dict.setdefault("k", "existed")
print some_dict.setdefault("not_existed_key", "default_value")

from collections import defaultdict

graph = defaultdict(set, **{"a": {"b"}, "b": {"c"}})
print graph
graph["c"].add("a")
print graph

from collections import OrderedDict

from collections import Counter

c = Counter(["foo", "foo", "foo", "bar"])
c["foo"] += 1
print c
print c["boo"]
c.subtract({"foo": 2})
print c
c["new"] += 1
print c.most_common(2)
c["negative"] -= 3
print "\t".join(c.elements())
c2 = Counter(foo=2, new=42)
print c2 + c
print c & c2
print c | c2  # no negative!
