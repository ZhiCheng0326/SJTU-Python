infile = open("input.txt","r")
outfile = open("final.txt","w")
y = infile.readlines()
lis = []
for i in range(len(y)):
    if y[i] == "\n":
        if y[i+1] == "\n" and y[i+2] != "\n":
            lis.append("\n")
            lis.append("\n")

        elif y[i-1] != "\n" and y[i+1] != "\n":
            lis.append("\n")
            lis.append("\n")

        else:
            continue
    else:
        new = y[i].replace("\n","")
        lis.append(new)


final = "".join(lis)
outfile.write(final)

infile.close()
outfile.close()
