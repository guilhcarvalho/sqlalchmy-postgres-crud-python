from backend import Crud, _Session
import time
import os


def main():
    while True:
        print('=' * 50)
        print('\tCRUD SQLAlchmy ORM and PostgreSQL')
        print('[1]Register new client in database')
        print('[2]Query one client')
        print('[3]Show all clients')
        print('[4]Update client data')
        print('[5]Delete client data')
        print('=' * 50)
        menu = input('Select an option: ')
        backend_operation = Crud(_Session)
        if menu == '1':
            backend_operation.create()
            time.sleep(2)
            os.system('cls')
            continue
        elif menu == '2':
            backend_operation.read_one()
            time.sleep(2)
            os.system('cls')
            continue
        elif menu == '3':
            backend_operation.read_all()
            continue
        elif menu == '4':
            backend_operation.update_data()
            continue
        elif menu == '5':
            backend_operation.delete_data()
main()