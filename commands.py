import Note
import file_functions as ff

class Commands:

    def add_note():
        title = input("Введите заголовок:\n")
        body = input("Введите текст заметки:\n")
        note = Note.Note(title=title, body=body)
        array_notes = ff.read_file()
        for i in array_notes:
            if Note.Note.get_id(note) == Note.Note.get_id(i):
                Note.Note.set_id(note)
        array_notes.append(note)
        ff.write_file(array_notes, 'a')
        print("Заметка создана")


    def edit_note():
        title = input("Введите заголовок заметки, которую хотите изменить: \n")
        array_notes = ff.read_file()
        flag = True
        edited_array = []
        for i in array_notes:
            if title == Note.Note.get_title(i):
                new_title = input("Введите новый заголовок: \n")
                Note.Note.set_title(i, new_title)
                new_body = input("Введите новый текст заметки: \n")
                Note.Note.set_title(i, new_body)      
                Note.Note.set_date(i)
                flag = False
            edited_array.append(i)
        if flag == False:
            ff.write_file(edited_array, 'a')
            print("Редактирование заметки завершено")
        else:
            print("Заметки с таким названием не существует")


    def del_note():
        title = input("Введите заголовок заметки для удаления: \n")
        array_notes = ff.read_file()
        flag = True
        for i in array_notes:
            if title == Note.Note.get_title(i):
                array_notes.remove(i)
                flag == False
        if flag == False:
            ff.write_file(array_notes, 'a')
            print("Заметка удалена")
        else:
            print("Заметки с таким названием не существует")

    
    def show_note(text):
        array_notes = ff.read_file()

        if text == "all":
            print("Заметки:")
            for i in array_notes:
                print(Note.Note.map_note(i))

        elif text == "ID":
            for i in array_notes:
                print("ID: ", Note.Note.get_id(i))
            id = input("\nВведите ID заметки: ")
            flag = True
            for i in array_notes:
                if id == Note.Note.get_id(i):
                    print(Note.Note.map_note(i))
                    flag = False
            if flag:
                print("Нет такого ID")

        elif text == "date":
            date = input("Введите дату в формате: dd.mm.yyyy: ")
            flag = True
            for i in array_notes:
                date_note = str(Note.Note.get_date(i))
                if date == date_note[:10]:
                    print(Note.Note.map_note(i))
                    flag = False
            if flag:
                print("В эту дату нет сохраненных заметок")
        else:
            print("Нет сохраненных заметок")
        