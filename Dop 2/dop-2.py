date = input("Vvedite name file: ")
n = input("Vvedite count firsts strings file: ")
with open(f"{date}.txt","r") as file:
    mas = file.readlines()
    for i in range(len(mas),len(mas)-n,-1):
        print(mas[i])