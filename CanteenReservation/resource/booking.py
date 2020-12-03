from flask_restful import Resource,reqparse
from flask import request
from CanteenReservation.database import DataBase

class Booking(Resource):
   
  
    def insertBookingdata(self):
        parser = reqparse.RequestParser()
        parser.add_argument('unique_id', type=str)
        parser.add_argument('adults', type=str)
        parser.add_argument('children', type=str)
        parser.add_argument('rooms', type=str)
        parser.add_argument('check_in', type=str)
        parser.add_argument('check_out', type=str)
        parser.add_argument('days', type=str)
        parser.add_argument('location', type=str)
        parser.add_argument('room_type', type=str)
        parser.add_argument('confirm_status', type=str)
        parser.add_argument('payment_status', type=str)
        parser.add_argument('price_rate', type=str)
        parser.add_argument('first_name', type=str)
        parser.add_argument('last_name', type=str)
        parser.add_argument('email', type=str)
        parser.add_argument('phone_no', type=str)
        
        args = parser.parse_args()
        db = DataBase()
        return db.insertBookingData(args)

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



