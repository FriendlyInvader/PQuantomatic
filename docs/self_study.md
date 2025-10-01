# NumPy

Tasks: [source](https://www.youtube.com/watch?v=DcfYgePyedM)
* T001: create 1D,2D,3D array
* T001.1: get size, item size, dimention (number axes), shape(axis's dimentions), type of elements. [ndarray properties](https://numpy.org/doc/stable/reference/arrays.ndarray.html#id1), [types](https://numpy.org/doc/stable/reference/arrays.dtypes.html#arrays-dtypes)
* T001.2: create array of ints
* T001.3: create array of 0s of ints
* T001.4: create matrix(2,4) of 1s
* T001.5: create array(3) of 9s
* T001.6: create matrix(2,7) of random values
* T001.7: create array(8) of random values of [0,7)
* T001.7.1: create array(8) of random normally distributed values (gausian distribution)
* T001.8: create 3x3 identity matrix
* T001.9: set and get the first and the last element of array
* T001.10: (slicing) set and get a row and a column of matrix
* T001.11: array of 100 values from 0 to 10 with the same interval
* T002: what if arr2=arr1; arr2[3]=999?
* T003: build 5x5 matrix like
~~~text
1 1 1 1 1
1 0 0 0 1
1 0 9 0 1
1 0 0 0 1
1 1 1 1 1
~~~
* T004: Vector/Math operations like **sum, sumab, mns, div, mlt, pow, cos, sin, sqrt**. [calculus](https://numpy.org/doc/stable/reference/arrays.ndarray.html#calculation)
* T005: [reshape, resize, flatten](https://numpy.org/doc/stable/reference/arrays.ndarray.html#shape-manipulation)
* T006: get all even elements
* T007: apply function element wise to array
* T008: given ['Mike','James','Chris','Jake']. collect all names starting from letter 'J' => ['James','Jake']
* T009: get percentile of 80 - what is the number, 80% of elements of array less then this number
* T010: get derivative and integral
* T011: Code
~~~text
Let y = exp ^ (-x/10) * sin(x). Consider 10,000 intervalsin the range [0, 10]
1. Plot the function y vs. x in the range [0,10]
2. Compute the mean ans standard deviation of y for x value in [4,7]
3. For x in the range [4,7], find the value ym such that 80% of y values are less then ym
4. Plot dy/dx vs x
5. Find the location where dy/dx=0
~~~
* T012: Sum together every number from 0 to 10000except for those that can be divided by 4 or 7. Do this in one line of code



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
mat_rand = np.random.rand(2,7) # random
mat_rand_norm = np.random.randn(7) # normally distributed (gausian)
arr_rand_int = np.random.randint(7, size=8)
mat_ident = np.eye(3,3)

arr[0] # the first
arr[-1] # the last
mat_ident[:,0] = np.array([3,4,5]) # set the first column to [3,4,5]
mat_ident[1,:] = np.array([7,8,9]) # set the second row to [7,8,9]
mat_ident[0:3:2,0] = np.array([30,50]) # set [0,0] to 30 and [3,0] to 50
arr_100 = np.linspace(0, 10, 100) # 100 valies of [0,10) with the same interval
arr_100 = np.arrange(0, 10, 0.02) # 100 valies of [0,10) with the same interval, equal to previous

print(arr_1D.size, arr_1D.itemsize, arr_2D.ndim, arr_1D.shape, arr_D2.dtype)
~~~

* T002: what if arr2=arr1; arr2[3]=999?
> arr2 and arr1 is the same array, changing arr1 changes arr2 and visa versa. fix **arr2=arr1.copy()**

* T003:build 5x5 matrix like
~~~python
# 1 1 1 1 1
# 1 0 0 0 1
# 1 0 9 0 1
# 1 0 0 0 1
# 1 1 1 1 1

import numpy as np
m = np.ones((5,5))
m[1:4,1:4] = np.zeros(3,3) # or m[1:-1,1:-1] = np.zeros(3,3)
m[2,2]=9.0
~~~

* T004: Math like **sum, sumab, mns, div, mlt, pow, cos, sin, sqrt**
~~~python
a = np.array([1, 2, 3])
b = np.array([10, 20, 30])
sum, sumab, mns, div, mlt, pow, cos, sin, sqrt = a+1, b+b, a-1, a/2, a*3, a**2, np.cos(a), np.sin(a), np.sqrt(b)
~~~

* T006: get all even elements
~~~python
arr = np.array([1,2,3,4,5,6,7])
print(arr[arr%2==0])
~~~
> NB: **arr%2==0** returns array of True/False. **arr[arr%2==0]** returns elements if True

* T007: apply function element wise to array
~~~python
def f(x):
    return x**2
arr = np.array([1,2,3,4,5,6,7])
arr2 = f(arr)
~~~

* T008: given ['Mike','James','Chris','Jake']. collect all names starting from letter 'J' => ['James','Jake']
~~~python
names = np.array(['Mike','James','Chris','Jake'])
first_letter = lambda str: str[0]
letters = np.vectorize(first_letter)(names)
result=names[letters=='J']
~~~

* T009: get percentile of 80 - what is the number, 80% of elements of array less then this number
~~~python
arr = np.array([1,2,3,4,5,6,7,8,9,10])
print(np.percentile(arr, 80)) # 8.2 => 80% of arr less then 8.2
~~~

* T010: get derivative
~~~python
x = np.linspace(1,10,100)
y = 1/x**2 + np.sin(x)   # f(x) = y
dydx = np.gradient(y, x) # derivative of f(x)
y_int = np.cumsum(y) * (x[1]-x[0]) # integral. 
~~~

* T011: Code
~~~python
# Let y = exp ^ (-x/10) * sin(x). Consider 10,000 intervalsin the range [0, 10]
# 1. Plot the function y vs. x in the range [0,10]
# 2. Compute the mean ans standard deviation of y for x value in [4,7]
# 3. For x in the range [4,7], find the value ym such that 80% of y values are less then ym
# 4. Plot dy/dx vs x
# 5. Find the location where dy/dx=0
import numpy as np
SIZE = 100000
x = np.linspace(0, 10, SIZE + 1)
assert 1 == x.ndim
assert SIZE + 1 == x.size
assert (SIZE + 1,) == x.shape
y = np.exp(-x / 10) + np.sin(x)
# plt.plot(x,y) # 1
y47=y[(x>=4)*(x<=7)]
y47_mean, y47_std = np.mean(y47), np.std(y47) # 2
y3 = np.percentile(y47, 80) # 3
dydx = np.gradient(y,x)
# plt.plot(x, dydx) # 4
lct = x[1:][dydx[1:]*dydx[:-1]<0] # 5 see https://www.youtube.com/watch?v=DcfYgePyedM (27:30 time)
~~~

* T012: Sum together every number from 0 to 10000 except for those that can be divided by 4 or 7. Do this in one line of code
~~~python
nums = np.arange(0, 10001, 1)
np.sum(nums[ (nums%4!=0) * (nums%7!=0) ])
~~~




# matplotlib

~~~python
import matplotlib.pyplot as plt
plt.plot([1, 2, 3], [2, 4, 6])
plt.title("Line Plot")
plt.xlabel("X Axis")
plt.ylabel("Y Axis")
plt.show()
~~~
