import psycopg2
from flask_restful import Resource
from flask import jsonify
import psycopg2.extensions
import json
from json import loads
from random import randint
import psycopg2.extras
import datetime

class DataBase(Resource):
    
 @classmethod
 def CreateTable(self):
 
  try:
    connection = psycopg2.connect(database = "postgres",
                                  user = "postgre_admin",
                                  password = "postgresql",
                                  host = "dbcanteenreservation.c6i7hzivudlm.us-east-2.rds.amazonaws.com",
                                  port = "5432"
                                  )

    cur = connection.cursor()

    if(self.table_exists(connection,"db_registration")):
   
     cur.execute('''CREATE TABLE db_registration
      (ID SERIAL PRIMARY KEY,
      name     TEXT     NOT NULL,
      password       TEXT     NOT NULL,
      email          TEXT     NOT NULL,
      phone_no       TEXT     NOT NULL,
      role           TEXT     NOT NULL,
      unique_id      TEXT     NOT NULL);''')

     cur.execute("""INSERT INTO db_registration (name,password,email,phone_no,role,unique_id)
                    VALUES (%s,%s,%s,%s,%s,%s)""",("Admin","admin@123","admin@sereneneuk.ac.uk","0227894556","admin","1"))

    


    if(self.table_exists(connection,"db_menu")):
   
     cur.execute('''CREATE TABLE db_menu
      (ID SERIAL PRIMARY KEY,
      item_name     TEXT     NOT NULL,
      item_description       TEXT     NOT NULL,
      item_price          TEXT     NOT NULL,
      item_calories       TEXT     NOT NULL);''')

     cur.execute("""INSERT INTO db_menu (item_name,item_description,item_price,item_calories)
                    VALUES (%s,%s,%s,%s)""",
                    ("Apple & Grape Fruit Bag","For a tasty snack on the go, try our Apple and Grape Fruit Bag. Sweet grapes and delicious apple that are one of your five-a-day and you can even swap it into a Happy Meal® instead of Fries.","1.49","194 kJ | 46 kcal"))
     cur.execute("""INSERT INTO db_menu (item_name,item_description,item_price,item_calories)
                    VALUES (%s,%s,%s,%s)""",
                    ("Double Big Mac","Four 100% beef patties, a slice of cheese, lettuce, onion and pickles and the unbeatable, tasty Big Mac® sauce.","2.49","2901 kJ | 694 kcal"))
     cur.execute("""INSERT INTO db_menu (item_name,item_description,item_price,item_calories)
                    VALUES (%s,%s,%s,%s)""",
                    ("Buxton® Mineral Water (Still)","Perfectly refreshing mineral water from the heart of the Peak District. Great with your meal or on its own.","0.49","0 kJ | 0 kcal"))
     cur.execute("""INSERT INTO db_menu (item_name,item_description,item_price,item_calories)
                    VALUES (%s,%s,%s,%s)""",
                    ("Chicken Legend® with Cool Mayo","Succulent chicken breast fillet in a crispy coating, with lettuce and Cool Mayo in a warm, toasted bakehouse roll. Simply delicious.","3.69","2220 kJ | 529 kcal"))
     cur.execute("""INSERT INTO db_menu (item_name,item_description,item_price,item_calories)
                    VALUES (%s,%s,%s,%s)""",
                    ("Chicken Selects®","Strips of tender chicken breast in a seasoned, crispy coating.Nutrition and allergen information do not include dips.","2.69","1502 kJ | 359 kcal"))
     cur.execute("""INSERT INTO db_menu (item_name,item_description,item_price,item_calories)
                    VALUES (%s,%s,%s,%s)""",
                    ("Coca-Cola® Zero Sugar","Zero calories, zero sugar, same great Coca-Cola taste. Perfect with your meal, or as a refreshing drink.","0.69","6 kJ | 1 kcal"))
     cur.execute("""INSERT INTO db_menu (item_name,item_description,item_price,item_calories)
                    VALUES (%s,%s,%s,%s)""",
                    ("Crispy Chicken Salad","Freshly prepared salad with chicken breast in a crispy coating, lettuce, cucumber, sliced tomato.","2.49","1337 kJ | 319 kcal"))
   
     cur.execute("""INSERT INTO db_menu (item_name,item_description,item_price,item_calories)
                    VALUES (%s,%s,%s,%s)""",
                    ("Mayo Chicken","Think crispy coated chicken with lettuce and cool mayo in a deliciously soft bun. How can you resist?","3.69","6 kJ | 1 kcal"))
     cur.execute("""INSERT INTO db_menu (item_name,item_description,item_price,item_calories)
                    VALUES (%s,%s,%s,%s)""",
                    ("Oreo® McFlurry","Take two great things and put them together. Like our soft ice cream and crumbled-up Oreo cookies. Who could resist?","1.90","1086 kJ | 258 kcal"))
     cur.execute("""INSERT INTO db_menu (item_name,item_description,item_price,item_calories)
                    VALUES (%s,%s,%s,%s)""",
                    ("Quarter Pounder™ with Cheese","A quarter-pound patty of 100% beef, with two slices of cheese, onions, pickles, mustard and a dollop of tomato ketchup in a sesame seed bun. Irresistible.","4.60","2168 kJ | 518 kcal"))
   
     cur.execute("""INSERT INTO db_menu (item_name,item_description,item_price,item_calories)
                    VALUES (%s,%s,%s,%s)""",
                    ("Side Salad","New freshly prepared salad with lettuce, cucumber, sliced tomato.","2.60","65 kJ | 15 kcal"))
   
     cur.execute("""INSERT INTO db_menu (item_name,item_description,item_price,item_calories)
                    VALUES (%s,%s,%s,%s)""",
                    ("The BBQ and Bacon Chicken One - Crispy","Make it a meal to remember with crispy chicken breast strips, plus bacon with smoky BBQ sauce, cool mayo, tomato and lettuce in a soft, toasted tortilla wrap. ","3.60","2098 kJ | 500 kcal"))
   
     cur.execute("""INSERT INTO db_menu (item_name,item_description,item_price,item_calories)
                    VALUES (%s,%s,%s,%s)""",
                    ("The Sweet Chilli Chicken One – Crispy","Try crispy chicken breast with a sweet chilli sauce, cool mayo, lettuce and cucumber in a soft, toasted tortilla wrap.","2.60","1990 kJ | 474 kcal"))
   
     cur.execute("""INSERT INTO db_menu (item_name,item_description,item_price,item_calories)
                    VALUES (%s,%s,%s,%s)""",
                    ("Tropicana® Orange Juice","A bottle of real orange juice that's great with your meal.","1.60","455 kJ | 108 kcal"))
   
     cur.execute("""INSERT INTO db_menu (item_name,item_description,item_price,item_calories)
                    VALUES (%s,%s,%s,%s)""",
                    ("Cappuccino","A double shot of Arabica bean espresso with steamed organic semi-skimmed milk, creating the perfect frothy texture. Totally delicious and topped with a chocolatey dusting.","1.90","406 kJ | 97 kcal"))


    if(self.table_exists(connection,"db_booking")):
   
      cur.execute('''CREATE TABLE db_booking
      (ID SERIAL PRIMARY KEY,
      booking_timeslot   TEXT     NOT NULL,
      booking_status     TEXT     NOT NULL,
      total_price     TEXT     NOT NULL,
      booking_id     TEXT     NOT NULL,  
      total_count     TEXT     NOT NULL,
      unique_id      TEXT     NOT NULL);''')


    if(self.table_exists(connection,"db_bookingitems")):
   
      cur.execute('''CREATE TABLE db_bookingitems
      (ID SERIAL PRIMARY KEY,
      item_price          TEXT     NOT NULL,
      item_description          TEXT     NOT NULL,
      item_calories          TEXT     NOT NULL,
      item_count       TEXT     NOT NULL,
      item_name           TEXT     NOT NULL,
      booking_id      TEXT     NOT NULL);''')
   


    connection.commit()
    cur.close()
    connection.close()

  except (Exception, psycopg2.Error) as error :
     print ("Error while connecting to PostgreSQL", error)
  finally:
    #closing database connection.
        if(connection):
           cur.close()
           connection.close()
           print("PostgreSQL connection is closed")
   

   


 def checkConnection(self):
     conn = psycopg2.connect(database = "postgres",
                                  user = "postgre_admin",
                                  password = "postgresql",
                                  host = "dbcanteenreservation.c6i7hzivudlm.us-east-2.rds.amazonaws.com",
                                  port = "5432"
                                  )
     return conn

 def table_exists(dbcon, tablename):
    exists = False
    try:
       dbcur = dbcon.cursor()
       dbcur.execute("""
        SELECT COUNT(*)
        FROM information_schema.tables
        WHERE table_name = '{0}'
        """.format(tablename.replace('\'', '\'\'')))
       if dbcur.fetchone()[0] == 1:
        exists = True
        dbcur.close()
        return False
       dbcur.close()
       return True
    except psycopg2.Error as e:
        print (e)
        return exists


 def insertCustomerData(self,args):
     name = args['name']
     password = args['password']
     email = args['email']
     phone_no = args['phone_no']
     unique_id = self.generaterandomNumber()
     query = """INSERT INTO db_registration (name,password,email,phone_no,role,unique_id) VALUES (%s,%s,%s,%s,%s,%s) RETURNING id """
     insertdata = (name,password,email,phone_no,"user",unique_id)
     insertval = self.insertQuery(query,insertdata)
     status = {"status": "1", "id": insertval}
     return jsonify(status)

 def checkCount(self,table,where):
     conn = self.checkConnection()
     cursor = conn.cursor()
     query = "select count(*) from "+ table + " where "+ where
     print(query)
     #query = "select count(*) from db_registration where email = 'joefreeda.30@gmail.com'"
     #cursor.execute(query,(inputdata,))
     cursor.execute(query)
     insertvalue = cursor.fetchone()[0]
     cursor.close()
     conn.commit()
     conn.close()
     return insertvalue

 def generaterandomNumber(self):
     return randint(100, 999)

 def insertQuery(self,query,insertdata):
     conn = self.checkConnection()
     cursor = conn.cursor()
     cursor.execute(query,insertdata)
     insertvalue = cursor.fetchone()[0]
     cursor.close()
     conn.commit()
     conn.close()
     return insertvalue

 def getLoginInfo(self,args) :
     password = args['password']
     email = args['email']
     query = "select json_agg(t) from (select * from db_registration where email = %s and password = %s)  t"
     #query = """select json_agg(t) from (select * from db_registration,db_roombooking  where (case when (select role from db_registration where db_registration.email = %s and db_registration.password = %s)='admin' then db_registration.unique_id = db_roombooking.unique_id else db_registration.email = %s	and db_registration.password = %s and  db_registration.unique_id = db_roombooking.unique_id  END) ) t"""
     #query = "select * from db_registration where email = %s and password = %s"
     insertValue = (email,password)
     customerdata = self.selectQuery(query,insertValue)
     status = {"status": "1", "data": customerdata}
     return jsonify(status)

 def selectQuery(self,query,insertdata):
     conn = self.checkConnection()
     #cursor = conn.cursor(cursor_factory=psycopg2.extras.DictCursor)
     cursor = conn.cursor()
     cursor.execute(query,insertdata)
     insertvalue = cursor.fetchall()[0]
     cursor.close()
     conn.commit()
     conn.close()
     return insertvalue[0]

 def selectwithoutreturn(self,query,insertdata):
     conn = self.checkConnection()
     cursor = conn.cursor()
     cursor.execute(query,insertdata)
     cursor.close()
     conn.commit()
     conn.close()

 def selectQuerywithoutargs(self,query):
     conn = self.checkConnection()
     cursor = conn.cursor()
     cursor.execute(query)
     insertvalue = cursor.fetchall()[0]
     cursor.close()
     conn.commit()
     conn.close()
     return insertvalue[0]

 def bookorder(self,json_data) :

        bookingId = self.generaterbookingId()

        query1 = """INSERT INTO db_booking (booking_timeslot,booking_status,total_price,booking_id,total_count,unique_id)
                    VALUES (%s,%s,%s,%s,%s,%s) RETURNING booking_id"""
        insertbookingdata = (
                      json_data['booking_timeslot'],
                      json_data['booking_status'],
                      json_data['total_price'],bookingId,json_data['total_count'],json_data['unique_id'])
        self.insertQuery(query1,insertbookingdata)

        for x in json_data['items']:
            itemname = x['item_name']
            itemprice = x['item_price']
            itemcount = x['item_count']
            itemdescription = x['item_description']
            itemcalories = x['item_calories']
            query2 = """INSERT INTO db_bookingitems (item_price,item_description,item_calories,item_count,item_name,booking_id)
                    VALUES (%s,%s,%s,%s,%s,%s) RETURNING booking_id"""
            insertbookingitemsdata = (itemprice,itemdescription,itemcalories,itemcount,itemname,bookingId)
            self.insertQuery(query2,insertbookingitemsdata)   

      
        status = {"status": "1", "id": bookingId}
        return jsonify(status)
            
 

 def generaterbookingId(self):
     return randint(10000, 99999)


 

 def getfoodmenu(self):
     query = "select json_agg(t) from (select * from db_menu order by id)  t"
     customerdata = self.selectQuerywithoutargs(query)
     status = {"status": "1", "data": customerdata}
     return jsonify(status)

 def getOrderDetailsByBookingID(self,args) :
     if(args['role']=='admin'):

          #query = "select json_agg(t) from (select * from db_booking INNER JOIN db_bookingitems on (db_booking.booking_id  = db_bookingitems.booking_id))  t"
          query = "select json_agg(t) from (SELECT db_booking.id,db_booking.booking_timeslot,db_booking.total_price,db_booking.booking_status,db_booking.unique_id,db_booking.total_count,db_booking.booking_id,db_registration.name , json_agg (( SELECT x FROM (SELECT db_bookingitems.id,db_bookingitems.item_price,db_bookingitems.item_description,db_bookingitems.item_calories,db_bookingitems.item_count,db_bookingitems.item_name,db_bookingitems.booking_id)AS x)) AS items FROM  db_booking INNER JOIN db_registration on 	db_registration.unique_id = db_booking.unique_id INNER JOIN   db_bookingitems ON db_bookingitems.booking_id = db_booking.booking_id GROUP  BY db_booking.id,db_registration.id) t"
          intsolu = self.selectQuerywithoutargs(query)
          status = {"status": "1", "menu": intsolu}
     else :
          unique_id = args['unique_id']
          #queryinneritems = "select json_agg(t) from (select item_name,item_price,item_count from db_booking INNER JOIN db_bookingitems on (db_booking.booking_id  = db_bookingitems.booking_id) where unique_id = %s) t" 
          #queryouteritems = "select json_build_object(t) from (select * from db_booking where unique_id = %s and booking_id = %s,select json_agg(d) from (select item_name,item_price,item_count from db_booking INNER JOIN db_bookingitems on (db_booking.booking_id  = db_bookingitems.booking_id) where unique_id = %s) d) t"
          query = "select json_agg(t) from (SELECT db_booking.id,db_booking.booking_timeslot,db_booking.total_price,db_booking.booking_status,db_booking.unique_id,db_booking.total_count,db_booking.booking_id, json_agg((SELECT x FROM (SELECT db_bookingitems.id, db_bookingitems.item_price,db_bookingitems.item_description,db_bookingitems.item_calories,db_bookingitems.item_count,db_bookingitems.item_name,db_bookingitems.booking_id)AS x)) AS items FROM   db_booking JOIN   db_bookingitems ON db_bookingitems.booking_id = db_booking.booking_id where db_booking.unique_id = %s GROUP  BY db_booking.id) t"
          insertbookingdata = (unique_id,)

          #intvalue = self.selectQuery(queryinneritems,insertbookingdata)
          intsolu = self.selectQuery(query,insertbookingdata)
          status = {"status": "1", "menu": intsolu}

     return jsonify(status)









 