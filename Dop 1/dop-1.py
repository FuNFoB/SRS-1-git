date = input("Vvedite name file: ")
n = int(input("Vvedite count firsts strings file: "))
#print("hi")
coint=0
with open(f"{date}.txt","r") as file:
    #print("+1")
    #for i in range(0,n,1):
    while(count!=n):
        print(file.readline().rstrip())
        count++
        #with open("ooo.txt","w+") as newfile:
        #    newfile.write(file.readline)
        #newfile.close()
    file.close()
