data = input("Vvedite name file: ")
print("Nachite vvodit stroki")
with open(data,"a") as file:
    while True:
        str = input()
        if str == "" or str ==" ":
            print("File zapisan")
            break
        else:
            file.write(str)
            file.write("\n")
