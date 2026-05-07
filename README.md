# Python Logic Lab: Odd Number Filter

## 📌 Project Overview
This is a simple yet efficient Python script that demonstrates **Functional Programming** concepts. The goal is to filter out all odd numbers from a range of 1 to 1000.

## 🚀 Concepts Covered
* **`range()`**: Generating a sequence of numbers efficiently.
* **`lambda` functions**: Creating anonymous, one-liner functions for quick logic.
* **`filter()`**: Using a higher-order function to process data without explicit loops.
* **Type Casting**: Converting a "lazy" filter object into a usable Python `list`.

## 🛠️ How It Works
Instead of using a traditional `for` loop with an `if` statement, this script uses a more "Pythonic" functional approach:

```python
numbers = range(1, 1001)
odd_numbers = list(filter(lambda x: x % 2 != 0, numbers))
print(odd_numbers)
