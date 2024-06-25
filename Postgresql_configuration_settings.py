""" This dictionary is responsible for setting configuration of Postgresql database :
    - *dbname*: the database name
    - *database*: the database name (only as keyword argument)
    - *user*: username used to authenticate
    - *password*: password used to authenticate
    - *host*: database host address (defaults to UNIX socket if not provided)
    - *port*: connection port number (defaults to 5432 if not provided)
    so , we set the database configurations by using this dictionary indirectly """

# Connect to the PostgresSQL database
DATABASE = {
    'host': "host_name",
    'database_name': "db_name",
    'port': "db_portnumber",
    'username': "db_username",
    'password': "db_password",
}


