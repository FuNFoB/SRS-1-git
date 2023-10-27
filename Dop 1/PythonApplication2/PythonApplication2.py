date = input("Vvedite name file: ")
n = int(input("Vvedite count firsts strings file: "))
count=0
with open(f"{date}.txt","r") as file:
    while(count!=n):
        print(file.readline().rstrip())
        count=count+1
    file.close()