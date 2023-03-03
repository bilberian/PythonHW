import json

db_path = 'phone_book.json'
welcome = 'Enter command: 1 - add record | 2 - edit info | 3 - delete | 4 - load DB | q - Quit\n'
phone_book = {}

def print_book(book):
    for k,v in book.items():
        print (k," - ", end = " | ")
        for i,j in v.items():
            print (i, j, end = " | ")
        print()

def save_db(path, db):
    with open(path, 'w', encoding='utf-8') as fh: # открываем файл на запись
        fh.write(json.dumps(db, ensure_ascii=False)) # преобразовываем словарь data в unicode-строку и записываем в файл
        print('Data succesfully saved')

def load_db(path):
    # загрузить из json
    with open(path, 'r', encoding='utf-8') as fh:  # открываем файл на чтение
        BD_local = json.load(fh)  # загружаем из файла данные в словарь data
    print('Data succesfully loaded')
    return BD_local

def new_record(path):
    name = input('Insert name: ')
    phone = input('Insert phone number: ')
    birthday = input('Insert birthday: ')
    division = " | "
    with open(path, 'a', encoding='utf-8') as fh:
            fh.write(f'{name} {division} {phone} {division} {birthday}\n\n')
    print("New record successfully added!")

def edit_record(path):
    with open(path, 'r', encoding='utf-8') as fh:
        edited_record = list(fh.readlines())
    num_edit = int(input('Insert record number to edit: '))
    name = input('Insert new name: ')
    phone = input('Insert new phone number: ')
    birthday = input('Insert new birthday: ')
    division = " | "   
    edited_record = edited_record[:num_edit - 1] + [f'{name} {division} {phone} {division} {birthday}\n'] + edited_record[num_edit:]
    with open(path, 'w', encoding='utf-8') as fh:
        fh.write(''.join(edited_record))
    print('The record is succesfully edited')

def delete_record(path):
    with open(path, 'r', encoding='utf-8') as fh:
        deleted_record = list(fh.readlines())
    num_delete = int(input('Insert record number to delete: '))
    deleted_record = deleted_record[:num_delete - 1] + deleted_record[num_delete:]
    with open(path, 'w', encoding='utf-8') as fh:
        fh.write(''.join(deleted_record))
    print('The record is succesfully deleted')        
 
try:
    phone_book = load_db(db_path)
except:
    phone_book = {
    'Миша гараж':{'phone': ['72443351195','72627397543'] , 'birthday': '11-02-2010', 'email':"mail@mail.ru"},
    'Sasha':{'phone': ['78436840045','77554802591']}}

    print('Data base not found. Using test data base')


action = None
while action != 'q':
    action = input(f'{welcome}').lower()
    if action == '1':
        new_record(db_path)
    elif action == '2':
        edit_record(db_path)
    elif action == '3':
        delete_record(db_path)
    elif action == '4':
        load_db(db_path)
save_db(db_path, phone_book)