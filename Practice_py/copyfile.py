try:
    with open("text.txt",'r') as file:
        re=file.read()
except FileNotFoundError as er:
    print("error :",er)
    re=None
if re is not None:

    try:
        with open("std.txt",'w') as fp:
            fp.write(re)
    except FileExistsError as e:
        print("Error:",e)