documents = [
    {"type": "passport", "number": "2207 876234", "name": "Василий Гупкин"},
    {"type": "invoice", "number": "11-2", "name": "Геннадий Покемонов"},
    {"type": "insurance", "number": "10006", "name": "Аристарх Павлов"}
]

directories = {
    '1': ['2207 876234', '11-2', '5455 028765'],
    '2': ['10006'],
    '3': []
}


def people(doc_n1):
    for item in documents:
        if item['number'] == doc_n1:
            return item['name']
    return 'Invalid number'


def shelf(doc_n2):
    for item in directories:
        if doc_n2 in directories[item]:
            return item
    return 'Invalid number'


def to_list():
    doc_list = []
    for doc in documents:
        doc_list.append(f"{doc['type']}, {doc['number']}, {doc['name']}")

    print(doc_list)
    return doc_list


def add(d_type, d_number, d_owner, shelf_n):
    if shelf_n not in directories:
        return 'Invalid shelf number'
    new_doc = dict(type=d_type, number=d_number, name=d_owner)
    documents.append(new_doc)
    directories[shelf_n] += [d_number]
    return 'Document added'


def command():
    print('''Команды: p - найти человека по документу
          s - найти полку с документом
          l - показать список документов
          a - добавить документ на полку
          q - выйти''')
    while True:
        user_input = input('Введите команду')
        if user_input == 'p':
            doc_n1 = input('Введите номер документа')
            print(people(doc_n1))
        elif user_input == 's':
            doc_n2 = input('Введите номер документа')
            print(shelf(doc_n2))
        elif user_input == 'l':
            to_list()
        elif user_input == 'a':
            shelf_n = input('Введите номер полки')
            d_type = input('Введите тип документа')
            d_number = input('Введите номер документа')
            d_owner = input('Введите имя обладателя документа')
            print(add(d_type, d_number, d_owner, shelf_n))
        elif user_input == 'q':
            break


#print(command(documents, directories))


if __name__ == '__main__':
    command()