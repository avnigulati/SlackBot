
from chatterbot.logic import LogicAdapter
import pymysql.cursors
import pymysql
from config import *
from roomadapter import *
from chatterbotadaper import * 


class CheckInAdapter(LogicAdapter):
    def can_process(self, statement):
        """
        Return true if the input statement contains
        Check In.
        """
        global words
        words = statement.text.split()

        # User should write in this format= Check In : mm/dd/yyyy
        set111 = ['check', 'in']

        if all(x in statement.text.split() for x in set111):
            words = statement.text.split()
            print("i am in check in adapter true part ")
            return True
        else:
            print("i am in check in adapter false part ")
            return False

    def process(self, statement):
        from chatterbot.conversation import Statement
        print("i am in check in adapter process part ")

        
        with conn.cursor() as cursor:
                #update bookings table with check in date at id 01
                #sql = "SELECT  COUNT(*) FROM `slackbot`.`bookings` WHERE `roomType`= %s"
                #cursor.execute(sql, 'suite')
                #result=cursor.fetchone()
                #print(result)
                #sql1 = "SELECT `NoOfRooms` FROM `slackbot`.`roomtype` WHERE `Type`=%s"
                #cursor.execute(sql1,'suite')
                #result1=cursor.fetchone()
                ##print(result1)
                #if result1 > result:
                #   available = 13
                sql = "SELECT COUNT(*) FROM `slackbot`.`roomnumber` WHERE `roomtype`=%s AND `isavailable`='Y'"
                cursor.execute(sql,'suite')
                result = cursor.fetchone()[0]
                if result > 0:
                  sql1 = "SELECT `roomnumber` FROM `slackbot`.`roomnumber` WHERE `roomtype`=%s AND `isavailable`='Y'"
                  cursor.execute(sql1,'suite')
                  roomnumber = cursor.fetchone()[0]
                  print(type(words[-1]))
                  print(type(roomnumber))
                  
                  #print(words[-1])
                  sql2 = "insert into bookings(roomType,check_in,roomnumber,customer_id) VALUES('%s', '%s', '%d', '%d')" % \
                           ('suite', words[-1] , int(roomnumber) ,49)
                  cursor.execute(sql2)
                  sql3 = "UPDATE  `slackbot`.`roomnumber` SET `isavailable` = 'N' WHERE `roomnumber`='%d'"
                  cursor.execute(sql3,roomnumber)
                  
                  
                  
                  
                
                
        conn.commit()
        

        response_statement = Statement("The check in date is updated \n"+
                            ''.join(str(roomnumber)))
        response_statement.confidence = 1
        print(response_statement.confidence)
        return response_statement
