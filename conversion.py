__author__ = 'Denis'


def conversion(switch, num):
    if switch == 1:
        return num + 1
    elif switch == 2:
        return num + 2
    elif switch == 3:
        return 2 * num


def find_count_conversions(n, m):
    """Function"""

    if not (0 <= n <= m and m <= pow(10, 15)):
        print("Error! Invalid input n, m")
        return

    # TODO write to end
    # TODO check

    stage = 3

    while stage > 0:
        quotient = m / conversion(stage, n)
        remainder = m % conversion(stage, n)


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

    print("n = {}".format(n))
    print("m = {}".format(m))
    print("The correct result: 3, my result: {}".format(find_count_conversions(n, m)))
    print("Done")


if __name__ == "__main__":
    main()
