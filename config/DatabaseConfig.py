import psycopg2


class DatabaseConfig:

    __connection = None

    @staticmethod
    def initializeConnection():
        DatabaseConfig.__connection = psycopg2.connect(
            database="TASKTRACKER", user="postgres", password="Infy123+")

    @staticmethod
    def getConnection():
        return DatabaseConfig.__connection

    @staticmethod
    def endConnection():
        if (DatabaseConfig.__connection):
            DatabaseConfig.__connection.close()
