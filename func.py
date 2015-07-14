import random

names = ['Masha', 'Petya', 'Vasia']
code_names = ['Jokie', 'Vintik', 'Funtic']
func_secret_names = map(lambda x: code_names[abs(hash(x))%len(code_names)], names)

for i in range(len(names)):
    names[i] = random.choice(code_names)
print "names"
print names
print "func_secret_names"
print func_secret_names


joiner = reduce(lambda a,x: a + x, [0,1,2,3,4],12)
print joiner