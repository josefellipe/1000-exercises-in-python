inPalindrome = input("Write a possible palindrome:\n")


def text_to_array(text):
    array_text = list(text)
    array_text = remove_space(array_text)
    return array_text


def text_to_array_reverse(text):
    array_text_reverse = list(reversed(text))
    array_text_reverse = remove_space(array_text_reverse)
    return array_text_reverse


def remove_space(array_space):
    array_space = [i for i in array_space if i != " "]
    return array_space


def compare_arrays(array1, array2):
    if array1 == array2:
        result = True
    else:
        result = False
    return result


def is_palindrome(yes):
    if yes:
        result = "is"
    else:
        result = "isn't"
    return result


array = text_to_array(inPalindrome)

array_reverse = text_to_array_reverse(inPalindrome)

same = compare_arrays(array, array_reverse)

print(f'\n{inPalindrome} {is_palindrome(same)} a Palindrome!')
