import Knot
import r_w_file
import view

def start():
    path_txt = input('Название файла с которым вы хотите работать: ')
    data = r_w_file.read_file(f'{path_txt}')
    number = ''
    while (number != '6'):
        number = view.get_request()
        Knot.init(data, path_txt)
        Knot.distribution(number)
        print()






