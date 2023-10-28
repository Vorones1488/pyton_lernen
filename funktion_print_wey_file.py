def get_file_info(file_path):
    cel_atr = file_path.count('.')
    if cel_atr != 1 and cel_atr != 0:
        file_path_copy = file_path.split('/')
        names = file_path_copy[-1].split('.')
        *_, atribut =  names
        names.pop(-1)
        name = '.'.join(names)
        file_path_copy.pop(-1)
        wey = '/'.join(file_path_copy)
        res = (wey, name, ('.' + atribut))
    elif cel_atr == 0:
        wey, name, atribut = file_path, "", ""
        res = (wey, name, atribut)
    else:
        file_path = file_path.replace('.', '/.')
        file_path = file_path.split('/')
        *wey, name, atribut = file_path
        wey = '/'.join(wey)
        res = (wey + '/', name, atribut)

    return res