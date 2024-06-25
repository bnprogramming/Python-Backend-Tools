import psycopg2
from peewee import PostgresqlDatabase
from logger import logger

class DatabaseManager:
    """This class is responsible for managing the database jobs :
    1- Creating(Set Configurations)
    2- connecting to the  created database
    3- disconnecting from the database
    4- apply and execute the SQL queries
    in python , each object of this class is a database , so we can use it and its methods."""

    def __init__(self, database_name, user, password, host, port):
        self.database_name = database_name
        self.user = user
        self.password = password
        self.host = host
        self.port = port
        # we want to establish the database automatically while declaration so we call connect_to_database() method
        self.database_connection = self.connect_to_database()

    def __str__(self):
        return self.database_name

    def connect_to_database(self):
        """
        Establishing the connection by OOP specifications
        """
        logger.info('Connecting to the database...')
        try:
            database_connection = PostgresqlDatabase(
                self.database_name,
                user=self.user,
                password=self.password,
                host=self.host,
                port=self.port
            )
            database_connection.connect()
            return database_connection

        except (Exception, psycopg2.Error) as stablishing_error:
            logger.info(f'Error while connecting to the database : {stablishing_error}')
            return None

    def close_connection(self):
        self.database_connection.close()
        logger.info(' Database closed ')

    def create_tables(self, models):
        for model in models:
            try:
                self.database_connection.create_tables([model])
                logger.info(f'Create table {model.__name__}  successful ')
            except Exception as error:
                logger.info(f'Create table {model.__name__}  unsuccessful :{error}')



