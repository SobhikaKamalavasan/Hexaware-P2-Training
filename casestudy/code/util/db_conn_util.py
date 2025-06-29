
import mysql.connector
from util.db_property_util import DBPropertyUtil

class DBConnUtil:
    connection = None

    @staticmethod
    def get_connection():
        if DBConnUtil.connection is None:
            try:
                props = DBPropertyUtil.get_property_string()
                DBConnUtil.connection = mysql.connector.connect(
                    host=props["host"],
                    port=props["port"],
                    user=props["user"],
                    password=props["password"],
                    database=props["database"]
                )
                print("✅ Database connection established.")
            except mysql.connector.Error as err:
                print(f"❌ Database connection failed: {err}")
        return DBConnUtil.connection
