__author__ = 'Denis'


def merge_first(list_one, list_two):
    local_list_one = list_one[:]
    local_list_two = list_two[:]

    mergedlist = []
    while local_list_one and local_list_two:
        if local_list_one[0] <= local_list_two[0]:
            mergedlist.append(local_list_one.pop(0))
        else:
            mergedlist.append(local_list_two.pop(0))

    while local_list_one:
        mergedlist.append(local_list_one.pop(0))

    while local_list_two:
        mergedlist.append(local_list_two.pop(0))

    # print(mergedlist) #DEBUG
    return mergedlist


def merge_second(list_one, list_two):
    mergedlist = list_one + list_two
    sorted(mergedlist)

    # print(mergedlist) #DEBUG
    return mergedlist


def find_median(list_one, list_two):
    # TODO only one: merge_first or merge_second
    sorted_list = merge_first(list_one, list_two)
    # merge_second(list_one, list_two)

    result = 0.0
    length = len(sorted_list)
    if length > 1 and length % 2 == 0:
        # TODO int(length/2 - 1) good?
        #print(length/2 - 1) # DEBUG
        #print(length/2) # DEBUG
        center_one = sorted_list[int(length/2 - 1)]
        center_two = sorted_list[int(length/2)]

        result = (center_one + center_two) / 2.0
    return result


def main():
    """
Даны два отсортированных числовых массива одинаковой длины N.
Найдите медиану числового массива длины 2N, содержащего все числа из двух данных массивов.
    """
    list_one = [1, 2, 3, 4]
    list_two = [1, 4, 5, 6]

    print(list_one)
    print(list_two)
    print("The correct result: 3.5, my result: {}".format( find_median(list_one, list_two) ))
    print("Done")


if __name__ == "__main__":
    main()
