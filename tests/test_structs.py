from algo.structs import *
from algo.tests.test import general_test
import random

print('\nTesting Heap_min:')
h1 = Heap_min()
a1 = random.sample([1, 2, 3, 10], 4)
for x in a1:
	h1.insert(x)
print(h1.values)
h1.extract_min()
print(h1.values)

print('##########')

h2 = Heap_min()
a2 = [1, 2, 4, 5, 3, 4, 8]
for x in a2:
	h2.insert(x)
print(h2.values)
h2.extract_min()
print(h2.values)

print('\nTesting Heap_max:')
h3 = Heap_max()
a3 = random.sample([1, 2, 3, 10], 4)
for x in a3:
	h3.insert(x)
print(h3.values)
h3.extract_max()
print(h3.values)

print('##########')

h4 = Heap_max()
a4 = [1, 2, 4, 5, 3, 4, 8]
for x in a4:
	h4.insert(x)
print(h4.values)
h4.extract_max()
print(h4.values)
