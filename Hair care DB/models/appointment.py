from peewee import (Model, CharField, SqliteDatabase,IntegerField, IntegrityError,TextField,DateTimeField)
import datetime

import config
DATABASE= config.DATABASE


class Appointment(Model):
    user_id=IntegerField()
    time_appointment=DateTimeField(default=datetime.datetime.now)
    salon_id = IntegerField()
    services = TextField()

    class Meta:
        database = DATABASE