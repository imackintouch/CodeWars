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

    def dice_outcome(n, s, k):

        if k > (n * s) or k < n : # Sum > the max possible sum of die or sum < total die is not doable so stop!
             return []

        if n == 1 : # I am down to calculating the outcome for a single die but only if sum is > 0!
            return [k]

        dice_outcome_list = []
        for i in range(1, s + 1):   # there is no way we can exceed the max value of a side to solve this problem.
            dice_outcome_list += [ i + dice_roll_sum for dice_roll_sum in dice_outcome(n-1, s, k-i)
                                   if i + dice_roll_sum == k ]

        return dice_outcome_list

    return len(dice_outcome(n,s, k))


def dice_outcome_display(n, s, k):
    print("Number of {}-sum outcomes for {} {}-sided die is: {}".format(k, n, s, outcome(n, s, k)))

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


