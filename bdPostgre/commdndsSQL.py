import psycopg2
# from config import host, user, password, database



try:
    # connect to exist database
    connection = psycopg2.connect(
    host="localhost",
    database="kng",
    user="postgres",
    password="Ggwpawp2003"  
    )
    connection.autocommit = True
    
    # the cursor for perfoming database operations
    # cursor = connection.cursor()
    # with connection.cursor() as cursor:
    #     cursor.execute('''CREATE TABLE table_name (
    # id SERIAL PRIMARY KEY,
    # login TEXT NOT NULL
    # );

    # ''')
    with connection.cursor() as cursor:
        cursor.execute(
            "SELECT version();"
        )
        
        print(f"Server version: {cursor.fetchone()}")
        

    
    # with connection.cursor() as cursor:
    #     cursor.execute(
    #         "INSERT INTO table_name (login) VALUES ('kng5')"
    #         )
    #     print("insert")

    # with connection.cursor() as cursor:
    #     table,argument,ctho = 'table_name','login','kng5'
    #     cursor.execute(
    #         f"DELETE from {table} WHERE {argument} = '{ctho}'"
    #     )
    # #     cursor.execute(
    # #         f"ALTER SEQUENCE {table}_id_seq RESTART WITH 1"
    # #     )
    #     print(f"Deleted from {table}, where {argument} = {ctho}")
    #     print("Identity sequence reset")


    with connection.cursor() as cursor:
        table = 'table_name'
        cursor.execute(f"DELETE FROM {table}")
        cursor.execute(f"ALTER SEQUENCE {table}_id_seq RESTART WITH 1")
        print(f"All rows deleted from {table} and id reset to 1")



    with connection.cursor() as cursor:
        cursor.execute(
            "SELECT * FROM table_name"
        )
        result = cursor.fetchall()
        print(result,sep='\n'),print('its all dataset')

except Exception as _ex:
    print("[INFO] Error while working with PostgreSQL", _ex)
finally:
    if connection:
        # cursor.close()
        connection.close()
        print("[INFO] PostgreSQL connection closed")