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
a4 = [8, 4, 5, 1, 2, 4, 3]
for x in a4:
	h4.insert(x)
print(h4.values)
h4.extract_max()
print(h4.values)

print('##########')

h5 = Heap_max()
a5 = [8, 5, 4, 1, 2, 4, 3]
for x in a5:
	h5.insert(x)
print(h5.values)
h5.extract_max()
print(h5.values)

print('##########')

print("\nTesting Heap('min'):")
h1 = Heap('min')
a1 = random.sample([1, 2, 3, 10], 4)
for x in a1:
	h1.insert(x)
print(h1.values)
h1.extract_root()
print(h1.values)

print('##########')

h2 = Heap('min')
a2 = [1, 2, 4, 5, 3, 4, 8]
for x in a2:
	h2.insert(x)
print(h2.values)
h2.extract_root()
print(h2.values)

print("\nTesting Heap('max'):")
h3 = Heap('max')
a3 = random.sample([1, 2, 3, 10], 4)
for x in a3:
	h3.insert(x)
print(h3.values)
h3.extract_root()
print(h3.values)

print('##########')

h4 = Heap('max')
a4 = [8, 4, 5, 1, 2, 4, 3]
for x in a4:
	h4.insert(x)
print(h4.values)
h4.extract_root()
print(h4.values)

print('##########')

h5 = Heap('max')
a5 = [8, 5, 4, 1, 2, 4, 3]
for x in a5:
	h5.insert(x)
print(h5.values)
h5.extract_root()
print(h5.values)
