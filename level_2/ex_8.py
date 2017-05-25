from datetime import datetime

def sort_elem_in_list(array):
  array = array.split(',')
  array.sort()
  
  return array


l = raw_input()

start = datetime.now()
print sort_elem_in_list(l)
after = datetime.now()
delta = after - start

print delta
