names_list = ["shevi", "Hila", "Ayelet", "Yael", "Chana","Efrat"]
file_name = input("הקש את שם הקובץ")
f = open(f'{file_name}.txt', "w+")
for name in names_list:
    f.write(name + "\n")
f = open(f'{file_name}.txt', "r")
file_r = f.read().split()
for i in range(1, len(file_r), 2):
    print(file_r[i])
