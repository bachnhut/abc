from peewee import *

user = 'root'
password = 'bachnhut'
db_name = 'fastapi_contact'

conn = MySQLDatabase(
    db_name, user=user,
    password=password,
    host='localhost'
)

# def get_connection():
#     return conn