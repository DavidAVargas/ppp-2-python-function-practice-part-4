#max number
def max_num(a, b, c):
    return max(a, b, c)

print(max_num(1, 2, 3))      
print(max_num(100, 50, 1))   
print(max_num(15, 30, 2))     

# multiply list
from functools import reduce
import operator

def mult_list(lst):
    if not lst:  
        return 0
    return reduce(operator.mul, lst, 1)


print(mult_list([1, 2, 3]))  
print(mult_list([]))        
print(mult_list([15]))      

# reverse string
def rev_string(my_str):
    return ''.join(reversed(my_str))


print(rev_string(""))        
print(rev_string("apple"))   
print(rev_string("mt string"))  

# number within
def num_within(x, a, b):
    return a <= x <= b


print(num_within(3, 2, 4))  
print(num_within(3, 1, 3))  
print(num_within(10, 2, 5)) 

# pascal
def pascal(n):
    if n < 1:
        print("invalid number of rows")
        return
    
    triangle = [[1]]
    for i in range(1, n):
        row = [1] * (i + 1)
        for j in range(1, i):
            row[j] = triangle[i - 1][j - 1] + triangle[i - 1][j]
        triangle.append(row)
    
    for row in triangle:
        print(row)

pascal(2)
pascal(5)