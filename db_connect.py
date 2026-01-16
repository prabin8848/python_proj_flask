import mariadb
db_config ={
    'host': 'localhost',
    'port': 3306,
    'user' :'test1',
    'password': 'pascal1',
    'database': 'broadwaydb'

}

def get_connection():
    try: 
        conn = mariadb.connect(**db_config)
        return conn
    except Exception as e:
        print(f"unable to connect to database.{e}") 
     