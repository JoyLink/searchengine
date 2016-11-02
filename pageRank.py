#what is the algorithm?
#how to design the data structure to help implement this algorithm
#this code is cite from http://blog.csdn.net/wiking__acm/article/details/49387847


from math import fabs
from time import time

data = open('web-Google.txt')
total_page_number = 875713
damping_factor = 0.8
tentominussix = 1e-6
currentstate = [1. / total_page_number for i in range(total_page_number)]
laststate = [1. / total_page_number for i in range(total_page_number)]
out_degree = [0 for i in range(total_page_number)]
precursor = [[] for i in range(total_page_number * 2)]
hash_table = [-1 for i in range(total_page_number * 2)]
idx = 0


def hash(x):
    global idx
    if hash_table[x] == -1:
        hash_table[x] = idx
        idx += 1
    return hash_table[x]


data.readline()
data.readline()
data.readline()
data.readline()
for line in data:
    x, y = map(hash, map(int, line.split()))
    out_degree[x] += 1
    precursor[y].append(x)

print 'data loaded'
print 'start iterating...'

iterationcnt = 0
begin = time()

while True:
    for i in range(total_page_number):
        currentstate[i] = 0
        for in_id in precursor[i]:
            currentstate[i] += damping_factor * laststate[in_id] / out_degree[in_id]
    der = 1 - sum(currentstate)
    for i in range(total_page_number):
        currentstate[i] += der / total_page_number

    tag = 0
    for i in range(total_page_number):
        if fabs(currentstate[i] - laststate[i]) > tentominussix:
            tag = 1
            break
    for i in range(total_page_number):
        laststate[i] = currentstate[i]
    iterationcnt += 1
    if tag == 0:
        break

end = time()
print currentstate[hash(99)]
print 'total iteration is %d' % iterationcnt
print 'total time is %f' % (end - begin)