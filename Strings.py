

# multiline strings use triple quotes """string"""
multi_line_string = """
w3 schools python tutorial
strings
"""

# loop through a string.
# a string is an array.

a = "my name is joshua"
for x in a:
    print(x)


def string_as_array():
    b = "joshua"
    for y in b:
        print(y)


# print a string
print("a string")
# print a variable
var_one = "a variable string"
print(var_one)

# access a character
# use square brackets
string_array = "strings are arrays"
# accesses the 0th element of the array
print(string_array[0])

# the len() function will get the length of the string
length_of_the_string = len(string_array)
print(length_of_the_string)


# check string using the "in" keyword
# will check for "string" in the string_array variable
# returns a boolean this example is true
print("string" in string_array)
check = "string" in string_array

if "string" not in string_array:
    print("\"string\" is not in this string")
else: print("\"string\" is in this string")

# slicing strings
# strings are arrays
# use the square brackets    string[start:stop:step]
slice_string = "a string to slice"
# indexes start at 0
slice_start_two_end_seven = slice_string[2:8]
slice_with_skip_two = slice_string[::2]

#  negative indexing.
#  negative indexes work from the end of the string
#  using slice_string. Pull string from sice with negative indexes
neg_slice = slice_string[-15:-9]

