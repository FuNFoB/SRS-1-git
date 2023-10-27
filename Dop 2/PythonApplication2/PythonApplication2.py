date = input("Vvedite name file: ")
n = int(input("Vvedite count firsts strings file: "))
count=0
mas = []
with open(f"{date}.txt","r") as file:
    
    for line in file:
        mas.append(line.rstrip())
    for i in range(len(mas),len(mas)-n,-1):
        print(mas[i-1])
        count=count+1
    file.close()