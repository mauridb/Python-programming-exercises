def generate_dict(number):
  """
  number: integer input
  """
  solution = {}
  for key in range(int(number)):
    solution[key] = key*key

  return solution
  
  
number = raw_input('Choose a number ..')
print generate_dict(number)
