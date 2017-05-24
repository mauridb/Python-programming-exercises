number = raw_input('Compute a factorial number .. ')
num = int(number)
print num, type(num)

def factorial(n):
  if n == 0:
    return 1
  
  return n*factorial(n-1)

print factorial(num) 
