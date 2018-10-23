from models.user import User
from models.saloon import Saloon
from models.appointment import Appointment
from peewee import SqliteDatabase, IntegrityError
import datetime
import config

DATABASE = config.DATABASE


def initialize():
    DATABASE.create_tables([User, Saloon, Appointment], safe=True)
    try:
        User.create(
            first_name="Felician",
            last_name="Mueni",
            email="john@doe.com",
            
        )
    except IntegrityError:
        pass
    try:
        Saloon.create(
              name = "mrembo",
              business_number = "9887",
              opening_time = "10:00am",
              closing_time = "5:00pm",
              description = "urembo services",
              services = "manicure,pedicure,haircare",
              user_id = 1,
              location = "george pandmore lane"
        )
    except IntegrityError:
        pass
    try:
        Appointment.create(
                  user_id=1,
                  salon_id = 1,
                  services ="haircare,manicure,facial",
                  time_appointment=datetime.datetime.now()
        )
    except IntegrityError:
        pass
    DATABASE.close()