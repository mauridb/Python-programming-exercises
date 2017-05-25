def solution(txt):
  return txt.upper()



while True:
  txt = raw_input()
  if txt == '0':
    break
  else:
    print solution(txt)
    print 'if you wanna turn off the programm type 0'
  
  
