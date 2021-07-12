# -*- coding: utf-8 -*-
"""
Created on Sat May  9 20:14:54 2020

@author: aishwary
"""

from os import chdir
chdir('G:/My Drive/2020/Coding/Itertools')
import itertools

# Infinite Iterators
counter=itertools.count()
counter=itertools.count(start=5)
counter=itertools.count(start=5,step=5)

print(next(counter))
print(next(counter))
print(next(counter))

data=[100,200,300,400]
daily_data=list(zip(itertools.count(),data))
print(daily_data)
daily_data=list(zip(range(10),data))
print(daily_data)
daily_data=list(itertools.zip_longest(range(10),data))
print(daily_data)

counter=itertools.cycle(['On','Off'])
print(next(counter))
print(next(counter))
print(next(counter))

counter=itertools.repeat(2)
print(next(counter))
print(next(counter))
print(next(counter))

# get squares of values 1-10
# map takes a function, it takes iterables to pass values to the function
squares=map(pow,range(10),itertools.repeat(2))
print(list(squares))
# starmap takes tuples as arguments to the function
squares=itertools.starmap(pow,[(0,2),(1,2),(2,2)])
print(list(squares))


# Permutation and combinations
letters = ['a', 'b', 'c', 'd']
numbers = [0, 1, 2, 3]
names = ['Corey', 'Nicole']

result=itertools.combinations(letters,2)
for item in result:
    print(item)

result=itertools.permutations(letters,2)
for item in result:
    print(item)

result=itertools.product(numbers,repeat=4)
for item in result:
    print(item)


result=itertools.combinations_with_replacement(numbers,4)
for item in result:
    print(item)

combined=itertools.chain(letters,numbers,names)
for item in combined:
    print(item)
    
result=itertools.islice(range(10),1,5)
for item in result:
    print(item)

with open('snippets.txt','r') as f:
    header=itertools.islice(f,3)
    for line in header:
        print(line,end='')


# Compress & Filter
selectors=[True,True,False,True]
result=itertools.compress(letters,selectors)
for item in result:
    print(item)
        
def lt_2(n):
    if n<2:
        return True
    return False

result=filter(lt_2,numbers)
result=itertools.filterfalse(lt_2,numbers)

for item in result:
    print(item)

# Accumulate, gives running total of values it has seen so far
result=itertools.accumulate(numbers)
for item in result:
    print(item)

numbers = [4, 1, 2, 3]

import operator
result=itertools.accumulate(numbers,operator.mul)
for item in result:
    print(item)

# Groupby itertools
people = [
    {
        'name': 'John Doe',
        'city': 'Gotham',
        'state': 'NY'
    },
    {
        'name': 'Jane Doe',
        'city': 'Kings Landing',
        'state': 'NY'
    },
    {
        'name': 'Corey Schafer',
        'city': 'Boulder',
        'state': 'CO'
    },
    {
        'name': 'Al Einstein',
        'city': 'Denver',
        'state': 'CO'
    },
    {
        'name': 'John Henry',
        'city': 'Hinton',
        'state': 'WV'
    },
    {
        'name': 'Randy Moss',
        'city': 'Rand',
        'state': 'WV'
    },
    {
        'name': 'Nicole K',
        'city': 'Asheville',
        'state': 'NC'
    },
    {
        'name': 'Jim Doe',
        'city': 'Charlotte',
        'state': 'NC'
    },
    {
        'name': 'Jane Taylor',
        'city': 'Faketown',
        'state': 'NC'
    }
]


def get_state(person):
    return person['state']

person_group=itertools.groupby(people,get_state)
for key,group in person_group:
    print(key)
    for person in group:
        print(person)
    print()
    