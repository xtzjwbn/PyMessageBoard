import sqlite3

conn = sqlite3.connect('../DataBase/MessageBoardDB.sqlite')
cs = conn.cursor()
# create_tb_sql = '''
# CREATE TABLE USER(
#    UUID TEXT  PRIMARY KEY     NOT NULL,
#    NAME           TEXT    NOT NULL,
#    PASSWORD       TEXT     NOT NULL,
#    NICKNAME       TEXT     NOT NULL
# );'''
# cs.execute(create_tb_sql)
# cs.execute('insert into USER values(?,?,?,?);', ('uuid', 'Tom', 'password', 'nickname'))
# conn.commit()
cs.execute('select * from USER where UUID = "UUID"')
result = cs.fetchall()
print(result[0][0])
conn.close()
