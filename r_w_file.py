import os.path

def write_file(source, path):
    file = open(path, 'w')
    sup_str = ''
    for i in source:
        sup_str += f'{i} {source[i]["name"]} {source[i]["surname"]} {source[i]["class"]}'
        file.writelines(f'{sup_str} \n')
        sup_str = ''
    file.close()


def read_file(path):
    result = {}
    if(os.path.lexists(path)):
        file = open(path, 'r')
        for line in file:
            sup_arr = line.split()
            result[sup_arr[0]] = {'name': sup_arr[1], 'surname': sup_arr[2], 'class': sup_arr[3]}
        file.close()
    else:
        file = open(path, 'a')
        file.writelines('')
        file.close()
    return result