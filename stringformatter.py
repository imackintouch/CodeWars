def namelist(names):
    """
    Given: an array containing hashes of names
    Return: a string formatted as a list of names separated by commas except for the last two names, which should be
    separated by an ampersand.

    Examples:
    namelist([ {'name': 'Bart'}, {'name': 'Lisa'}, {'name': 'Maggie'} ])
    # returns 'Bart, Lisa & Maggie'

    namelist([ {'name': 'Bart'}, {'name': 'Lisa'} ])
    # returns 'Bart & Lisa'

    namelist([ {'name': 'Bart'} ])
    # returns 'Bart'

    namelist([])
    # returns ''

    :param names:
    :return:


    """
    name_str = ''
    i = 0
    for name_item in names:
        if i < len(names)-1:
            name_str += name_item['name']
            if i < len(names)-2:
                name_str += ', '
        i += 1

    if len(names) > 1:
        name_str += ' & ' + name_item['name']
    elif len(names) == 1:
        name_str = names[0]['name']

    return name_str


name_info = [{'name': 'Bart'}, {'name': 'Lisa'}, {'name': 'Maggie'}]
print(namelist(name_info))
name_info = [{'name': 'Bart'}]
print(namelist(name_info))
name_info = [{'name': ''}]
print(namelist(name_info))
name_info = [{'name': 'Bart'}, {'name': 'Lisa'}]
print(namelist(name_info))
name_info = [{'name': 'Bart'}, {'name': 'Ernie'}, {'name': 'Lisa'}, {'name': 'Polly'}]
print(namelist(name_info))
