data = input("Vvedite Name file: ")
k=1
with open(f"{data}.txt","r") as file:
    mas = file.readlines()
    for i in range(0,len(mas),1):
            print(str(k)+" "+mas[i])
            k=k+1