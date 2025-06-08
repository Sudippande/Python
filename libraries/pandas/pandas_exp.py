#pandas program to read csv file.
import pandas as pd
# x=pd.read_csv('sudip.csv',header=0).values # it will display the sex of the person
# y=pd.read_csv('sudip.csv',usecols=['name','Age']).values#it willnot display sex
# print(x)
# print(y)

# #write in and save in csv using panda
# import pandas as pd
# import numpy as np

# # Create a 2x3 array: first row is headers, second row is data
# a = np.array([
#     ['Name', 'Age', 'Address','Gender'],
#     ['sudip', 3, 'Birendrbazar','m'],
#     ['ramesh',34,'jkp','M']
# ])

# # Use the first row as columns, and second row as the data
# df = pd.DataFrame(a[1:], columns=a[0])
# print(df)

# #save your dataframe with
# df.to_csv('sudip1.csv')
# print("Saved the Data")

# #to read 
# data=pd.read_csv('sudip1.csv')
# print(data)


# import numpy as np
# a=np.random.randint(1,100,(2,4))
# print(a)

# import random
# n=random.sample(range(1,100),10)
# n.sort()
# print(n)

# d={"col1":[1,2,3],"col2":["A","B","C"]}
# df=pd.DataFrame(d)
# df.dropna(inplace=True)
# df=df[df.col1!=1]
# print(df)

