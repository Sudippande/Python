import csv
with open('Book1.csv','r') as f:
    read=csv.reader(f)
    for r in read:
        print(r)