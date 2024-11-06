import os
import pymysql

def check_db_connection():
    db_host = os.environ.get('DB_HOST', '127.0.0.1')
    db_user = os.environ.get('DB_USER', 'root')
    db_password = os.environ.get('DB_PASSWORD', 'test')
    db_name = os.environ.get('DB_NAME', 'test')

    try:
        connection = pymysql.connect(
            host=db_host,
            user=db_user,
            password=db_password,
            database=db_name,
            cursorclass=pymysql.cursors.DictCursor
        )
        connection.close()
        return True
    except Exception as e:
        print("Failed to connect to database:", str(e))
        return False

if __name__ == '__main__':
    if check_db_connection():
        exit(0)
    else:
        exit(1)