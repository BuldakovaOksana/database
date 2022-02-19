import additional
import r_w_file
import working_file
import action_table
import view

path_txt = 'base_data.txt'
data = r_w_file.read_file(f'{path_txt}')
count = 0
while(count < 6):
    number = view.get_request()
    additional.init_gl(data,path_txt)
    additional.distribution_sl(number)




