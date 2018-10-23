from flask import (Flask, render_template, request, jsonify)
from models.saloon import Saloon
from peewee import IntegrityError
from models.user import User
from models.appointment import Appointment
from datetime import datetime
app_start_config = {'debug': True, 'port': 8080, 'host': '0.0.0.0'}
app = Flask(__name__)
import bootstrap
bootstrap.initialize()


@app.route('/')
def index():
    return "List of products"


@app.route('/user/register', methods=['POST'])
def register_user():
  user_data = dict(request.form.items())
  result = {}
  try:
      User.create(
          first_name=user_data.get('first_name'),
          last_name=user_data.get('last_name'),
          email=user_data.get('email')
          )
      result = {
        'status': 'success',
        'message':'{} is registered'.format(user_data.get('first_name'))}
      return jsonify(result)
  except IntegrityError:
    result = {
      'status':'failed',
      'message':'{} is not unique'.format(user_data.get('email'))}
  return jsonify(result)

@app.route('/user')
def list_users():
  users = User.select()
  results = []
  for user in users:
    results.append(
      {
        'first_name':user.first_name,
        'last_name':user.last_name,
        'email':user.email,
      }
    )
  return jsonify(results)



@app.route('/appointment/add', methods=['POST'])
def make_appointment():
    appointment_data = dict(request.form.items())
    time_appointment_raw = appointment_data.get('time_appointment')
    time_appointment_processed = datetime.strptime(time_appointment_raw ,"%d %b %Y %H:%M")
    Appointment.create(
        user_id=appointment_data.get('user_id'),
        saloon_id=appointment_data.get('saloon_id'),
        services=appointment_data.get('services'),
        time_appointment=time_appointment_processed
    )
    result = {
        "status": "Success",
        "message": "Appointment set"
        }
    return jsonify(result)


@app.route('/appointment')
def list_appointments():
    appointments = Appointment.select()
    results = []
    for appointment in appointments:
        results.append(
            {
                'user_id': appointment.user_id,
                'time_appointment': appointment.time_appointment,
                'saloon_id': appointment.saloon_id,
                'services': appointment.services
            }
            )
    return jsonify(results)



@app.route('/saloon/add',  methods=['POST'])
def add_saloon():
    saloon_data = dict(request.form.items())
    Saloon.create(
        name=saloon_data.get('name', 'Anonymous'),
        business_number=saloon_data.get('business_number'),
        opening_time=saloon_data.get('opening_time'),
        closing_time=saloon_data.get('closing_time'),
        description=saloon_data.get('description'),
        services=saloon_data.get('services'),
        user_id=1
    )
    result = {'status': 'success'}
    return jsonify(result)


@app.route('/saloon',  methods=['GET'])
def list_saloons():
    saloons = Saloon.select()
    results = []
    for saloon in saloons:
        results.append(
            {
                'name': saloon.name,
                'business_number': saloon.business_number,
                'opening_time': saloon.opening_time,
                'closing_time': saloon.closing_time,
                'description': saloon.description,
                'services': saloon.services,
                'user_id': saloon.user_id,
             }
            )
    return jsonify(results)

if __name__ == '__main__':
    app.run(**app_start_config)