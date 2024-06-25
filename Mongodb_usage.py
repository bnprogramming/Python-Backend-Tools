import random
from pymongo import MongoClient
import Mongodb_configuration_settings
from logger import logger


# create connection to database
client = MongoClient(host=Mongodb_configuration_settings.DATABASE['host'],
                     port=Mongodb_configuration_settings.DATABASE['port'])

# create database
mongo_db = client[Mongodb_configuration_settings.DATABASE['name']]

# create collection
collections = mongo_db.list_collection_names()
if 'contacts' in collections:
    contact_collection = mongo_db.get_collection('contacts')
else:
    contact_collection = mongo_db['contacts']

# Generate random data
first_names = ['John', 'Jane', 'David', 'Emma', 'Michael', 'Olivia']
last_names = ['Smith', 'Johnson', 'Williams', 'Brown', 'Jones', 'Garcia']

if __name__ == '__main__':
    for _ in range(100):
        first_name = random.choice(first_names)
        last_name = random.choice(last_names)

        entry = {
            'first_name': first_name,
            'last_name': last_name,
        }

        # Insert the entry into my MongoDB phonebook
        try:
            contact_collection.insert_one(entry)
            logger.info(entry, 1)
        except Exception as error:
            logger.error(entry, 1, error)

    logger.info('phonebook enteries are added successfully!.')
