vards = input('Ievadi vārdu: ')

with open('name.txt', 'a', encoding='utf-8')as f:
    f.write(vards + '\n')

