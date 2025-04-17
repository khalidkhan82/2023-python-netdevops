def counter(max_value: int):
    number = 0
    while number <= max_value:
        yield number
        number += 1


numbers = counter(5)

try:
	print("first number:", next(numbers))
	print("2nd number:", next(numbers))
	print("3rd number:", next(numbers))
	print("4th number:", next(numbers))
	print("5th number:", next(numbers))
	print(next(numbers))
	print(next(numbers))
except StopIteration:
	print("ran out of numbers")

try:
	print("first number:", next(numbers))
	print("2nd number:", next(numbers))
	print("3rd number:", next(numbers))
	print("4th number:", next(numbers))
	print("5th number:", next(numbers))
	print(next(numbers))
	print(next(numbers))
except StopIteration:
	print("ran out of numbers")