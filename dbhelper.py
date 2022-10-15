import mariadb
import dbcreds

# attempts to connect to the db using cursor conn and creation when done it will return the cursor
# if and error occurs it will show a corresponding error
def connect_db():
    try:
        conn = mariadb.connect(user=dbcreds.user, password=dbcreds.password,
        host=dbcreds.host, port=dbcreds.port, database=dbcreds.database)
        cursor = conn.cursor()
        return cursor
    except mariadb.OperationalError as error:
        print("operational error", error)
    except Exception as error:
        print("unknown error", error)


# attempt to close the conn to DB, gets conn assoicated w/ the cursor then closes cursor and conn
def close_connect(cursor):
    try:
        conn = cursor.connection
        cursor.close()
        conn.close()
    except mariadb.OperationalError as error:
        print('operational error', error)
    except mariadb.InternalError as error:
        print('internal error', error)
    except Exception as error:
        print('unknown error', error)

# returns an error based on what kind of error it is if the execute statment doesn't work
# if and error occurs it will show a corresponding error
def execute_statment(cursor, statement, list_of_args=[]): 
    try:
        cursor.execute(statement, list_of_args)
        results = cursor.fetchall()
        return results
    except mariadb.ProgrammingError as error:
        print('programming error', error)
        return str(error)
    except mariadb.IntegrityError as error:
        print('integrity error', error)
        return str(error)
    except mariadb.DataError as error:
        print('data error', error)
        return str(error)
    except Exception as error:
        print('unknown error', error)
        return str(error)


#returns a list of tuples if it connects if it fails it will return a string "conntection error"
def run_statment(statment, list_of_args=[]):
    cursor = connect_db()
    if(cursor == None):
        return "conntection error"
    results = execute_statment(cursor, statment, list_of_args)
    close_connect(cursor)
    return results