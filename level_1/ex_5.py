class GitHub(object):
  
  def get_string(self):
    txt = raw_input()
    return txt

  def printString(self, txt):
    return txt

# _________________________________________


git = GitHub()

def test():
  return git.printString(git.get_string())


  
print test()
