data = input("Vvedite name file: ")
count = int(input("Vvedite count string: "))
k=1
with open(f"{data}.txt", "r") as file:
    mas = file.readlines()
    a=1
    for i in range(0,len(mas),1):
        if (a<=count):
            #print("+1")
            with open(f"{k}.txt","a") as newfile:
                #print("Create File")
                newfile.write(mas[i])
                newfile.close()
        else:
            k=k+1
            with open(f"{k}.txt","a") as newfile:
                #print("Else File")
                newfile.write(mas[i])
            a=1
        a=a+1
    file.close()
