from flask_restful import Resource,reqparse
from flask import request
from CanteenReservation.database import DataBase

class Booking(Resource):
   
  
    def insertOrderDetails(self):
        parser = reqparse.RequestParser()
        parser.add_argument('unique_id', type=str)
        parser.add_argument('items', type=dict)
        parser.add_argument('total_count', type=str)        
        parser.add_argument('booking_status', type=str)
        parser.add_argument('total_price', type=str)
               
        args = parser.parse_args()
        db = DataBase()
        return db.bookorder(args)

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



