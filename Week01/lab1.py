# Sample Coding Questions 01 Week 01
# Basira Zaki

# Defining Variables
# Define an array variable with elements 1, 4, 7, 9
my_arry=[1, 4, 7, 9]
print("Array:", my_array)

# Order of Operations
# Define 4 variables a, b, c, d with values 1, 2, 3, 4
a = 1
b = 2
c = 3
d = 4
# Original expression: e = a - b ** c // d + a % c
# Fully-Bracketed Version:
# ** (power) has highest precedence
# then // (floor division) and % (modulo)
# then - and + from left to right
e = ((a - ((b ** c) // d)) + (a % c))
print("\nOrder of Operations:")
print(f"a = {a}, b = {b}, c = {c}, d = {d}")
print(f"Expression: e = a - b ** c // d + a % c")
print(f"Fully-Bracketed: e = ((a - ((b ** c) // d)) + (a % c))")
print(f"Result: e = {e}")
# Step-by-step breakdown:
print("\nStep-by-step:")
print(f"1. b ** c = {b} ** {c} = {b ** c}")
print(f"2. (b ** c) // d = {b ** c} // {d} = {(b ** c) // d}")
print(f"3. a % c = {a} % {c} = {a % c}")
print(f"4. a - ((b ** c) // d) = {a} - {(b ** c) // d} = {a - ((b ** c) // d)}")
print(f"5. (a - ((b ** c) // d)) + (a % c) = {a - ((b ** c) // d)} + {a % c} = {e}")

# Formatting
temperature = 32.6
print(f"\nThe temperature today is: {temperature:.3f} degrees Celsius")
# Common Functions
userAge = input("\nEnter your age: ")
userAge = int(userAge) + 22
print(f"Now showing the shop items filtered by age: {userAge}")
