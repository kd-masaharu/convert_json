import csv

filename = 'data.csv'
print("[")
with open(filename, encoding='utf8', newline='') as f:
    data = csv.reader(f)
    data = list(data)
    di = {}
    for i in range(1,len(data)):
        di["questionId"] = i
        di["genreId"] = data[i][0]
        di["question"] = data[i][1]
        di["answers"] = [
            f"1.{data[i][2]}",
            f"2.{data[i][3]}",
            f"3.{data[i][4]}",
            f"4.{data[i][5]}"
        ]
        di["correct"] = data[i][6]
        di["explanation"] = data[i][7]
        di["url"] = data[i][8]
        if i != len(data)-1:
            print("\t"+str(di).replace('\'','\"')+',')
        else:
            print("\t"+str(di).replace('\'','\"'))
print("]")