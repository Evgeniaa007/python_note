import Note as model
import file_functions as file_operation

class Commands:

    '''Добавление заметки'''
    def add_note():
        title = input("Введите заголовок заметки: ")
        body = input("Введите описание заметки: ")
        note = model.Note(title=title, body = body) # Создание экземплеяра класса заметки
        array_notes = file_operation.read_file() # Создание массива с заметками и чтение его в существующем файле
        # Прохождение по созданному массиву с заметками и проверка созданной заметки на уникаольность id в существующем массиве
        for i in array_notes: 
            for j in array_notes:
                if model.Note.get_id(note) == model.Note.get_id(j): # Если id созданной заметки равен id любой другой заметки
                    model.Note.set_id(note) # Увеличиваем ей id с помощью метода counter()
        array_notes.append(note) # Добавляем созданную заметку в массив с заметками
        file_operation.save_to_json(array_notes) # Запись массива с заметками в файл
        print("Заметка добавлена в журнал заметок!")


    '''Удаление заметки'''
    def del_notes():
        id = input("Введите ID удаляемой заметки: ")
        array_notes = file_operation.read_file() # Создание массива с заметками и чтение его в существующем файле
        flag = True
        for note in array_notes:
            if id == model.Note.get_id(note):
                array_notes.remove(note)
                flag = False
        if flag: # Если flag остался неизменным, значит такого id нет
            print("нет такого id")
        else:
            file_operation.save_to_json(array_notes)
            print("Заметка с id: ", id, " успешно удалена!")


    '''Редактирование заметки'''
    def change_note():
        id = input("Введите ID изменяемой заметки: ")
        array_notes = file_operation.read_file()
        flag = True
        array_notes_new = [] # Создание нового пустого массива 
        for note in array_notes:
            if id == model.Note.get_id(note):
                note.title = input("измените  заголовок: ")
                note.body = input("измените  описание: ")
                model.Note.set_date(note)
                flag = False
            array_notes_new.append(note)

        if flag:
            print("нет такого id")
        else:
            file_operation.save_to_json(array_notes_new)
            print("Заметка с id: ", id, " успешно изменена!")


    '''Вывод журнала'''
    def show(text):
        array_notes = file_operation.read_file() # Создание массива с заметками и чтение его в файле
        if text.__eq__("all"):
            print("ЖУРНАЛ ЗАМЕТОК:")
            for note in array_notes:
                print(model.Note.show_note(note))
        
        elif text.__eq__("ID"):
            for note in array_notes:
                print("ID: ", model.Note.get_id(note)) # Получение всех id в массиве заметок
            id = input("Введите id заметки: ")
            flag = True
            for note in array_notes:
                if id == model.Note.get_id(note):
                    print(model.Note.show_note(note))
                    flag = False
            if flag: # Если flag остался неизменным, значит такого id нет
                print("Нет такого ID")

        elif text.__eq__("date"):
            for note in array_notes:
                print("date: ", model.Note.get_creation_date(note)) # Получение всех date в массиве заметок
            date = input("Введите дату в формате: dd.mm.yyyy: ")
            flag = True
            for note in array_notes:
                if date in model.Note.get_creation_date(note):
                    print(model.Note.show_note(note))
                    flag = False
            if flag: # Если flag остался неизменным, значит такой даты нет
                print("Нет такой даты")