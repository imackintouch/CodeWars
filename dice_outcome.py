import sys

"""
dice roll out come program. (Try to challenge myself in another module to calculate sums without storing a list)
"""

outcome_count = 0
def is_desired_sum(dice_roll_str, k):
    dice_roll_list = dice_roll_str.rstrip(',').split(",")
    print("List to get summed up:{}".format(dice_roll_list))
    sum = 0
    for i in range(0, len(dice_roll_list)):
        sum += int(dice_roll_list[i])
    print("My sum is:{}".format(sum))
    return sum == k



def outcome(n, s, k):
    def dice_outcomes(n, s, k):
        """
        You have n dices each one having s sides numbered from 1 to s. How many outcomes add up to a specified number k?
        For example if we roll four normal six-sided dices we have four outcomes that add up to 5.
        (1, 1, 1, 2) (1, 1, 2, 1) (1, 2, 1, 1) (2, 1, 1, 1)

        :param n: number of die
        :param s: number of sides on each dice
        :param k: target die value sum
        :return:
        """
        print("Calculating outcome({}, {}, {})".format(n,s,k))

        if k > (n * s) or k < n:
            if k > (n*s):
                print("Sum {} is larger than maximum possible die sum: {} * {}".format(k, n, s))
            if k <= 0:
                print("Sum {} is less than or equal to number of die {} which is not possible!".format(k, n))
            return []

        if n == 1 : # We cannot have less than 1 die.
            print("Number of die is now 1. Stopping state reached. Need to return.".format(k, n))
            return [str(k)]

        dice_outcome_list = []
        for i in range(1, s + 1):   # There is no way we can exceed the max value of a side to solve this problem.

            outcome_list = dice_outcomes(n-1, s, k-i)
            print("Outcome list at start of main loop:{}".format(outcome_list))
            #
            # Now let's look at this list of die roll outcomes
            #
            for die_roll_outcome in outcome_list:
                dice_roll_str = str(i) + "," + str(die_roll_outcome).rstrip(',')

                print("A given dice roll string for {}, {}, {} is: {}".format(n, s, k, dice_roll_str))
                if is_desired_sum(dice_roll_str, k):
                    print("The sum of {} MEETS current outcome criteria {}".format(dice_roll_str, k))
                    dice_outcome_list.append(dice_roll_str)
                    print("outcome_list is now: {}".format(dice_outcome_list))
                else:
                    print("{} does not meet current outcome criteria {}".format(dice_roll_str, k))

        return dice_outcome_list

    outcome_list = dice_outcomes(n, s, k)
    print("Number of {}-sum outcomes for {} {}-sided die is: {}".format(k, n, s, len(outcome_list)))
    print("Actual outcomes: {}".format(outcome_list))
    print("")
    return len(outcome_list)

def main():
    outcome(1, 6, 0)
    outcome(2, 6, 13)
    outcome(3, 6, 9)
    outcome(3, 6, 10)
    outcome(2, 6, 10)
    sys.exit(0)
    outcome(2, 6, 9)
    outcome(4, 6, 5)
    sys.exit(0)
    outcome(2, 6, 3)
    outcome(2, 6, 4)
    outcome(3, 6, 4)


if __name__ == '__main__':
    main()