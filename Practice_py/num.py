# import random
# ra=[random.randint(1,100)for i in range(10)]
# print(ra)

# import numpy as np
# av=(np.random.randint(1,100,size=10))
# to_list=av.tolist()
# print(to_list)

# import random
# ab=random.sample(range(1,100),10)
# print(ab)
# ab.sort()
# print(ab)

import matplotlib.pyplot as ptl
a=[1,28,3,4,50]
b=[43,5,61,7,8]
ptl.plot(a,b)
ptl.title("Added")
ptl.xlabel("X Axis")
ptl.ylabel("Y Axis")
ptl.show()