grades = input("\nWrite the grades separated by comma:\n")


def format_grades(grade):
    array_grade = list(grade)
    array_grade = [i for i in array_grade if i != ","]
    array_grade = [i for i in array_grade if i != " "]
    return array_grade


def arithmect_mean(grade):
    n = 0
    sum = 0
    for i in grade:
        sum += float(i)
        n += 1
    return sum/n


def geometric_mean(grade):
    n = 0
    product = 1
    for i in grade:
        product = product*float(i)
        n += 1
    return product**(1/n)


def compare_means(am,gm):
    if am > gm:
        comparation = "The Arithmect mean is higher"
    else:
        comparation = "The Geometric mean is higher"
    return comparation

grades = format_grades(grades)

print(f'\nThe grades are {grades}'
      f'\nThe arithmect mean is {arithmect_mean(grades):.2f}'
      f'\nThe geometric_mean is {geometric_mean(grades):.2f}'
      f'\n{compare_means(arithmect_mean(grades),geometric_mean(grades))}')
