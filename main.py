from backend import Crud, _Session
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
            os.system('cls')
            print('='*10+' '+'New client registration'+' '+'=' * 10)
            backend_operation.create()
            continue
        elif menu == '2':
            print('='*25+' '+'Client'+' '+'=' * 25)
            backend_operation.read_one()
            continue
        elif menu == '3':
            os.system('cls')
            print('='*25+' '+'Clients'+' '+'=' * 25)
            backend_operation.read_all()
            continue
        elif menu == '4':
            print('='*25+' '+'Update'+' '+'=' * 25)
            backend_operation.update_data()
            continue
        elif menu == '5':
            print('='*25+' '+'Delete'+' '+'=' * 25)
            backend_operation.delete_data()
main()