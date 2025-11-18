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
)


class Registrations(Base):
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
        with _Session() as session:
            try:
                data = Registrations(name=name, cpf=cpf)
                session.add(data)
                session.commit()
                print('Successfull')
            except IntegrityError as e:
                session.rollback()
                print(f'Dados já cadastrados: {e}')

    def read_one(self):
        '''Busca um registro especifico, optando por ID, Nome ou CPF'''
        try:
            busca = input('Query by: [1]ID, [2]Name or [3]CPF: ')
            if busca == '1':
                query_id = int(input('ID: '))
                try:
                    with _Session() as session:
                        data = session.query(Registrations).filter_by(id=query_id).first()
                        print(f'<ID: {data.id} // Name: {data.name} // CPF: {data.cpf}>')
                except ValueError as e:
                    print(f'Erro: {e}')
                    return None
            elif busca == '2':
                query_name = input('Name: ')
                try:
                    with _Session() as session:
                        data = session.query(Registrations).filter_by(name=query_name).first()
                        print(f'<ID: {data.id} // Name: {data.name} // CPF: {data.cpf}>')
                except Exception as e:
                    print(f'Erro: {e}')
                    return None
            elif busca == '3':
                query_cpf = input('CPF: ')
                try:
                    with _Session() as session:
                        data = session.query(Registrations).filter_by(cpf=query_cpf).first()
                        print(f'<ID: {data.id} // Name: {data.name} // CPF: {data.cpf}>')
                except Exception as e:
                    print(f'Erro: {e}')
                    return None
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
                    print(f'<ID: {clients.id} // Name: {clients.name} // CPF: {clients.cpf}>')
        except Exception as e:
            print(f'Erro {e}')
            return None

    def update_data(self):
        '''Atualiza name, cpf de um registro  pelo id no banco de dados'''
        try:
            id = input('ID: ')
            name = input('Name: ')
            cpf = input('cpf: ')
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
        id = input('ID: ')
        try:
            with _Session() as session:
                data = session.query(Registrations).filter_by(id=id).first()
                session.delete(data)
                session.commit()
                print('Successfull')
        except Exception as e:
            print(f'Erro {e}')
            return None
