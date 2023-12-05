import os

directory = input("введите директорию конфиг файла(если он зашифрованый введите a'eng'),(если нет нажмите Enter) - ")
ecd = input("где находится файл .ecd - ")
rar = input("куда хотите rar - ")
ung = input("куда(где) хотите(находится) расшифрованый config файл - ")
if directory=='a':
    os.rename(directory,ung)
admin = input("введите admin пароль - ")
if admin=='admin1(123)':
    file = open(ung)
    print(file.read())
    os.rename(ecd,rar)
    input("")
else:
    root = input("введите root пароль - ")
    if root=='root1(123)':
        file = open(ung)
        print(file.read())
        os.rename(ecd,rar)
        input("")