#The is_positive function should return True if the number received is positive and False if it isn't. Can you fill in the gaps to make that happen?

def is_positive(number):
  if number > 0:
    return True
  else:
    return False

print(is_positive(-5)) # False
print(is_positive(0)) # False
print(is_positive(13)) # True
