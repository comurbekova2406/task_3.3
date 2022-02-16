import psycopg2
conn = psycopg2.connect(dbname='titanic', user='postgres', password='401901')
cur = conn.cursor()
# cur.execute("""CREATE TABLE passengers
# ( id integer, survived integer, class integer, name text, sex varchar(50),
# age varchar(50), sibsp integer, parch integer, ticket varchar(255),
# fare numeric NULL, cabin varchar(255) NULL, embarked varchar(50) ) """)
# with open(r'titanic.txt', 'r') as f: next(f) cur.copy_from(f, 'passengers', sep='|')
#     conn.commit()

# начало вашего кода
# 1
cur.execute("select name from passengers where survived=0")
record = cur.fetchall()
print("Результат", record)
# 2
cur.execute("SELECT COUNT(*) *100 FROM passengers WHERE survived=1"
            "SELECT COUNT(*) FROM passengers WHERE sex='female',class=1)
record = cur.fetchall()

