import Note


def read_file():
        try: # Попытка выполнить функцию, но если не создан файл - выдает ошибку, которая уходит в 'except'
            array = [] 
            with open('notes.json', 'r', encoding='utf-8') as f: # 'r' - чтение данных
                notes = f.read().strip().split("\n") # Разделение заметок по строкам
                for n in notes:
                    split_n = n.split(';') # Разделение заметок по ";"
                    note = Note.Note( # Создание эксемпляра заметки
                        id = split_n[0], title = split_n[1], body = split_n[2], creation_date = split_n[3])
                    array.append(note)
        except FileNotFoundError:
            print('Файла нет. Сначала введите данные\n')    
        finally:
            return array

def save_to_json(array):
    with open('notes.json', 'w', encoding='utf-8') as fw: # 'w' - перезапись данных
        fw.seek(0)
    with open('notes.json', 'a', encoding='utf-8') as fa: # 'a' - добавление данных
        for note in array:
            fa.write(f'{Note.Note.to_string(note)}\n') # Запись заметки в файл

# def read_file():
#     try:
#         array = []
#         file = open("notes.csv", "r", encoding='utf-8')
#         notes = file.read().strip().split("\n")
#         for n in notes:
#             split_n = n.split(';')
#             note = Note(
#                 id=split_n[0], title=split_n[1], body=split_n[2], date=split_n[3])
#             array.append(note)
#     except Exception:
#         print('Нет сохраненных заметок.')
#     finally:
#         return array


   
# def write_file(array, mode):
#     file = open("notes.csv", mode = 'w', encoding='utf-8')
#     file.seek(0)
#     file.close()
#     file = open("notes.csv", mode=mode, encoding='utf-8')
#     for notes in array:
#         file.write(Note.Note.to_string(notes))
#         file.write('\n')
#     file.close 