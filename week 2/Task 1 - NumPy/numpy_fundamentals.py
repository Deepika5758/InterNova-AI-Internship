
import numpy as np

# 1. Creating a NumPy array
print("1. Creating NumPy Arrays")

arr1 = np.array([10, 20, 30, 40, 50])
print("1D Array:", arr1)

# 2. Creating a 2D array
arr2 = np.array([[10, 20, 30],
                 [40, 50, 60]])
print("\n2D Array:")
print(arr2)

# 3. Array indexing
print("\n2. Array Indexing")
print("First element:", arr1[0])
print("Last element:", arr1[-1])

# 4. Array slicing
print("\n3. Array Slicing")
print("Elements from index 1 to 3:", arr1[1:4])
print("First row of 2D array:", arr2[0, :])

# 5. Shape and dimensions
print("\n4. Shape and Dimensions")
print("Shape of 1D array:", arr1.shape)
print("Dimensions of 1D array:", arr1.ndim)
print("Shape of 2D array:", arr2.shape)
print("Dimensions of 2D array:", arr2.ndim)

# 6. Mathematical operations
print("\n5. Mathematical Operations")
print("Addition:", arr1 + 5)
print("Subtraction:", arr1 - 5)
print("Multiplication:", arr1 * 2)
print("Division:", arr1 / 2)

# 7. Statistical operations
print("\n6. Statistical Operations")
print("Mean:", np.mean(arr1))
print("Maximum:", np.max(arr1))
print("Minimum:", np.min(arr1))
print("Sum:", np.sum(arr1))
