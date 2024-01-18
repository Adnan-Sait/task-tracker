import yaml
import psycopg2


def initializeConnection():
    """
    Initializes and returns the database connection.
    """
    database = None
    user = None
    password = None

    with open('./resources/config.yml') as configFile:
        configurationValues = yaml.load(configFile, Loader=yaml.BaseLoader)

        database = configurationValues["dbConnectionDetails"]["database"]
        user = configurationValues["dbConnectionDetails"]["user"]
        password = configurationValues["dbConnectionDetails"]["password"]

    if (database and user and password):
        return psycopg2.connect(
            database=database, user=user, password=password)
    else:
        raise Exception(
            f"One or more required config values are missing. Database connection could not be established.")


class DatabaseConfig:

    __connection = initializeConnection()

    @staticmethod
    def getConnection():
        return DatabaseConfig.__connection

    @staticmethod
    def endConnection():
        if (DatabaseConfig.__connection):
            DatabaseConfig.__connection.close()
