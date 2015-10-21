__author__ = 'Denis'


# TODO refactoring
# TODO documentation

def merge_two_lists(list_one, list_two):
    """
    Function merge two lists in sorted order into merged list.
    Copy lists by value.
    :param list_one: list
    :param list_two: list
    :return: list
    """

    # Copy lists by value
    temp_list_one = list_one[:]
    temp_list_two = list_two[:]

    mergedlist = []
    while temp_list_one and temp_list_two:
        if temp_list_one[0] <= temp_list_two[0]:
            mergedlist.append(temp_list_one.pop(0))
        else:
            mergedlist.append(temp_list_two.pop(0))

    while temp_list_one:
        mergedlist.append(temp_list_one.pop(0))

    while temp_list_two:
        mergedlist.append(temp_list_two.pop(0))

    return mergedlist


# def merge_second(list_one, list_two):
#     mergedlist = list_one + list_two
#     sorted(mergedlist)
#
#     # print(mergedlist) #DEBUG
#     return mergedlist


def find_median(list_one, list_two):
    """
    Function merge two lists in sorted order into sorted list,
    and whem find median in sorted list.
    :param list_one: list
    :param list_two: list
    :return: float
    """

    # TODO only one: merge_first or merge_second
    sorted_list = merge_two_lists(list_one, list_two)
    # merge_second(list_one, list_two)

    result = 0.0
    length = len(sorted_list)
    if length > 1 and length % 2 == 0:
        center_one = sorted_list[length // 2 - 1]
        center_two = sorted_list[length // 2]

        result = (center_one + center_two) / 2.0
    else:
        print("Error! Invalid input list_one, list_two")
        return

    return result


def main():
    """
    Given two sorted numeric array of the same length N. Find the median of the numerical array of length 2N,
    containing all the numbers of the two data sets.

    Sample input:
    1 2 3 4
    1 4 5 6

    Example output:
    3.5
    """

    list_one = [1, 2, 3, 4]
    list_two = [1, 4, 5, 6]

    file_name = "median_input.txt"

    # Check that file exist
    try:
        with open(file_name) as file:
            list_one = file.readline().split(",")
            list_two = file.readline().split(",")
    except FileNotFoundError:
        print("File '{}' doesn't exist, using default arrays ".format(file_name))

    list_one = list(map(int, list_one))
    list_two = list(map(int, list_two))
    print(list_one)
    print(list_two)
    print("The correct result: 3.5, my result: {}".format(find_median(list_one, list_two)))
    print("Done")


if __name__ == "__main__":
    main()
