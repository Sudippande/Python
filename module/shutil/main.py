import shutil
import os
count=0
for file in os.listdir():
    count+=1
    print(file,f"file {count}")