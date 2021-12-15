import pandas as pd
import mysql.connector as mysql


# lendo arquivo csv e trantando linhas duplicadas e substituindo NaN
empdata = pd.read_csv(r'FILE PATH', index_col=False, delimiter=';')
empdata.drop_duplicates()
empdata['proposal'].fillna('default', inplace=True)
empdata['status_netsales'].fillna('default', inplace=True)
empdata['last_comment_mind'].fillna('default', inplace=True)
empdata['last_company_mind'].fillna('deafult', inplace=True)
empdata['obs'].fillna('default', inplace=True)

#empdata = empdata.isnull().sum() # verifica quantos NaN possui o dataframe em cada coluna
print(empdata)

'''
# criando banco
try:
    conn = mysql.connect(host='localhost', user='root', password='12345')

    if conn.is_connected():
        cursor = conn.cursor()
        cursor.execute("CREATE DATABASE csv")
        print('database is created')
except:
    print('error connection')
'''

#criando tabelas
conn = mysql.connect(host='localhost', database='csv', user='root', password='12345')
if conn.is_connected():
        cursor = conn.cursor()
        cursor.execute("select database();")
        record = cursor.fetchone()
        print("You're connected to database: ", record)
        #cursor.execute('DROP TABLE IF EXISTS 002_bko;')
        #print('Creating table....')
        '''
        cursor.execute("CREATE TABLE 002_bko(created varchar(500),"
                       "updated varchar(500),"
                       "id varchar(500),"
                       "proposal varchar(500),"
                       "state varchar(2),"
                       "city varchar(500),"
                       "status varchar(500),"
                       "status_mind varchar(500),"
                       "status_netsales varchar(500),"
                       "current_step varchar(500),"
                       "reason_mind varchar(500),"
                       "reason_mind_cancel varchar(500),"
                       "last_comment_mind text(1000),"
                       "last_company_mind varchar(500),"
                       "order_created varchar(500),"
                       "order_mind_last_updated varchar(500),"
                       "number_order varchar(500),"
                       "obs varchar(500),"
                       "attempts varchar(500),"
                       "user_robot_mind varchar(500),"
                       "user_robot_net_sales varchar(500),"
                       "num_robot varchar(500),"
                       "squad varchar(500),"
                       "syystem varchar(500));")
        print('table created')
        '''

# insert no banco
for i, row in empdata.iterrows():
                    sql = "INSERT INTO 002_bko(created, updated, id, proposal, state, city, status, status_mind," \
                          "status_netsales, current_step, reason_mind, reason_mind_cancel, last_comment_mind, last_company_mind," \
                          "order_created, order_mind_last_updated, number_order, obs, attempts, user_robot_mind, user_robot_net_sales, num_robot, squad, syystem) " \
                          "VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s);"
                    cursor.execute(sql, tuple(row))
                    print("Record inserted")
                    conn.commit()


