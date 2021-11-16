from sqlalchemy import delete
from banco import user_table, engine

connect = engine.connect()

delete = delete(user_table).where(user_table.c.nome == 'nav')

result = connect.execute(delete)

print(result.rowcount)