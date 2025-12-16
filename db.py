import pymysql
import os
# ...

def get_connection():
    return pymysql.connect(
        host=os.environ.get('DB_HOST', 'shinkansen.proxy.rlwy.net'),  # << Lee la clave DB_HOST
        user=os.environ.get('DB_USER', 'root'),      # << Lee la clave DB_USER
        password=os.environ.get('DB_PASSWORD', 'jteoApphwrVEJklHMncvmwOweZhQLgsY'),  # << Lee la clave DB_PASSWORD
        database=os.environ.get('DB_NAME', 'activos'), # << Lee la clave DB_NAME
        # ...
    )
