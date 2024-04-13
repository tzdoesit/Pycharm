print("Python in Y minutes")

# print('Hello World')

# print(3)
# print(1 + 1)
# print(8 - 1)
# print(10 * 2)
# print(35 / 5)
#
# print(5 // 3)
# print(-5 // 3)
# print(5.0 // 3.0)
# print(-5.0 // 3.0)

# print(10.0 / 3)
# print(7 % 3)
# print(-7 % 3)
#
# print(2 ** 3)
# print(1 + 3 * 2)
# print((1 + 3) * 2)
#
# print(True)
# print(False)
# print(True and False)
# print(not True)
# print(not False)
# print(False or True)
#
# print(True + True)
# print(True * 8)
# print(False - 5)

# print(0 == False)
# print(2 > True)
# print(2 == True)
# print(-5 != False)

# print(bool(0))
# print(bool(""))
# print(bool([]))
# print(bool({}))
# print(bool(()))
# print(bool(set()))
# print(bool(4))
# print(bool(-6))
#
# print("this", "is", "a", "tuple")

# print(2 == 1)
# print(1 == 1)
#
# print(1 != 1)
# print(2 != 3)
#
# print(1 < 10)
# print(1 > 10)
# print(2 <= 2)
# print(2 >= 2)

# print((1 < 2) and (2 < 3))
# print((2 < 3) and (3 < 2))

# a = [1, 2, 3, 4]
# b = a
# print(b is a)
# print(b == a)
# b = [1, 2, 3, 4]
# print(b is a) #not the same object, is False
# print(b == a)
# a = b
# print(b is a)

# print("This is a string")
# print('This is also a string')
# print("You can concatenate + " + "strings.")
# print("You can also concatenate " "without the +")
#
# print("hello world" [4])
#
# print(len("This is a string"))

# name = "Reiko"
# print(f"She said her name is {name}.")
#
# print(f"{name} is {len(name)} characters long")
#
# print(f"Name is {name}")

# print(None)

# print("etc" == None)
# print(None is None)

# If you don't want to print the default new line at end of print function
# print("Hello, world", end="!")
# print("Hello, world", end="!")

# input_string = input("Enter a word: ")
# print(input_string)

# some_var = 5
# print(some_var)

# undefined var leads to an error
# print(some_unknown_var)

# yay_or_nay = "yay!" if 1 > 0 else "nay!"
# print(yay_or_nay)

# list = []
# print(list)
#
# list.append(1)
# list.append("hi")
# list.append(2)
# list.pop()
# list.pop(0)
# print(list)


# other_list = [4, 5, 6]
# print(other_list)
# print(other_list[0])

# list_nums = [1, 2, 3, 4, 5]
# print(list_nums[2])
# print(list_nums[-1])
# print(list_nums[1:3])
# print(list_nums[2:])
# print(list_nums[:3])

# Return list selecting elements with a step size of 2 => [1, 3, 5]
# print(list_nums[::2])

# Return list in reverse order => [5, 4, 3, 2, 1]
# print(list_nums[::-1])

# Use any combination of these to make advanced slices
# li[start:end:step]

# # Looking out-of-bounds results in an IndexError
# print(list_nums[7])

# li = list_nums[:]
# li.append(6)
# print(li)
# del li[5]
# print(li)
# li.pop()
# print(li)
# li.remove(2)
# print(li)
# li.insert(1, 2)
# print(li)
# print(li.index(4))
#
# li2 = [5, 6, 7]
# li3 = (li + li2)
# print(li3)
#
# print(li)
# print(li2)
# li4 = li.extend(li2)
# print(li4)
#
# print(1 in li)

###
# Tuples are like list are immutable (unchangeable)
###

# tup = (1, 2, 3)
# print(tup[1])
# print(tup)

# Note that a tuple of length one has to have a comma after the last element but
# tuples of other lengths, even zero, do not.

# type((1))   # => <class 'int'>
# type((1,))  # => <class 'tuple'>
# type(())    # => <class 'tuple'>
#
# print(len(tup))
# print(tup + (4, 5, 6))
# print(tup[:2])
# print(2 in tup)
# print(tup)
#
# a, b, c = (1, 2, 3)
# print(a, b, c)
#
# a, *b, c = (1, 2, 3, 4, 5, 6)
# print(a, b, c)
#
# d, e, f = 4, 5, 6
# print(d, e, f)
#
# e, d = d, e
# print (e, d)

###
# Dictionaries store mappings from keys to values
###

# empty_dict = {}
filled_dict = {"one":1, "two":2, "three":3}
# print(filled_dict)
print(filled_dict["one"])
print(list(filled_dict.keys()))
print(list(filled_dict.values()))
print(filled_dict.values())
print(filled_dict.keys())
print("one" in filled_dict)
print(1 in filled_dict)


# Looking up a non-existing key is a KeyError
# print(filled_dict["four"])  # KeyError

# Note keys for dictionaries have to be immutable types. This is to ensure that
# the key can be converted to a constant hash value for quick look-ups.
# Immutable types include ints, floats, strings, tuples.
#
# invalid_dict = {[1,2,3]: "123"}  # => Yield a TypeError: unhashable type: 'list'
# valid_dict = {(1,2,3):[1,2,3]}   # Values can be of any type, however.
#
# also_valid_dict = {(1,2,3):[1,2,3]}
# print(also_valid_dict)













