import counter as counter

from datetime import datetime


'''Класс заметки'''
class Note:

    '''Конструктор класса'''
    def __init__(self, id = str(counter.counter()), title = "текст", body = "текст", 
                 creation_date = str(datetime.now().strftime("%d.%m.%Y %H:%M:%S"))):
        self.id = id # Индентификатор
        self.title = title # Заголовок
        self.body = body # Тело заметки
        self.creaton_date = creation_date # Дата/время создания или последнего изменения
    
    '''Геттеры'''
    def get_id(note):
        return note.id
    
    def get_title(note):
        return note.title
    
    def get_body(note):
        return note.body
    
    def get_creation_date(note):
        return note.creaton_date
    
    '''Сеттеры'''
    def set_id(note):
        note.id = str(counter.counter())

    def set_title(note):
        note.title = note

    def set_body(note):
        note.body = note

    def set_date(note):
        note.creaton_date = str(datetime.now().strftime("%d.%m.%Y %H:%M:%S"))

    def to_string(note):
        return note.id + ';' + note.title + ';' + note.body + ';' + note.creaton_date
    

    def show_note(note):
        return '\nID: ' + note.id + '\n' + 'Название: ' + note.title + '\n'         \
        + 'Описание: ' + note.body + '\n' + 'Дата публикации: ' + note.creaton_date
    