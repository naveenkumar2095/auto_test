#Python program to swap two variables

x = 5
y = 6
print('The value of x before swapping: {}'.format(x))
print('The value of y before swapping: {}'.format(y))

# create a temporary variable and swap the values
temp = x
x = y
y = temp

print('The value of x after swapping: {}'.format(x))
print('The value of y after swapping: {}'.format(y))
