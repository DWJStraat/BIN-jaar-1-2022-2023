import mariadb

class Db_Wrapper():
    def __init__(self, host, database, user, password, port = 3306):
        self.host = host
        self.database = database
        self.user = user
        self.password = password
        self.port = port
        self.connection = None
        self.cursor = None

    def connect(self):
        self.connection = mariadb.connect(
            host=self.host,
            user=self.user,
            password=self.password,
            database=self.database,
            port=self.port
        )

    def disconnect(self):
        self.connection.close()

    def getCursor(self):
        self.cursor = self.connection.cursor()

    def closeCursor(self):
        self.cursor.close()

    def commit(self):
        self.connection.commit()

    def open(self):
        self.connect()
        self.getCursor()

    def close(self, commit = False):
        if commit:
            self.commit()
        self.closeCursor()
        self.disconnect()

    def execute (self, query, commit = False):
        self.open()
        try:
            self.cursor.execute(query)
            if commit:
                self.commit()
            try:
                value = self.cursor.fetchall()
            except mariadb.ProgrammingError:
                value = None
            self.close()
        except mariadb.Error as e:
            print(f"Error: {e}\nQuery: {query}")
            raise e
        return value
