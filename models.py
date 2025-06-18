import psycopg2

class Modelo:
    def __init__(self):
        try:
            self.connection = psycopg2.connect(
                host="192.168.10.15",
                database="darek_db",
                user="postgres",
                password=""
            )
            self.cursor = self.connection.cursor()
        except Exception as e:
            print(str(e))

    def execute_query(self, query):
        self.cursor.execute(query)
        return self.cursor.fetchall()

    def close_connection(self):
        self.cursor.close()
        self.connection.close()
