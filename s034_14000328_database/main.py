from psycopg2 import connect
from psycopg2._psycopg import connection, cursor

from setting import DB_CONFIG

config_line = " ".join(map(lambda i: f"{i[0]}='{i[1]}'", DB_CONFIG.items()))
conn: connection = connect(config_line)
print(conn)
curs: cursor = conn.cursor()
query = f"INSERT INTO test_answer (id,person_id,request_date,answer_date) VALUES (191,5,'2020-03-12','2020-03-20') RETURNING id;"
# query = f"UPDATE test_answer set person_id=5 where id=101"
# query = F"DELETE FROM test_answer where id=101 "
# query = "SELECT * FROM test_answer"
a = curs.execute(query)
b = conn.commit()
c = curs.fetchall()
conn.close()
print(a)
print(b)
print(c)