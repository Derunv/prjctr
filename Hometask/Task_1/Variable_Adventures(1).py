# Task 1
print('Task 1')
a = 3
b = 5


c = a
a = b
b = c

a = a + b
b = a - b
a = a - b

a += b
b = a - b
a -= b

print('a = ', a, 'b = ', b)


# Task 2
print()
print('Task 2')
print('Please enter first number')
first_input = input()
print('Please enter second number')
second_input = input()
print('Result = ', int(first_input) - int(second_input))

# Task 3
print()
print('Task 3')
print('Please enter first number')
first_input = input()
print('Please enter second number')
second_input = input()
print('Result = ', max(int(first_input),int(second_input)))

# Task 5
print()
print('Task 4')
print('Please enter first number')
a = input()
print('Please enter second number')
b = input()
print('Please enter third number')
c = input()

d = a
a = c
c = d
print('Result = ', a, b, c)

