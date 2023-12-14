import csv

filename = 'data.csv'
print('[')
with open(filename, encoding='utf8', newline='') as f:
    data = csv.reader(f)
    data = list(data)
    for i in range(1,len(data)):
        print('\t{')
        print(f'\t\t"questionId":"{i}",')
        print(f'\t\t"genreId":"{data[i][0]}",')
        print(f'\t\t"question":"{data[i][1]}",')
        print(f'\t\t"answers":[')
        print(f'\t\t\t"1.{data[i][2]}",')
        print(f'\t\t\t"2.{data[i][3]}",')
        print(f'\t\t\t"3.{data[i][4]}",')
        print(f'\t\t\t"4.{data[i][5]}"')
        print(f'\t\t],')
        print(f'\t\t"correct":"{data[i][6]}",')
        print(f'\t\t"explanation":"{data[i][7]}",')
        print(f'\t\t"url":"{data[i][8]}"')
        if i == len(data)-1:
            print('\t}')
        else:
            print('\t},')
print(']')