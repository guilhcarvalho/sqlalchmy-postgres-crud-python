from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy.exc import IntegrityError


Base = declarative_base()
_engine = create_engine(
    'postgresql+psycopg2://'
    'postgres:admin@'
    'localhost:5432/'
    'cadastros_postgresql'
) #Faz a conexão com o banco de dados postgreSQL


class Registrations(Base): #Cria a tabela 'clients' no banco de dados
    __tablename__ = 'clients'
    id = Column(Integer, primary_key=True)
    name = Column(String, unique=True)
    cpf = Column(String, unique=True)

    def _repr__(self):
        return f'<{self.id}> <{self.name}> <{self.cpf}>'


Base.metadata.create_all(_engine)
_Session = sessionmaker(bind=_engine)


class Crud():
    def __init__(self, _Session):
        self._Session = _Session

    def create(self):
        '''Cria novos registros no banco de dados'''
        name = input('Name: ')
        cpf = input('CPF: ')
        if len(cpf) == 11 and cpf.isdigit():
            try:
                with _Session() as session:
                    data = Registrations(name=name, cpf=cpf)
                    session.add(data)
                    session.commit()
                    print('Successfull')
            except IntegrityError as e:
                session.rollback()
                print(f'Dados já cadastrados: {e}')
        else:
            print('Invalid CPF')

    def read_one(self):
        '''Busca um registro especifico, optando por ID, Nome ou CPF'''
        try:
            busca = input('Query by: [1]ID, [2]Name or [3]CPF: ')
            if busca == '1': #Realiza a busca através do ID digitado
                query_id = int(input('ID: '))
                try:
                    with _Session() as session:
                        data = session.query(Registrations).filter_by(id=query_id).first()
                        print(f'> ID: {data.id} // Name: {data.name} // CPF: '
                              f'{data.cpf[:3]}.{data.cpf[3:6]}.{data.cpf[6:9]}-{data.cpf[9:]}')
                except Exception:
                    print('ID não encontrado')
            elif busca == '2': #Realiza a busca através do Nome digitado
                query_name = input('Name: ')
                try:
                    with _Session() as session:
                        data = session.query(Registrations).filter_by(name=query_name).first()
                        print(f'> ID: {data.id} // Name: {data.name} // CPF: '
                              f'{data.cpf[:3]}.{data.cpf[3:6]}.{data.cpf[6:9]}-{data.cpf[9:]}')
                except Exception:
                    print('Nome não encontrado.')
            elif busca == '3': #Realiza a busca através do CPF digitado
                query_cpf = input('CPF: ')
                try:
                    with _Session() as session:
                        data = session.query(Registrations).filter_by(cpf=query_cpf).first()
                        print(f'> ID: {data.id} // Name: {data.name} // CPF: '
                              f'{data.cpf[:3]}.{data.cpf[3:6]}.{data.cpf[6:9]}-{data.cpf[9:]}')
                except Exception:
                    print('CPF não encontrado.')
            else:
                print('Select a correct option.')
        except ValueError as e:
            print(f'Input a valid value: Erro {e}')

    def read_all(self):
        '''Busca todos os registros no banco de dados'''
        try:
            with _Session() as session:
                data = session.query(Registrations).all()
                for clients in data:
                    print(f'> ID: {clients.id} // Name: {clients.name} // CPF: '
                          f'{clients.cpf[:3]}.{clients.cpf[3:6]}.{clients.cpf[6:9]}-{clients.cpf[9:]}')
        except Exception as e:
            print(f'Erro {e}')
            return None

    def update_data(self):
        '''Atualiza name, cpf de um registro  pelo id no banco de dados'''
        try:
            id = input('ID: ')
            name = input('New name: ')
            cpf = input('New cpf: ')
            with _Session() as session:
                data = session.query(Registrations).filter_by(id=id).first()
                data.name = name
                data.cpf = cpf
                session.commit()
                print('Successfull')
                
        except Exception as e:
            print(f'Erro: {e}')
            return None

    def delete_data(self):
        '''Deleta um registro especifico informado pelo id no banco de dados'''
        try:
            id = input('ID: ')
            with _Session() as session:
                data = session.query(Registrations).filter_by(id=id).first()
                session.delete(data)
                session.commit()
                print('Successfull')
        except Exception as e:
            print(f'Erro {e}')
            return None