from sqlalchemy import create_engine, MetaData, Column, Table, INTEGER, String, DATETIME
import datetime


engine = create_engine('sqlite:///teste.db', echo=True) #Criação do banco de dados echo=True é para printar tudo o que está fazendo
metadados = MetaData(bind=engine)

# criando tabelas

user_table = Table('usuarios', metadados,
                   Column('id', INTEGER, primary_key=True),
                   Column('nome', String(40), index=True),
                   Column('idade', INTEGER, nullable=False),
                   Column('senha', String),
                   Column('criado_em', DATETIME, default=datetime.datetime.now()),
                   Column('atualizado_em', DATETIME, default=datetime.datetime.now(), onupdate=datetime.datetime.now()))

metadados.create_all()
