def parse_name(name):
    possible_names = []
    possible_addons = ['tv', 'ttv', '_tv', '_ttv']
    removables = ['you exiled ', 'you assisted in exiling ', 'you disrupted ', '\n', '\x0c']
    # convert to lowercase for easier parsing
    name = name.lower()
    # remove
    for removable in removables:
        name = name.replace(removable, '')
    # add the cleaned up name to the list of possible names
    possible_names.append(name)
    # remove any additional signifiers
    for addon in possible_addons:
        if addon in name:
            possible_names.append(name.replace(addon, ''))
    return possible_names