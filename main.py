import psycopg2
from psycopg2.sql import SQL, Identifier

# Функция, создающая структуру БД (таблицы).
def create_db(conn):
    with conn.cursor() as cur:
        cur.execute("""
        CREATE TABLE IF NOT EXISTS clients(
        id SERIAL PRIMARY KEY,
        name VARCHAR(60) NOT NULL,
        surname VARCHAR(60) NOT NULL,
        email VARCHAR(60) NOT NULL
        );
        """)
        cur.execute("""
        CREATE TABLE IF NOT EXISTS telephones(
        telephone VARCHAR(60),
        client_id INTEGER NOT NULL REFERENCES clients(id)
        );
        """)
    conn.commit()

# Функция, позволяющая добавить нового клиента.
def add_client(conn, first_name, last_name, email, phones=None):
    with conn.cursor() as cur:
        cur.execute("""
        INSERT INTO clients(name,surname,email) VALUES (%s,%s,%s);
        """,(first_name, last_name, email))
    conn.commit()

# Функция, позволяющая добавить телефон для существующего клиента.
def add_phone(conn, client_id, phone):
    with conn.cursor() as cur:
        cur.execute("""
        INSERT INTO telephones(client_id,telephone) VALUES (%s,%s);
        """,(client_id,phone))
    conn.commit()

# Функция, позволяющая изменить данные о клиенте.
# замена для всех полей
def change_client2(conn, client_id, first_name=None, last_name=None, email=None):
    with conn.cursor() as cur:
        cur.execute("""
        UPDATE clients SET name =%s,surname =%s,email=%s WHERE id=%s;
        """,(first_name, last_name, email,client_id,))
    conn.commit()
# замена одного или несколько полей
def change_client(conn, client_id, name=None, surname=None, email=None):
    with conn.cursor() as cur:
        arg_list = {'name': name, "surname": surname, 'email': email}
        for key, arg in arg_list.items():
            if arg:
                cur.execute(SQL("UPDATE clients SET {}=%s WHERE id=%s").format(Identifier(key)), (arg, client_id))
        cur.execute("""
            SELECT * FROM clients
            WHERE id=%s
            """, client_id)
        return cur.fetchall()



# Функция, позволяющая удалить телефон для существующего клиента.
def delete_phone(conn, client_id):
    with conn.cursor() as cur:
        cur.execute("""
           DELETE FROM telephones WHERE client_id=%s;
           """, (client_id))
    conn.commit()

# Функция, позволяющая удалить существующего клиента.
def delete_client(conn, client_id):
    with conn.cursor() as cur:
        cur.execute("""
        DELETE FROM clients WHERE id=%s;
        """,(client_id,))
    conn.commit()

# Функция, позволяющая найти клиента по его данным: имени, фамилии, email или телефону.
def find_client(conn, searchword):
    with conn.cursor() as cur:
        cur.execute("""
        SELECT * FROM clients
        JOIN telephones ON client_id = id
        WHERE name =%s OR surname =%s OR email =%s OR telephone =%s
        """,(searchword,searchword,searchword,searchword,))
        return cur.fetchall()
    conn.commit()


with psycopg2.connect(database="homework_db",user="postgres",password="12345") as conn:
    # вызывайте функции здесь
    #create_db(conn)
    #add_client(conn, 'Alex', 'Ivanov', 'alex.ivanov@test.ru')
    #add_client(conn, 'Ivan', 'Pavlov', 'ivan.pavlov@test.ru')
    #add_client(conn, 'Olga', 'Somova', 'olga.somova@test.ru')
    # add_phone(conn, '1', '+79215555555')
    # add_phone(conn, '2', '+79215555556')
    # add_phone(conn, '3', '+79215555558')
    # delete_phone(conn, '1')
    # delete_client(conn, '1')
    # change_client2(conn, '3','Anna','Somova','anna.somova@test.ru')
    print(change_client(conn, '3','Olga',email='olga.somova@test.ru'))
    print(find_client(conn,'Olga'))

conn.close()