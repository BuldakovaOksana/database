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
    elif(key_func == '6'): return 'Vs'
    else: print('Введите корректное число')

def init_gl(source_in,path_in):
    global source
    source = source_in
    global path
    path = path_in

do_it = { '1':action_table.output_all(source),'2':working_file.append_info(source,path),
            '3':working_file.del_info(source, path),'4':modul1.sort(path), '5':action_table.sort_abc(source)}

def distribution_sl(key_fun):



