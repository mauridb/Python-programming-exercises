from datetime import datetime

def multi_dimensional_array(num_rows, num_elem_in_row):
  
  matrix = []
  
#standard_start = datetime.now()  
# for row in range(num_rows):
#   matrix.append([row]*num_elem_in_row)
    # print row 
# standard_end = datetime.now()


# point_start = datetime.now()
  matrix = [[row]*num_elem_in_row for row in range(num_rows)]
# point_end = datetime.now()
# res_list = point_end - point_start
# res_standard = standard_end - standard_start

  # print point_start
  # print point_end
# print 'LIST COMPREHENSION: '+str(res_list)
# print 'STANDARD:'+str(res_standard)  

  print matrix
  # print num_elem_in_row
  




multi_dimensional_array(3,5)
  

