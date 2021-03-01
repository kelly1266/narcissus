import re


def parse_name(name):
    """
    Parses enemy player name from notification
    :param name:
    :return:
    """
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


def parse_notif_from_tesseract(tesseract_str):
    """
    Parses the notification message from the tesseract string
    :param tesseract_str:
    :return:
    """
    tesseract_str = tesseract_str.split('\n')
    exile_string = ''
    for s in tesseract_str:
        if 'you' in s.lower():
            exile_string = s.lower()
    regex = re.compile('[^a-zA-Z0-9_ ]')
    exile_string = regex.sub('', exile_string)
    return exile_string


def change_color(image):
    return