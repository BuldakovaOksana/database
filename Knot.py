import r_w_file
import working_file
import action_table
import modul1

def distribution(key_func,source,path):
    if (key_func == '1'): action_table.output_all(source)
    elif (key_func == '2'): working_file.append_info(source,path)
    elif (key_func == '3'): working_file.del_info(source, path)
    elif (key_func == '4'): modul1.sort(path)
    elif (key_func == '5'): action_table.sort_abc(source)
    elif (key_func == '6'): print('Всего хорошего!')
    else: print('Введите корректное число')




