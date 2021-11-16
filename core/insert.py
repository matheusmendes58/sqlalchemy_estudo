from banco import engine, user_table

connect = engine.connect()

insert = user_table.insert()

novo_usuario = insert.values(nome='fabio',
                             idade=30,
                             senha='123456')

connect.execute(novo_usuario)

connect.execute(user_table.insert(), [
    {'nome': 'marivaldo', 'idade': 30, 'senha': 'sdkjfhs'},
    {'nome': 'robertp', 'idade': 10, 'senha': 'sakjfhskvbk'},
    {'nome': 'nav', 'idade': 40, 'senha': 'asfkjbfdbkn'},
    {'nome': 'math', 'idade': 27, 'senha': 'bsdbfqb'}
])