"""
tips:
- ctrl + p autocomplete vim
- :%s  

"""

numbers = range(2000, 3201)
# print numbers

list_divisible_with_7 = [number for number in numbers if number%7==0]
# print list_divisible_with_7 

list_divisible_by_7_not_by_5 = [str(number) for number in list_divisible_with_7 if number%5!=0]
print list_divisible_by_7_not_by_5

solution = ','.join(list_divisible_by_7_not_by_5)
print solution

