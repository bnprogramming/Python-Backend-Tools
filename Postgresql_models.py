import peewee

import Postgresql_configuration_settings
import Postgresql_database_manager

dbm = Postgresql_database_manager.DatabaseManager(
    database_name=Postgresql_configuration_settings.DATABASE['database_name'],
    user=Postgresql_configuration_settings.DATABASE['username'],
    password=Postgresql_configuration_settings.DATABASE['password'],
    host=Postgresql_configuration_settings.DATABASE['host'],
    port=Postgresql_configuration_settings.DATABASE['port']
)


class Product(peewee.Model):
    product_name = peewee.CharField(max_length=50, verbose_name='ProductName', null=False)
    brand = peewee.CharField(max_length=50, verbose_name='Brand', null=False)
    base_price = peewee.IntegerField(verbose_name='BasePrice', null=False)

    def __str__(self):
        return self.product_name

    class Meta:
        database = dbm.database_connection


class Customer(peewee.Model):
    first_name = peewee.CharField(max_length=30, verbose_name='First Name', null=False)
    last_name = peewee.CharField(max_length=30, verbose_name='Last Name', null=False)
    phone_number = peewee.CharField(max_length=30, verbose_name='Phone Number', null=False)

    def __str__(self):
        return f'{self.first_name} - {self.last_name} - {self.phone_number}'

    class Meta:
        database = dbm.database_connection


class Order(peewee.Model):
    customer = peewee.ForeignKeyField(Customer, verbose_name='Customer', null=False)
    product = peewee.ForeignKeyField(Product, verbose_name='Product', null=False)
    year = peewee.IntegerField(verbose_name='Year', null=False)
    month = peewee.IntegerField(verbose_name='Month', null=False)
    day = peewee.IntegerField(verbose_name='Day', null=False)
    quantity = peewee.FloatField(verbose_name='Quantity', null=False)
    final_price = peewee.FloatField(verbose_name='FinalPrice', null=False)

    def __str__(self):
        return f'{self.customer} - {self.product} - {self.final_price}'

    class Meta:
        database = dbm.database_connection
