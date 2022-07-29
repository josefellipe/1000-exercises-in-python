number = int(input("\nWrite a number:  "))


def double(num):
    return num*2


def squared(num):
    return num**2


def root(num):
    return (num**0.5)


print(f'\nThe double of {number} is {double(number)}'
      f'\nThe square of {number} is {squared(number)}'
      f'\nThe square root of {number} is {root(number):.2f}\n\n')
