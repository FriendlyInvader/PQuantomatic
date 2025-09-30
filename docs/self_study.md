# NumPy

Tasks:
* T001: create 1D,2D,3D array
* T001.1: get size, item size, dimention (number axes), shape(axis's dimentions), type of elements
* T001.2: create array of ints
* T001.3: create array of 0s of ints
* T001.4: create matrix(2,4) of 1s
* T001.5: create array(3) of 9s
* T001.6: create matrix(2,7) of random values
* T001.7: create array(8) of random values 0f [0,7)
* T001.8: create 3x3 identity matrix
* T001.9: set and get the first and the last element of array
* T001.10: (slicing) set and get a row and a column of matrix

Solutions
* T001:
~~~python
import numpy as np
arr_1D = np.array([1,2,3,4,5])
mat = np.array([[1,2], [3,4]])
arr_int = nd.array([1,2,3,4,5], dtype='int32')
arr_zeros = np.zeros(3, dtype='int32')
mat_ones = np.ones((2,4))   # NB: size is of type tuple
arr_nines = np.full(3, 9)
mat_rand = np.random.rand(2,7)
arr_rand_int = np.random.randint(7, size=8)
mat_ident = np.eye(3,3)

arr[0] # the first
arr[-1] # the last
mat_ident[:,0] = np.array([3,4,5]) # set the first column to [3,4,5]
mat_ident[1,:] = np.array([7,8,9]) # set the second row to [7,8,9]
mat_ident[0:3:2,0] = np.array([30,50]) # set [0,0] to 30 and [3,0] to 50

print(arr_1D.size, arr_1D.itemsize, arr_2D.ndim, arr_1D.shape, arr_D2.dtype)
~~~