
def output_all(source):
    for i in source:
        print(f'{i} {source[i]["name"]} {source[i]["surname"]} {source[i]["class"]}', end='')
        print()

def sort_class(source,num_class):
    for i in source:
        if (source[i]["class"] == str(num_class)):
            print(f'{i} {source[i]["surname"]} {source[i]["name"]} - {source[i]["class"]}')

def sort_abc(source):
    result = []
    for i in source:
        result.append(f'{source[i]["surname"]} {source[i]["name"]} id - {i}')
    result.sort()
    for i in result:
        print(i)

