people = [
    {'name': 'Masha', 'h': 160},
    {'h': 'Sasha', 'h': 80},
    {'name': 'Pasha'}]
hs = map(lambda dict: dict['h'], filter(lambda x: 'h' in x, people))
# print reduce(lambda a, x: x+a, hs) / len(hs)


def zero(s):
    if s[0] == "0":
        return s[1:]


def one(s):
    if s[0] == "1":
        return s[1:]


def rule_sequence(s, rules):
    if s is None:
        return None
    elif len(rules) == 0:
        return s
    else:
        return rule_sequence(rules[0](s), rules[1:])


print rule_sequence('0101', [zero, one, zero])
# => 1

print rule_sequence('0101', [zero, zero])
# => None


def pipeline_each(data, funcs):
    return reduce(lambda a, f: map(f, a), funcs, data)


def repls(str):
    return len(str)


def ml(a):
    return a * 2

for s in pipeline_each(["aa", "bb"], [repls, ml]):
    print s


def adddd(_d, key, value):
    from copy import deepcopy
    d = deepcopy(_d)
    d[key] = value
    return d

def assoc(_d, keys):
    from copy import deepcopy
    return reduce(lambda a, x: adddd(a, x, _d[x]), keys, {})

def call(fn, key):
    def apply_fn(record):
        return assoc(record, key, fn(record.get(key)))
    return apply_fn

def pluck(fields):
    def extract_fn(dict):
        return assoc(dict, fields)
    return extract_fn
