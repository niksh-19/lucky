with open("mydefaults.ini.txt") as ini_file:
    data=ini_file.read()
y=[]
z=[]
for x in data:
    if x.isalpha():
        y.append(x)
    elif x.isdigit():
        z.append(x)
print("no. of alphabets: ",len(y)) 
print("instance of numbers: ",len(z))