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

@app.route('/register', methods = ['POST'])
def registration_fun() :
     registerinstance = Registration()
     return registerinstance.insert_Customerdata()

@app.route('/login',methods = ['POST'])
def login_fun():
    registerinstance = Registration()
    return registerinstance.getLoginInfo()

@app.route('/menu',methods = ['POST'])
def menu_info():
    registerinstance = Registration()
    return registerinstance.getmenu()

@app.route('/bookorder',methods = ['POST'])
def bookorder_fun():
    booking = Booking()
    return booking.insertOrderDetails()

@app.route('/vieworder',methods = ['POST'])
def vieworder_fun():
    booking = Booking()
    return booking.getOrderDetailsInfo()
