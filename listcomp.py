# list comprehension examples

#
# build a list of even numbers between 1 and 10
#
evens = [x for x in range(1, 11) if x % 2 == 0 ]
print(evens)

#
# build a list of squares for all numbers between 1 and 20 inclusive
#
squares = [x * x for x in range(1, 21)]
print(squares)
