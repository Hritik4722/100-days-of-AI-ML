import numpy as np
import math as mh

def is_prime(num):
    if num < 2:
        return (False,0)
    for counter in range(2, int(mh.sqrt(num)) + 1):
        if num % counter == 0:
            return (False,0)
    return (True,num)
        

matrix = np.arange(1,101)
new_matrix = matrix.reshape(10,10)
new_list_tf = []
new_list_num = []
print(new_matrix)
for i in new_matrix:
    for j in i:
        ans,number = is_prime(j)
        new_list_tf.append(ans)
        new_list_num.append(number)
array_tf = np.array(new_list_tf).reshape(10,10)
array_number = np.array(new_list_num).reshape(10,10)
num_of_prime = np.count_nonzero(array_number)
print(array_tf)
print("Only prime numbers\n")
print(array_number)
print("Number of prime numbers is ", num_of_prime)
