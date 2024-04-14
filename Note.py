from datetime import date
import datetime

from counter import counter

class Note:

    def __init__ (self, id, title, body, creation_date):
        id = str(counter.counter())
        self.id = id
        self.title = title
        self.body = body
        self.date = date
    
    #Геттеры#

    def get_id(note):
        return note.id

    def get_title(note):
        return note.title

    def get_body(note):
        return note.body

    def get_date(note):
        return note.date
    
    #Сеттеры#

    def set_id(note, id):
        note.id = id=str(counter.counter())

    def set_title(note, title):
        note.title = title

    def set_body(note, body):
        note.body = body

    def set_date(note):
        note.date = str(datetime.now().strftime("%d.%m.%Y %H:%M:%S"))

    def to_string(note):
        return note.id + ';' + note.title + ';' + note.body + ';' + note.date

    def map_note(note):
        return '\nID: ' + note.id + '\n' + 'Заголовок: ' + note.title + '\n' + 'Текст: ' + note.body + '\n' + 'Дата создания: ' + note.date
