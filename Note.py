from datetime import date
import datetime

class Note:

    def __init__ (self, id, title, body, creation_date):
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
        note.id = id

    def set_title(note, title):
        note.title = title

    def set_body(note, body):
        note.body = body

    def set_date(note):
        note.date = str(datetime.now().strftime("%d.%m.%Y %H:%M:%S"))
