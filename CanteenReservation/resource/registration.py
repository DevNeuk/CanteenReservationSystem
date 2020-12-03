
from flask_restful import Resource,reqparse
from flask import request
from flask import jsonify
from CanteenReservation.database import DataBase



class Registration(Resource):
     
      
      def insert_Customerdata(self):
        parser = reqparse.RequestParser()
        parser.add_argument('first_name', type=str)
        parser.add_argument('last_name', type=str)
        parser.add_argument('user_name', type=str)
        parser.add_argument('password', type=str)
        parser.add_argument('email', type=str)
        parser.add_argument('phone_no', type=str)
        parser.add_argument('address', type=str)
        parser.add_argument('country', type=str)
        parser.add_argument('postal_code', type=str)
        parser.add_argument('unique_id', type=str)
        args = parser.parse_args()
        #print(args['user_name'], args['password'],args)
        db = DataBase()
        table = "db_registration"
        where = "email = '" + args['email']+"'"
        #insertdata = (args['email'])
        if(db.checkCount(table,where) == 0 ):
         return db.insertCustomerData(args)
        else :
         return jsonify({"status": "0", "id": 0})
        #return jsonify(args['user_name'], args['password'])


      def getLoginInfo(self):
        db = DataBase()
        parser = reqparse.RequestParser()
        parser.add_argument('password', type=str)
        parser.add_argument('email', type=str)
        args = parser.parse_args()
        customerdata = db.getLoginInfo(args)
        return customerdata
      
      
    
     



