import additional
import r_w_file
import view

path_txt = 'base_data.txt'
data = r_w_file.read_file(f'{path_txt}')
number = ''
while(number != '6'):
    number = view.get_request()
    additional.distribution(number,data,path_txt)





