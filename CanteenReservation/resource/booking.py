from flask_restful import Resource,reqparse
from flask import request
from CanteenReservation.database import DataBase
import json

class Booking(Resource):
   
  
    def insertOrderDetails(self):
       # parser = reqparse.RequestParser()
        #parser.add_argument('unique_id', type=str)
       # parser.add_argument('items', type = list, location='json')
       # parser.add_argument('total_count', type=str)         
       # parser.add_argument('booking_status', type=str)
        json_data = request.get_json()
       # readable_json = json.dumps(json_data)
       # parser.add_argument('total_price', type=str)
               
       # args = parser.parse_args()
        db = DataBase()
        return db.bookorder(json_data)

    def getCustomerInfo(self):
        parser = reqparse.RequestParser()
        parser.add_argument('unique_id', type=str)
        parser.add_argument('role',type=str)
        args = parser.parse_args()
        db = DataBase()
        return db.getDatabyLoginId(args)

    def getBookingIdInfo(self):
        parser = reqparse.RequestParser()
        parser.add_argument('booking_id', type=str)
        args = parser.parse_args()
        db = DataBase()
        return db.getDatabyBookingId(args)

    def cancelbooking(self):
        parser = reqparse.RequestParser()
        parser.add_argument('booking_id', type=str)
        args = parser.parse_args()
        db = DataBase()
        return db.cancelbooking(args)



