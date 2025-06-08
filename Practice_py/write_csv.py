import csv
data=[['name','age','int'],['sudip','33','335']]
with open("Python/Practice_py/sudip1.csv",'w',newline='') as f:
    re=csv.writer(f)
    re.writerows(data)
    print("File is written succesfully")

with open("Python/Practice_py/sudip1.csv",'r') as f:
    reader=csv.DictReader(f)
    for rea in reader:
        print(rea)

# import pandas as pd
# re=pd.read_csv("Python/Practice_py/sudip1.csv")
# for a in re:
#     print(a)
    