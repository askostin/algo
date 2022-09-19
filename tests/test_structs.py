from algo.structs import *
from algo.tests.test import general_test
import random

# testin Heap_min
a1 = Heap_min()
for x in random.sample([1, 2, 3, 10], 4):
	a1.insert(x)
print(a1.values)
print(a1.size)
a1.extract_min()
print(a1.values)
print(a1.size)

a2 = Heap_min()
for x in random.sample([10, 15, 30, 40, 40, 50, 100], 7):
	a2.insert(x)
print(a2.values)
print(a2.size)
a2.extract_min()
print(a2.values)
print(a2.size)
