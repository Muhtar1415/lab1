#task1
import os
path=r"C:\Users\user\Desktop\pp2"
dir_list=os.listdir(path)
print("Files and directories in: ", path)
print(dir_list)

#task2
import os
path=r"C:\Users\user\Desktop\pp2"

print(f"{path} exists: {os.access(path, os.F_OK)}")
print(f"{path} is readable: {os.access(path, os.R_OK)}")
print(f"{path} is writeable: {os.access(path, os.W_OK)}")
print(f"{path} is executable: {os.access(path, os.X_OK)}")

#task3
import os
def check(path):
    if os.path.exists(path):
        print("Name of file: ", os.path.basename(path))
        print("Name of directory: ", os.path.dirname(path))

path=r"C:\Users\user\Desktop\pp2"
print(check(path))
    
    
#task4
line=open("sometext.txt", "r")
print(len(line.readlines()))
line.close()

#task5
f = open("text5.txt", "w")
li = input("Input a list of values separated by commas: ").split(", ")
f.write(str(li))
f.close()

#task6
from string import ascii_uppercase

path = r"C:\Users\user\Desktop\pp2"
if not os.access(new_path, os.F_OK):
    os.makedirs(new_path)

for soz in ascii_uppercase:
    f = open(f"{new_path}\\{soz}.txt", "w")
    f.write(f"This is {soz}'s txt file")
    f.close()

#task7
with open("builtin_func.txt", "r") as f1:
    f2 = open(f"copy_builtin_func.txt", "w")
    for line in f1:
        f2.write(line)
    f1.close()

#task8
def delete_file(path):
    if os.path.exists(path):
        if os.access(path, os.W_OK):
            try:
                os.remove(path)
                print(f"Файл '{path}' успешно удален.")
            except Exception as e:
                print(f"Ошибка при удалении файла: {e}")
            else:
                print("The file deleted")
        else:
            print(f"Отсутствует право на запись в файл '{path}'.")
    else:
        print(f"Файл '{path}' не существует.")

delete_file(r"C:\Users\user\Desktop\pp2")