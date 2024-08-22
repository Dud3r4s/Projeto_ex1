import mysql.connector

#FAZ A CONEXÃO DO BANCO DE DADOS COM O PYTHON
comanda_bd = mysql.connector.connect(
    host='127.0.0.1',
    user='root',
    password='',
    database='comanda_bar'
)

# FAZ UMA CONEXÃO PARA MANIPULAR OS DADOS 
cursor = comanda_bd.cursor()

cursor.execute("SELECT * FROM cliente") # Nome da tabela no mysql

m = cursor.fetchall()

print(m)


