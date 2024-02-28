import numpy as np

# a. Creating arrays

zeros_array = np.zeros((4, 3))

ones_array = np.ones((4, 3))

numbers_array = np.arange(12).reshape(4, 3)

print(zeros_array, ones_array, numbers_array)

# b. Tabulating the function F(x) = 2x^2 + 5, x ∈ [1,100] with step 1

x_values = np.arange(1, 101)
function_values_b = 2 * x_values ** 2 + 5
print("\nTabulated values of F(x) = 2x^2 + 5:")
for i in range(len(x_values)):
    print(f"x={x_values[i]}, F(x)={function_values_b[i]}")


# c. Tabulating the function F(x) = e^(-x), x ∈ [-10,10] with step 1
x_values = np.arange(-10, 11)
function_values_c = np.exp(-x_values)
print("\nTabulated values of F(x) = e^(-x):")
for i in range(len(x_values)):
    print(f"x={x_values[i]}, F(x)={function_values_c[i]}")
