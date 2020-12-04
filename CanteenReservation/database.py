import psycopg2
from flask_restful import Resource
from flask import jsonify
import psycopg2.extensions
import json
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






 def generaterbookingId(self):
     return randint(10000, 99999)


 def getDatabyLoginId(self,args):
     if(args['role']=='admin'):
          query = "select json_agg(t) from (select * from db_registration INNER JOIN db_roombooking on (db_registration.unique_id = db_roombooking.unique_id) where db_registration.role = 'user')  t"
     else :
          query = "select json_agg(t) from (select * from db_roombooking where unique_id = %s)  t"
     insertValue = (args['unique_id'],)
     customerdata = self.selectQuery(query,insertValue)
     return jsonify(customerdata)











 