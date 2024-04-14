import Menu as menu
from commands import Commands as func

""" Метод вызова из меню команд"""
def start():
    flag = True
    while flag:
        menu.Menu.menu_console()
        user_input = input('Выберите пункт из меню: ')
        
        if user_input == '0': # выход
            print('Приложение "заметки" завершено')
            flag = False

        elif user_input == '1': # вывод журнала
            func.show('all')
        
        elif user_input == '2': # вывод заметки по id
            func.show('ID')
        
        elif user_input == '3': # выбор заметки по дате
            func.show('date')
        
        elif user_input == '4': # редактирование заметки
            func.show('all')
            func.change_note()
        
        elif user_input == '5': # добавление заметки
            func.add_note()
        
        elif user_input == '6': # удаление заметки
            func.show('all')
            func.del_notes()
              
        else:
            print('Такого действия нет!')
            #return