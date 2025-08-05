import array as arr

# i means integer
a = arr.array("i", [1, 2, 3])
print(type(a))
for i in a:
    print(i)

"""
Only consists of elements belonging to the same data type
Can directly handle arithmetic operations
Preferred for a longer sequence of data items
"""
