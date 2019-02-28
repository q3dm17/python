# coding=utf-8

import re
from collections import Counter
from functools import reduce

file_name = r"C:\work\portal.requisites\Portal.Requisites.Service\Registries\InfrastructureRegistry.cs"
f = open(file_name)
some_line = "using Portal.Service.Core.Authentication;"
print(reduce(lambda a, x: x + a, map(lambda x: x.split(" "), some_line.split(".")), []))
print(re.findall(r"\w+", u"using Portal.Service.Core.Authentication; русское слово"))
words_hist = Counter()
for l in f.readlines():
    words = re.findall(r"\w+", l)
    for word in words:
        words_hist[word.lower()] += 1
    # print l
print(words_hist)
