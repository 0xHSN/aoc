from collections import Counter

with open('input','r') as f:
    l = list(map(str.strip, f.readlines()))

gamma = int("".join([Counter(x).most_common()[-1][0][0] for x in list(zip(*l))]), 2)
epsilon = int(len(l[0])*'1', 2) - gamma

print(gamma*epsilon)

