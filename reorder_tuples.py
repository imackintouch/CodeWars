import random
import sys
from collections import namedtuple

QueueUser = namedtuple('User', 'preceder user_id')
NO_ONE = 'NoOne'


def display_list(tuple_list):
    for item in tuple_list:
        print(item)


def scramble(orig):
    dest = orig[:]
    random.shuffle(dest)
    return dest


def binary_search(alist, item):
    first = 0
    last = len(alist)-1
    found = False
    midpoint = 0

    while first <= last and not found:
        midpoint = (first + last)//2
        if alist[midpoint].preceder == item:
            found = True
        else:
            if item < alist[midpoint].preceder:
                last = midpoint - 1
            else:
                first = midpoint + 1

    if found:
        return alist[midpoint]
    else:
        return QueueUser('Not found', 'Not found')


def build_user_queue_from_file(data_file):
    #
    # Build an ordered queue of users from a file
    # modelling each user as a namedtuple of type User
    #
    user_q = []
    with open(data_file, mode='r') as infile:
        prev_user = NO_ONE
        for record in infile:
            # print(record)
            user = record.split(':')[4]
            u = QueueUser(prev_user, user)
            user_q.append(u)
            prev_user = user
    return user_q


def restore_queue_order(user_q):
    sorted_userq = sorted(user_q, key=lambda user_name: user_name.preceder)  # Sort tuples by preceder fields

    user = binary_search(sorted_userq, NO_ONE)
    if user.user_id == 'Not found':
        print("\n Cannot find queue leader! Something very weird happened...Exiting")
        sys.exit(-1)

    new_user_q = [user]

    print("\n Queue leader user is {}".format(user))
    while len(new_user_q) != len(user_q):
        successor_user = binary_search(sorted_userq, user.user_id)

        if successor_user.user_id == "Not found":
            print("Something very weird happened!! Cannot find a successor..Exiting")
            sys.exit(-1)

        # Insert successor user at end of list
        new_user_q.append(successor_user)
        user = successor_user

    return new_user_q


def validate(original_list, new_list):
    # Test equality of 2 lists

    if original_list == new_list:
        print("\nThe new list is equal to the original one. Victory...is Life!!!!")
    else:
        print("\nThe reconstituted new list is NOT equal to the original one. EPIC FAIL!!!!")


if __name__ == '__main__':
    userq = build_user_queue_from_file('/Users/ianmcfarlane/tmp/passwd')
    print("Original order of user tuples")
    display_list(userq)

    # Scramble original list of users
    scrambled_userq = scramble(userq)
    print("\nHere's a scrambled version of the userq that we will need to re-order later:")
    display_list(scrambled_userq)

    print("\nRestoring order to scrambled queue:")
    new_userq = restore_queue_order(scrambled_userq)

    print("\nSize of new_userq is:{}\n".format(len(new_userq)))
    print("Contents of new_userq:")
    display_list(new_userq)

    validate(userq, new_userq)
