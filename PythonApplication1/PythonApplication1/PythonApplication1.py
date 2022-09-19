import win32api, platform, shutil, os, json, zipfile
import xml.etree.ElementTree as ET

def inf_os():
    drives: list = win32api.GetLogicalDriveStrings().replace(":\\", "").split("\x00")[:-1]
    print(platform.architecture())
    for char in drives:
        print(f"Info about disk {char}")
        total, used, free = shutil.disk_usage(f"{char}:\\")

        print(f"Total: {total // (2**30)} GiB")
        print(f"Used: {used // (2**30)} GiB")
        print(f"Free: {free // (2**30)} GiB")
        print("\n" * 2)

def filles():
    print("Введите нужное значение для выполнения необходимой функции ")
    print("1 для создания файла")
    print("2 для записи строки в файл")
    print("3 для чтения файла")
    print("4 для удаления файла")
    a = int(input())
    match a:
        case 1:
            filename = input("Введите имя файла ")
            with open(filename, 'w+') as f:
                f.write("")
        case 2:
             filename = input("Введите имя файла куда записать ")
             text = input("Введите что записать в файл (текст) ")
             with open(filename, 'w+') as f:
                f.write(text) 
        case 3:
            filename = input("Введите имя файла ")
            with open(filename, 'r') as f:
                print(f.read())
        case 4:
            filename = input("Введите имя файла который надо УДАЛИТЬ ")
            os.remove(filename)
    print("\n" * 2)

def json_f():
    print("Введите нужное значение для выполнения необходимой функции ")
    print("1 для создания файла")
    print("2 для создания нового объекта")
    print("3 для чтения файла")
    print("4 для удаления файла")
    a = int(input())
    match a:
        case 1:
            with open("file.json", "w+") as json_fi:
                inp = {"name" : "vasya", "age" : "16"}
                json_fi = json.dump(inp,json_fi)
        case 2:
            with open("file.json", "w+") as json_fi:
                inp = {"name" : "ilya", "age" : "19"}
                json_fi = json.dump(inp,json_fi)
        case 3:
            with open("file.json", 'r') as f:
                print(f.read())
        case 4:
            os.remove("file.json")
    print("\n" * 2)

def xml_f():
    print("Введите нужное значение для выполнения необходимой функции ")
    print("1 для создания файла")
    print("2 для записи новых данных")
    print("3 для чтения файла")
    print("4 для удаления файла")
    a = int(input())
    match a:
        case 1:
            xml_body=ET.Element('parent')
            tree = ET.ElementTree(xml_body)
            tree.write("sample.xml")
        case 2:
            text = input("Введите новые данные ")
            xml_body=ET.Element(text)
            tree = ET.ElementTree(xml_body)
            tree.write("sample.xml")
        case 3:
            with open("sample.xml", 'r') as f:
                print(f.read())
        case 4:
            os.remove("sample.xml")
    print("\n" * 2)

def zip_f():
    print("Введите нужное значение для выполнения необходимой функции ")
    print("1 для создания архива")
    print("2 для добавления файла в архив")
    print("3 для разорхивирования файла")
    print("4 для удаления файла")
    a = int(input())
    match a:
        case 1:
           z = zipfile.ZipFile("zippy.zip", 'w')
        case 2:
            if zipfile.is_zipfile('zippy.zip'):
                print("вывожу все файлы для удобства ", os.listdir())
                f_name = input("Введите название файла который добавить ")
                with zipfile.ZipFile('zippy.zip', 'w') as myzip:
                     myzip.write(f_name)
            else: print("А у вас нету архива")
        case 3:
            with zipfile.ZipFile('zippy.zip', 'r') as zip_file:
                zip_file.extractall()
        case 4:
            os.remove("zippy.zip")
    print("\n" * 2)

while True:
    print("Введите нужное значение для выполнения необходимой функции ")
    print("1 для вывода информации об ос")
    print("2 для работы с файлами ")
    print("3 для работы с JSON ")
    print("4 для работы с XML ")
    print("5 для работы с ZIP ")
    print("6 для выхода ")
    a = int(input())
    match a:
        case 1: inf_os()
        case 2: filles()
        case 3: json_f()
        case 4: xml_f()
        case 5: zip_f()
        case 6: break
    print("\n" * 2)