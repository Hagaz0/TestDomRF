import cx_Oracle

ip = "10.95.23.432"
port = 777
service_name = "prod"
login = "akr"
password = "123"

dsn = cx_Oracle.makedsn(ip, port, service_name=service_name)

connection = cx_Oracle.connect(login, password, dsn)

cursor = connection.cursor()
cursor.execute("SELECT * FROM risk_management.clients WHERE ROWNUM <= 5")
rows = cursor.fetchall()

for row in rows:
    print(row)

cursor.close()
connection.close()