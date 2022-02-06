#
# Strip this down to make it more palatable for the Codewars site.
# e.g. strip out any prints and make all functions child functions of the outcome function.
# Also see if I can come up with a version that doesn't build up lists but returns only integer sums?
#
import sys

"""
dice roll outcome program
"""

def outcome(n, s, k):

    def is_desired_sum(dice_roll_str, k):
        dice_roll_list = dice_roll_str.rstrip(',').split(',')
        sum = 0
        for i in range(0, len(dice_roll_list)):
            sum += int(dice_roll_list[i])
        return sum == k

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

        if k > (n * s) or k < n : # Sum > the max possible sum of die or sum < total die is not doable so stop!
             return []

        if n == 1 : # I am down to calculating the outcome for a single die but only if sum is > 0!
            return [str(k)]

        dice_outcome_list = []
        for i in range(1, s + 1):   # there is no way we can exceed the max value of a side to solve this problem.

            outcome_list = dice_outcomes(n-1, s, k-i)

            for die_roll_outcome in outcome_list:
                dice_roll_str = str(i) + "," + str(die_roll_outcome).rstrip(',')

                if is_desired_sum(dice_roll_str, k):
                    dice_outcome_list.append(dice_roll_str)

        return dice_outcome_list

    outcome_list = dice_outcomes(n, s, k)
    print("Actual outcomes: {}".format(outcome_list))
    return len(outcome_list)

def dice_outcome_display(n, s, k):
    print("Number of {}-sum outcomes for {} {}-sided die is: {}".format(k, n, s, outcome(n, s, k)))
    print("")

dice_outcome_display(1, 6, 0)
dice_outcome_display(1, 0, 1)
dice_outcome_display(0, 6, 1)
dice_outcome_display(1, 6, 1)
dice_outcome_display(1, 6, 2)
dice_outcome_display(1, 6, 3)
dice_outcome_display(1, 6, 4)
dice_outcome_display(1, 6, 5)
dice_outcome_display(1, 6, 6)
dice_outcome_display(1, 6, 7)

dice_outcome_display(2, 6, 1)
dice_outcome_display(2, 6, 2)
dice_outcome_display(2, 6, 3)
dice_outcome_display(2, 6, 4)
dice_outcome_display(2, 6, 5)
dice_outcome_display(2, 6, 6)
dice_outcome_display(2, 6, 7)
dice_outcome_display(2, 6, 8)
dice_outcome_display(2, 6, 9)
dice_outcome_display(2, 6, 10)
dice_outcome_display(2, 6, 11)
dice_outcome_display(2, 6, 12)
dice_outcome_display(2, 6, 13)

dice_outcome_display(3, 6, 6)
dice_outcome_display(3, 6, 9)
dice_outcome_display(3, 6, 10)
dice_outcome_display(3, 6, 11)
dice_outcome_display(3, 6, 12)
dice_outcome_display(3, 6, 15)

dice_outcome_display(4, 6, 5)