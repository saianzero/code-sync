"""
ITERATOR
An object that returns elements one at a time 
from a sequence or data stream
and remembees its positio between calls.

It has two methodss (iterator protocol)
__iter__() -> Returns the iterator object itself
__next__() -> returns the next item in the sequence
              raises StopIteration when no more items

"""
import random

class Dice:
    def __init__(self, rolls):
        self.rolls = rolls
        self.count = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.count < self.rolls:
            self.count+=1
            return random.randint(1, 6)
        else:
            raise StopIteration

dice = Dice(3)

for die in dice:
    print(die)

"""
Internally:

for loop
   │
   ▼
iter(dice)
   │
   ▼
dice.__iter__()
   │
   ▼
returns dice
   │
   ▼
next(dice)
   │
   ├── count < rolls → return random number
   │
   ├── count < rolls → return random number
   │
   ├── count < rolls → return random number
   │
   └── otherwise → StopIteration
                         │
                         ▼
                    for loop ends

"""

"""
An ITERABLE is an object that can produce an iterator. 
An ITERATOR is the stateful object that actually produces values one at a time through __next__(). 
Every iterator is iterable, but not every iterable is an iterator.
"""
# iterable
nums = [1, 2, 3]

next(nums)        # ❌ TypeError

# iterator
it = iter(nums)

next(it)          # 1
next(it)          # 2
next(it)          # 3
next(it)          # StopIteration