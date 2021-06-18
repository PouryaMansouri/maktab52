from psycopg2 import connect
from psycopg2._psycopg import connection, cursor

from setting import DB_CONFIG

config_line = " ".join(map(lambda i: f"{i[0]}='{i[1]}'", DB_CONFIG.items()))
conn: connection = connect(config_line)
print(conn)
curs: cursor = conn.cursor()
# information:
user_national_code = '1080055524'
test_name = 'blood test'

# TODO: query to get user_id and test_id
get_user_id_query = f"SELECT * FROM person where national_code='{user_national_code}';"
get_test_id_query = f"SELECT * FROM test where name='{test_name}';"
curs.execute(get_user_id_query)
# conn.commit()
user_id = curs.fetchall()
curs.execute(get_test_id_query)
# conn.commit()
test_id = curs.fetchall()

# TODO: get max test_answer id
get_max_test_answer_id = f"SELECT max(id) FROM test_answer;"
curs.execute(get_max_test_answer_id)
# conn.commit()
max_id = curs.fetchall()[0][0]

# TODO: query to add new row for test_answer
add_new_test_answer_query = f"INSERT INTO test_answer (id,person_id,request_date,answer_date) VALUES ({max_id + 1},{user_id[0][0]},'2020-03-12','2020-03-20') RETURNING id;"
curs.execute(add_new_test_answer_query)
conn.commit()
test_answer_id = curs.fetchall()
# TODO: query to ger test_pride id for test
get_test_price_id_query = f"SELECT * FROM test_price where test_id ='{test_id[0][0]}';"
curs.execute(get_test_price_id_query)
# conn.commit()
test_price_ = curs.fetchall()

# TODO: get max test_answer_list id
get_max_test_answer_list_id = f"SELECT max(id) FROM test_answer_list;"
curs.execute(get_max_test_answer_list_id)
# conn.commit()
max_id = curs.fetchall()[0][0]

# TODO: query to add new row for test_answer_list
add_new_test_answer_list_query = f"INSERT INTO test_answer_list (id,test_id,price,test_answer_id) VALUES ({max_id + 1},{test_id[0][0]},{test_price_[0][2]},{test_answer_id[0][0]}) RETURNING id;"
curs.execute(add_new_test_answer_list_query)
res = curs.fetchall()
conn.commit()
conn.close()
print("user_id ", user_id[0][0])
print("test_id=", test_id[0][0])
print("test_answer_id=", test_answer_id[0][0])
print("test_price=", test_price_[0][2])
print(res)

