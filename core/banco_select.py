from sqlalchemy import select
from banco import user_table

mostrar_dados = select([user_table])

for row in mostrar_dados.execute():
    print(row)