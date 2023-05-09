# the format() method can be used to combine strings and numbers
#  this method takes arguments, formats them, and then passes them to the
#  strings placeholders {}
string_to_format = "Hello, my name is joshua. I am {} years old. My sister is " \
                   "{}"
age_josh = 50
age_sister = 44
formatted_string = string_to_format.format(age_josh, age_sister)

#  placeholders can be indexed {0} {1} to assign arguments to the correct
#  placeholder

