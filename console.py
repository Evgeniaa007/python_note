import Menu
from commands import Commands as com

""" Метод вызова из меню команд"""
def start():
    flag = True
    while flag:
        Menu.Menu.menu_console()
        user_input = input('Выберите действие: ')
        
        if user_input == '0': # выход
            print('Приложение "заметки" завершило работу')
            flag = False

        elif user_input == '1': # вывод журнала
                com.show_note("all")           
        
        elif user_input == '2': # вывод заметки по id
            com.show_note('ID')                 

        elif user_input == '3': # выбор заметки по дате
            com.show_note('date')               

        elif user_input == '4': # редактирование заметки
            com.show_note('all')                
            com.edit_note()               

        elif user_input == '5': # добавление заметки
            com.add_note()                  
        
        elif user_input == '6': # удаление заметки
            com.show_note('all')                
            com.del_note()                

        else:
            print('Такого действия не существует')
            return