# Q = Square root of [(2*C*D)/H] ---> formula
from __future__ import division
import math


# fixed variables
c = 50
h = 30

def sol(l):
  solution = []
  list_numbers = l.split(',')
  print list_numbers

  for n in list_numbers:
    res = int(math.sqrt((2*c*int(n))/h))
    solution.append(str(res))
  
  print solution
  return ' - '.join(solution)



l = raw_input()
print sol(l)  
