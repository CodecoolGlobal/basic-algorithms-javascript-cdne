"""
Implement these two search algorithms.
"""


def linear_search(number, list):
    """
    Search for the number in the sorted list with the linear search algorithm
    and return the index of the element.

    Optional: print out how many comparision was needed to find the number

    :param integer number: The number to search for
    :param list of numbers list: Ascending list of numbers
    :return: Index of the element or None
    :rtype: integer
    """
    index = 0

    for list_number in list:
        if list_number == number:
            print("Compared:", index + 1, " times")
            return index
        else:
            index += 1
    return None


def binary_search(number, list):
    """
    Search for the number in the sorted list with the binary search algorithm
    and return the index of the element.

    Optional: print out how many comparision was needed to find the number

    :param integer number: The number to search for
    :param list of numbers list: Ascending list of numbers
    :return: Index of the element or None
    :rtype: integer
    """
    compared = 0
    low_bound = 0
    high_bound = len(list) - 1
    while low_bound <= high_bound:
        middle_bound = (low_bound + high_bound) // 2
        compared += 1
        if list[middle_bound] == number:
            print("Compared:", compared, "times")
            return middle_bound
        elif list[middle_bound] > number:
            high_bound = middle_bound - 1
        else:
            low_bound = middle_bound + 1
    return None


def print_results(search, index):
    result = search.title() + ' search '

    if index is None:
        result += 'did not find it.'
    else:
        result += f'found it on index {index}.'

    print(result)


def main():
    numbers = [3, 6, 8, 11, 18, 23, 24, 33, 36, 45, 46, 51, 56, 60, 69, 72, 83, 90, 93, 97]
    searched_number = int(input('What is the number you are looking for? (0-100) '))

    print_results('linear', linear_search(searched_number, numbers))
    print_results('binary', binary_search(searched_number, numbers))


if __name__ == '__main__':
    main()
