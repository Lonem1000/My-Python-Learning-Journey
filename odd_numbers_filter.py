"""
Script: My Odd Number Filter
Goal: Extract odd numbers from 1 to 1001 using functional programming.
Concepts used: range(), filter(), and lambda functions.
"""

# Define the range (1 to 1000)
numbers = range(1, 1001)

# Use filter and lambda function to pick only odd numbers
# x % 2 != 0 checks if there is a remainder when divided by 2
odd_numbers = list(filter(lambda x: x % 2 != 0, numbers))

# Output the result using a formatted string
print(f"Found {len(odd_numbers)} odd numbers.")
print(odd_numbers)
