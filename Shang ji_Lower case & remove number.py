x = raw_input("Please input:")

for i in x:
    for j in range(10):
        y=str(j)
        x = x.replace(y, '')

x = x.lower()
    
print x
