import psycopg2


def initializeConnection():
    """
    Initializes and returns the database connection.
    """
    return psycopg2.connect(
        database="TASKTRACKER", user="postgres", password="Infy123+")


class DatabaseConfig:

    __connection = initializeConnection()

    @staticmethod
    def getConnection():
        return DatabaseConfig.__connection

    @staticmethod
    def endConnection():
        if (DatabaseConfig.__connection):
            DatabaseConfig.__connection.close()
