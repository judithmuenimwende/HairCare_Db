from peewee import (Model, CharField, SqliteDatabase, IntegrityError, TextField)

import config
DATABASE= config.DATABASE


class User(Model):
    first_name = CharField(max_length=100)
    last_name = CharField(max_length=100)
    email = CharField(max_length=100, unique=True)
  

    class Meta:
        database = DATABASE
