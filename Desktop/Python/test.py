'''Создать телефонный справочник с возможностью импорта и экспорта данных в формате .txt.
Фамилия, имя, отчество, номер телефона - данные, которые должны находиться в файле.
1. Программа должна выводить данные
2. Программа должна сохранять данные в текстовом файле
3. Пользователь может ввести одну из характеристик для поиска определенной записи(Например имя или фамилию человека)
4. Использование функций. Ваша программа не должна быть линейной '''


def phone_book(phonebook):
    while True:
        print('Что вы хотите сделать?')
        user_choice = input("\n Выберите необходимое действие: \n"
          "1. Отобразить весь справочник \n"
          "2. Найти абонента \n"
          "3. Добавить абонента в справочник \n"
          "4. Изменить данные \n"
          "5. Сохранить справочник в текстовом формате \n"
          "6. Закончить работу \n")
        print()

        
        if user_choice == '1':
            file_to_add = input('Введите название импортируемого файла: ')
            import_data(file_to_add, phonebook)
        elif user_choice == '2':
            contact_list = read_file_to_dict(phonebook)
            find_number(contact_list)
        elif user_choice == '3':
            add_phone_number(phonebook)
        elif user_choice == '4':
            change_phone_number(phonebook)
        elif user_choice == '5':
            delete_contact(phonebook)
        elif user_choice == '6':
            show_phonebook(phonebook)
            break
        else:
            print('Неправильно выбрана команда!')
            continue


def import_data(file_to_add, phonebook):                 # ОТОБРАЗИТЬ ВЕСЬ СПРАВОЧНИК
    try:
        with open(file_to_add, 'r', encoding='utf-8') as new_contacts, open(phonebook, 'a', encoding='utf-8') as file:
            contacts_to_add = new_contacts.readlines()
            file.writelines(contacts_to_add)
    except FileNotFoundError:
        print(f'{file_to_add} не найден')


def read_file_to_dict(file_name):                           # НАЙТИ АБОНЕНТА
    with open(file_name, 'r', encoding='utf-8') as file:    # загружаем файл с помощью контекстного меню
        lines = file.readlines()
    headers = ['Фамилия', 'Имя', 'Номер телефона']
    contact_list = []                                       # создаем пустой список
    for line in lines:                                      # перебираем наш файл
        line = line.strip().split()
        contact_list.append(dict(zip(headers, line)))       
    return contact_list                                     # возвращаем список


def read_file_to_list(file_name):                          # ДОБАВИТЬ АБОНЕНТА В СПРАВОЧНИК
    with open(file_name, 'r', encoding='utf-8') as file:    # загружаем файл
        contact_list = []                                  # создали пустой список
        for line in file.readlines():                        # перебираем файл
            contact_list.append(line.split())               # записывем человеа в список
    return contact_list                                     # возвращаем список


def search_parameters():                                   
    print('По какому полю выполнить поиск?')
    search_field = input('1 - по фамилии\n 2 - по имени\n 3 - по номеру телефона\n')
    print()
    search_value = None
    if search_field == '1':
        search_value = input('Введите фамилию для поиска: ')
        print()
    elif search_field == '2':
        search_value = input('Введите имя для поиска: ')
        print()
    elif search_field == '3':
        search_value = input('Введите номер для поиска: ')
        print()
    return search_field, search_value


def find_number(contact_list):                           # СОХРАНИТЬ СПАВОЧНИК В ТЕКСТОВОМ ФОРМАТЕ
    search_field, search_value = search_parameters()
    search_value_dict = {'1': 'Фамилия', '2': 'Имя', '3': 'Номер телефона'}
    found_contacts = []
    for contact in contact_list:
        if contact[search_value_dict[search_field]] == search_value:
            found_contacts.append(contact)
    if len(found_contacts) == 0:
        print('Контакт не найден!')
    else:
        print_contacts(found_contacts)
    print()


def get_new_number():                                  # ДОБАВИТЬ АБОНЕНТА В СПРАВОЧНИК        
    last_name = input('Введите фамилию: ')
    first_name = input('Введите имя: ')
    phone_number = input('Введите номер телефона: ')
    return last_name, first_name, phone_number


def add_phone_number(file_name):                      
    info = ' '.join(get_new_number())
    with open(file_name, 'a', encoding='utf-8') as file:
        file.write(f'{info}\n')


def show_phonebook(file_name):                          # ЗАКОНЧИТЬ РАБОТУ
    list_of_contacts = sorted(read_file_to_dict(file_name), key=lambda x: x['Фамилия'])
    print_contacts(list_of_contacts)
    print()
    return list_of_contacts


def search_to_modify(contact_list: list):                      # НАЙТИ АБОНЕНТА
    search_field, search_value = search_parameters()
    search_result = []
    for contact in contact_list:
        if contact[int(search_field) - 1] == search_value:
            search_result.append(contact)
    if len(search_result) == 1:
        return search_result[0]
    elif len(search_result) > 1:
        print('Найдено несколько контактов')
        for i in range(len(search_result)):
            print(f'{i + 1} - {search_result[i]}')
        num_count = int(input('Выберите номер контакта, который нужно изменить/удалить: '))
        return search_result[num_count - 1]
    else:
        print('Контакт не найден')
    print()


def change_phone_number(file_name):                           # ИЗМЕНИТЬ ДАННЫЕ
    contact_list = read_file_to_list(file_name)
    number_to_change = search_to_modify(contact_list)
    contact_list.remove(number_to_change)
    print('Какое поле вы хотите изменить? ')
    field = input('1 - Фамилия\n 2 - Имя\n 3 - Номер телефона\n')
    if field == '1':
        number_to_change[0] = input('Введите фамилию: ')
    elif field == '2':
        number_to_change[1] = input('Введите имя: ')
    elif field == '3':
        number_to_change[2] = input('Введите номер телефона: ')
    contact_list.append(number_to_change)
    with open(file_name, 'w', encoding='utf-8') as file:
        for contact in contact_list:
            line = ' '.join(contact) + '\n'
            file.write(line)


def delete_contact(file_name):                      # СОХРАНИТЬ СПАВОЧНИК В ТЕКСТОВОМ ФОРМАТЕ
    contact_list = read_file_to_list(file_name)
    number_to_change = search_to_modify(contact_list)
    contact_list.remove(number_to_change)
    with open(file_name, 'w', encoding='utf-8') as file:
        for contact in contact_list:
            line = ' '.join(contact) + '\n'
            file.write(line)


def print_contacts(contact_list: list):
    for contact in contact_list:
        for key, value in contact.items():
            print(f'{key}: {value:12}', end='')
        print()


if __name__ == '__main__':
    file = 'Phonebook.txt'
    phone_book(file)
