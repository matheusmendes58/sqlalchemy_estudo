from sqlalchemy import update
from banco import user_table, engine

connect = engine.connect()


update = update(user_table).where(user_table.c.nome == 'math')
update = update.values(nome='Matheus')

result = connect.execute(update)

print(result.rowcount)


