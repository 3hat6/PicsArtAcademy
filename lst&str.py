def _replace(source, old, new):
    """ the function replace all old words to new in source string """
    result = ''
    _list = source.split(' ')
    for elem in _list:
        if elem == old:
            result += new + ' '
        else:
            result += elem + ' '
    return result.strip()


_str = "barev brother how are u brother sax lava brother "
#print(_replace(_str, 'brother', 'bro'))

def _split(source, sep):
    # aranc probel verji sax lavan korcnuma u verji element@ chi qcum mej@ xi ?
    result = []
    attached = ''
    word = ''
    if sep == ' ':
        for elem in source:
            if elem == sep:
                result.append(attached)
                attached = ''
            else:
                attached += elem
    for elem in source:
        if word == sep:
            result.append(attached.strip())
            attached = ''
            word = ''
        elif elem != ' ':
            word += elem
        elif elem == ' ':
            attached += word + ' '
            word = ''
    print(source)
    return result

#print(_split(_str, "brother"))

def _joint(data, sep):
    result = ''
    for elem in data:
        result += elem + sep
    return result


#print(_joint(["Hi", 'whats up', 'all is okay?'], ' '))
#print(_joint(["Hi", 'whats up', 'all is okay'], ' niggah '))
