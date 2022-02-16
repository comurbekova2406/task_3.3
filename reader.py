import psycopg2


conn = psycopg2.connect(dbname='titanic', user='postgres', password='401901')
cur = conn.cursor()

cur.execute(
    """CREATE TABLE passengers( 
id int, survived int, 
class int,name text, sex varchar(50), age int, 
sibsp int, parch int, ticket varchar(255), fare numeric NULL, 
cabin varchar(255) NULL, embarked varchar(50) ) """)
with open(r'titanic.txt', 'r') as f:
    next(f)
    cur.copy_from(f, 'passengers', sep='|')
conn.commit()
# начало вашего кода
postgreSQL_select_Query = "select *names from passengers where survived=0"
record = cursor.fetchall()
print("Результат", record)

cur.close()
conn.close()
