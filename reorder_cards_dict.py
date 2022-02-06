#!/user/local/bin/python3.7

NO_ONE = 'No One'

def display(cards):
    print("My card list is(preceder card user is listed 2nd in each row:)")
    for card_key in cards.keys():
        print(cards[card_key], card_key)
    print

def build_card_data_from_file(data_file):
    #
    # Build a dictionary from a file of user data where each entry is keyed by a preceder user.
    #
    users_dict = {}
    users_set = set()
    with open(data_file, mode='r') as infile:
        prev_user = NO_ONE
        for record in infile:
            # print(record)
            user = record.split(':')[4]
            users_dict[prev_user] = user
            prev_user = user
            users_set.add(user)

    return users_dict, users_set

def find_leader(cards, cards_set):
    #
    # First, try to find the card that has a preceder = to NO_ONE. If it
    # exists then the key of the leader card is NO_ONE. Otherwise we need to find
    # a card user that has no valid preceder and return its key.
    #
    if cards.get(NO_ONE) is not None:
        return (NO_ONE, cards.get(NO_ONE))

    for card in cards.items():          # cards.items is a list of tuples where first element is the key.
        if card[0] in cards_set:        # Utilize card set fr O(1) searching of actual users.
            continue
        else:
            return card

def display_user_card(card):
    print("Card Preceder is:'{}', Card User is:'{}' ".format(card[0], card[1]))

def remove_card(card, cards, cards_set):
    print("Removing the card where preceder is:'{}' and user is:'{}'".format(card[0], card[1]))
    del cards[card[0]]
    cards_set.discard(card[1])

def display_restored_card_order(cards, leader):
    # Set up key for leader card. Leader card has NO_ONE in front.
    card_key = leader[0]

    while card_key is not None:
        card_user = cards.get(card_key)
        if card_user is not None:
            print(card_user, card_key)
        card_key = card_user      # The current user will become the key to get the next user in original sequence.


if __name__ == '__main__':
    user_cards, user_cards_set = build_card_data_from_file('/Users/ianmcfarlane/tmp/passwd')
    display(user_cards)

    print("Finding User Card Leader...")
    leader_user_card = find_leader(user_cards, user_cards_set)
    display_user_card(leader_user_card)

    remove_card(leader_user_card, user_cards, user_cards_set)
    print("Finding the new leader")
    leader_user_card = find_leader(user_cards, user_cards_set)
    display_user_card(leader_user_card)

    print("\nRestoring order to user cards:")
    display_restored_card_order(user_cards, leader_user_card)

#
# Code should be changed to have build_card_data_from_file return 2 structures.
#  - A dictionary of card users with preceder user values as keys...useful for sequencing
#  - A set that consists of the actual users which will be useful for O(1) searches.
# Portions of this data structure can then be passed around as needed.