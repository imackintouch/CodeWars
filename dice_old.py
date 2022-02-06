
"""
dice roll out come program
"""

outcome_count = 0
def is_desired_sum(dice_roll_str, k):
    dice_roll_str = dice_roll_str.rstrip(",")
    dice_roll_list = dice_roll_str.split(",")
    print(dice_roll_list)
    sum = 0
    for i in (0, len(dice_roll_list) - 1):
        sum += int(dice_roll_list[i])

    if sum == k:
        return True
    else:
        return False


def outcome(n, s, k):
    """
    You have n dices each one having s sides numbered from 1 to s. How many outcomes add up to a specified number k?
    For example if we roll four normal six-sided dices we have four outcomes that add up to 5.
        (1, 1, 1, 2) (1, 1, 2, 1) (1, 2, 1, 1) (2, 1, 1, 1)

    :param n: number of die
    :param s: number of sides on each dice
    :param k: target die value sum
    :return:
    """
    print("Calculating outcome({},{},{})".format(n,s,k))

    if k > n * s:
        print("Sum {} is larger than maximum possible die sum {} * {}".format(k, n, s))
        return ""

    if n == 1 : # I am down to calculating the outcome for a single die
        return str(k)

    dice_roll_str = ""
    for i in range(1, k + 1):   # there is no way we can exceed the outcome on a single die roll to solve this problem.

        # print(i)
        if (k-i) == 0: # we cannot have a sum of 0. (we can probably make this another stopping condition)
            continue
        dice_roll_str += str(i) + "," + outcome(n-1, s, k-i) + ","

        print("A given dice roll string for {}, {}, {} is: {}".format(n, s, k, dice_roll_str))
        if is_desired_sum(dice_roll_str, k):
            print("{} MEETS current outcome criteria {}".format(dice_roll_str, k))
        else:
            print("{} does not meet current outcome criteria {}".format(dice_roll_str, k))

        dice_roll_str = ""

    return dice_roll_str


outcome(2, 6, 13)
outcome(2, 6, 3)
outcome(2, 6, 4)
outcome(3, 6, 4)
#outcome(4, 7, 6)
#outcome(3, 6, 4)