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
        dice_roll_str = dice_roll_str.rstrip(",")
        dice_roll_list = dice_roll_str.split(",")
        sum = 0
        for i in range(0, len(dice_roll_list)):
            sum += int(dice_roll_list[i])
        #print("My sum is:{}".format(sum))
        if sum == k:
            return True
        else:
            return False

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
        #print("Calculating outcome({},{},{})".format(n,s,k))

        if k > (n * s): # Sum is larger than maximum possible die sum.
             #print("Sum {} is larger than maximum possible die sum: {} * {}".format(k, n, s))
             return []

        if n == 1 and k > 0 : # I am down to calculating the outcome for a single die but only if sum is > 0!
            return [str(k)]

        dice_outcome_list = []
        for i in range(1, s + 1):   # there is no way we can exceed the max value of a side to solve this problem.

            # print(i)
            if (k - i) <= 0: # we cannot have a sum of 0. (we can probably make this another stopping condition)
                continue

            if (k < n): # Desired outcome sum is smaller than minimum possible die sum
                #print("Sum {} is smaller than minimum possible die sum: {} * {}".format(k, n, s))
                continue

            outcome_list = dice_outcomes(n-1, s, k-i)
            #print("Outcome list at start of main loop:{}".format(outcome_list))
            #
            # Now let's look at this list of die roll outcomes
            #
            for die_roll_outcome in outcome_list:
                dice_roll_str = str(i) + "," + str(die_roll_outcome).rstrip(',')

                #print("A given dice roll string for {}, {}, {} is: {}".format(n, s, k, dice_roll_str))
                if is_desired_sum(dice_roll_str, k):
                    #print("The sum of {} MEETS current outcome criteria {}".format(dice_roll_str, k))
                    dice_outcome_list.append(dice_roll_str)
                    #print("outcome_list is now: {}".format(dice_outcome_list))
                #else:
                    #print("{} does not meet current outcome criteria {}".format(dice_roll_str, k))

        return dice_outcome_list

    outcome_list = dice_outcomes(n, s, k)
    #print("Number of {}-sum outcomes for {} {}-sided die is: {}".format(k, n, s, len(outcome_list)))
    print("Actual outcomes: {}".format(outcome_list))
    return len(outcome_list)

def die_outcome_display(n, s, k):
    print("Number of {}-sum outcomes for {} {}-sided die is: {}".format(k, n, s, outcome(n, s, k)))
    print("")

die_outcome_display(2, 6, 13)
die_outcome_display(3, 6, 3)
die_outcome_display(3, 6, 10)
die_outcome_display(2, 6, 10)
die_outcome_display(2, 6, 9)
die_outcome_display(4, 6, 5)
die_outcome_display(2, 6, 3)
die_outcome_display(2, 6, 4)
die_outcome_display(3, 6, 4)
die_outcome_display(3, 6, 5)
die_outcome_display(4, 6, 5)
die_outcome_display(4, 7, 6)
die_outcome_display(1, 6, 0)