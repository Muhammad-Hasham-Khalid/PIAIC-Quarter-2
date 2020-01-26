import numpy as np

ndarray = np.array(
    [
    [11, 12, 13],
    [21, 22, 23],
    [31, 32, 33],
    [41, 42, 43],
    ]
)

print("ndarray :", ndarray)
print("Dimension :", ndarray.ndim)
print("Shape :", ndarray.shape)
# (4,3) Main array of size 4 then each element of size 3
# Means main array's largest index can be 3 == (4-1) and inner largest index can be 2 == (3-1)

# use of colon is optional means select all
print("Sliced :", ndarray[:4, 1])  # comma means we are going to slice the next dimension
print("Max_Sliced :", ndarray[0:4, 0:3])

newNdArray = np.array(
    [
        [[111, 112, 113, 114], [121, 122, 123, 124], [131, 132, 133, 134]],
        [[211, 212, 213, 214], [221, 222, 223, 224], [231, 232, 233, 234]],
        [[311, 312, 313, 314], [321, 322, 323, 324], [331, 332, 333, 334]],
        [[411, 412, 413, 414], [421, 422, 423, 424], [431, 432, 433, 434]],
    ]
)

print("newNdArray :", newNdArray)
print("Dimension :", newNdArray.ndim)
print("Shape :", newNdArray.shape)

# Slicing
print("Sliced :", newNdArray[2, 1, 2])
print("Max_Sliced :", newNdArray[0:newNdArray.shape[0], 0:newNdArray.shape[1], 0:newNdArray.shape[2]]) # this will give you the whole array


'''
NOTE : 
    The most important in slicing is to keep the number of dimensions and shape in mind.
    This will make it easy for us to slice the whole array in different sizes and shapes.
'''