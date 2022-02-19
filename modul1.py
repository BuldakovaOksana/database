


def sort(data):
    a = input('Введите номер класса: ')
    file=open(data, 'r')
    for line in file:
        arr = line.split()
        if arr[3]==a:
            print(f'{arr[0]} {arr[1]} {arr[2]}')
          
