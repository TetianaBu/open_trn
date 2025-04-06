import pyodbc
import os

def get_db_connection():
    # Get database credentials from environment variables
    server = os.getenv('DB_SERVER')    # Database server
    uid = os.getenv('DB_USER')          # Database username
    pwd = os.getenv('DB_PASSWORD')          # Database password

    conn = pyodbc.connect(
        f'DRIVER={{ODBC Driver 17 for SQL Server}};'
        f'SERVER={server};'
        f'DATABASE=TRN;'
        f'UID={uid};'
        f'PWD={pwd}'
    )
    return conn

print(get_db_connection())
get_db_connection()
