from algo.structs import *
from algo.tests.test import general_test
import random

# testin Heap_min
a1 = Heap_min()
for x in random.sample([1, 2, 3, 10], 4):
	a1.insert(x)
print(a1.values)
a1.extract_min()
print(a1.values)

print('##########')

a2 = Heap_min()
for x in [1, 2, 4, 5, 3, 4, 8]:
	a2.insert(x)
print(a2.values)
a2.extract_min()
print(a2.values)
