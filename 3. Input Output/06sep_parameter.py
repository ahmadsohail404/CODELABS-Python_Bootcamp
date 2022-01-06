
# The separator between the arguments to print() function in Python is space
# by default (softspace feature) , which can be modified and can be made to any
# character, integer or string as per our choice.

# code for disabling the softspace feature

print('C', 'O', 'V', 'I', 'D')
print('C', 'O', 'V', 'I', 'D', sep='')

# for formatting a date
print('09', '12', '2016', sep='-')

# another example
print('nisb', 'nie.ac.in', sep='@')

# one more example
print('C', 'O', 'V', 'I', sep='', end='')
print('D')
