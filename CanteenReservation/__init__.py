from flask import Flask
from flask_restful import Api,Resource
from .resource.registration import Registration
from .resource.booking import Booking
from CanteenReservation.database import DataBase
import json
import requests
from flask import jsonify
from flask_cors import CORS

from flask import Flask
app = Flask(__name__)
CORS(app)


@app.route('/')
def getname():
  status = {"status": "1", "id": "Hello"}
  return jsonify(status)

api = Api(app)

@app.before_first_request
def create_tables():
  
     DataBase.CreateTable()

