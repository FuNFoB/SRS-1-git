name1=input("Vvedite 1 file: ")
name2=input("Vvedite 2 file: ")
name3 = input("Vvedite name outfile: ")
with open(f"{name3}.txt", 'w') as outfile:
    with open(f"{name1}.txt","r") as infile1:
        outfile.write(infile1.read())
    outfile.write("\n")
    with open(f"{name2}.txt","r") as infile2:
        outfile.write(infile2.read())