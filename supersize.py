def superSize(i):
    """

    superSize takes an integer and rearrangres it digits to produce the largest possible value
    e.g. supersize(1537) is 7531

    :param i: integer value to supersize
    :return:
    """

    return int(''.join(sorted(str(i), reverse=True)))


print(superSize(12))
print(superSize(1005))
print(superSize(35988))
