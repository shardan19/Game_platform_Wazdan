import threading
import time
import config
import mysql.connector

class DataRefresher:
    def __init__(self):
        self.connection = self.connect_to_database()
        self.data=None

        self.refresh_thread = threading.Thread(target=self.refresh_data)
        self.refresh_thread.daemon = True


    def start(self):
        self.refresh_thread.start()
    


    def refresh_data(self):
        while True:
            print("Refreshing data...")
            try:
                cursor=self.connection.cursor()
                select="SELECT * FROM "+config.DB_NAME+"."+config.TABLE_NAME
                print(select)
                cursor.execute(select)
                columns = [column[0] for column in cursor.description]
                rows = cursor.fetchall()
                data = {row[0]: {columns[i]: row[i] for i in range(1, len(columns))} for row in rows}
                print("Fetched data:",data)
                self.data=data
                cursor.close()
            except mysql.connector.Error as error:
                print("MySQL database fetc Error:", error)
            
            time.sleep(config.REFRESH_INTERVAL)

            self.connection.close()
            self.connection = self.connect_to_database()
    
    def connect_to_database(self):
        try:
            connection = mysql.connector.connect(
                host=config.DB_HOST,
                user=config.DB_USER,
                password=config.DB_PASSWORD,
                database=config.DB_NAME
            )
            if connection.is_connected():
                print("Connected to MySQL database")
                return connection
            else:
                print("Failed to connect to MySQL database")
                return None
            
        except mysql.connector.Error as error:
            print("Error connecting to MySQL database:", error)
            return None
