from math import log2

__author__ = 'Denis'


# TODO refactoring

def find_count_conversions(n, m):
    """
    Function count number of conversions. From n -> {(1), 2) or 3)} -> m
    1) n -> n + 1
    2) n -> n + 2
    3) n -> 2n

    pow(2, coeff1) * n + 2 * coeff2 + 1 * coeff3 = m

    example:
        n = 5, m = 101
        coeff1 = int(log2(m / n)) = 4
        coeff2 = int((m - pow(2, coeff1) * n) / 2) = 10
        coeff3 = int((m - pow(2, coeff1) * n) % 2) = 1


    0 <= n <= m <= 10 ^ 15
    :param n: int
    :param m: int
    :return: int
    """

    if not (0 <= n <= m <= pow(10, 15)):
        print("Error! Invalid input n, m")
        return

    coeff1 = int(log2(m / n))

    temp = m - pow(2, coeff1) * n

    coeff2 = int(temp / 2)
    coeff3 = int(temp % 2)
    return coeff1 + coeff2 + coeff3


def main():
    """
    We call the transformation of an integer n the use of one of the following:

    1) n -> n + 1
    2) n -> n + 2
    3) n -> 2n

    Write a program that, given the numbers n and m defines the length of the shortest sequence of transformations,
    which translates into a number n integer m (0 <= n <= m <= 10 ^ 15).

    Example:
    n = 5, m = 13
    """

    n = 5
    m = 13

    file_name = "conversion_input.txt"

    # Check that file exist
    try:
        with open(file_name) as file:
            input_str = file.readline().split(",")
            input_str = list(map(int, input_str))
            n, m = input_str[0], input_str[1]
    # ValueError, TypeError
    except FileNotFoundError:
        print("File '{}' doesn't exist, using default arrays ".format(file_name))

    print("n = {}".format(n))
    print("m = {}".format(m))
    print("The correct result: 3, my result: {}".format(find_count_conversions(n, m)))
    print("Done")


if __name__ == "__main__":
    main()
