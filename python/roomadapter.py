from chatterbot.logic import LogicAdapter
import pymysql.cursors
import pymysql
from config import *
import chatterbotadaper

typeroom=""
class RoomAdapter(LogicAdapter):
    def can_process(self, statement):
        """
        Return true if the input statement contains
        'what' and 'is' and 'temperature'.
        """

        set1 = ['book','suite', 'room']
        set2 = ['book','deluxe', 'room']
        set3 = ['book','condo', 'room']
        #set4 = ['suite']
        #set5 = ['delux']
        #set6 = ['condo']

        if all(x in statement.text.split() for x in set1):
            return True
        elif all(x in statement.text.split() for x in set2):
            return True
        elif all(x in statement.text.split() for x in set3):
            return True
        #elif all(x in statement.text.split() for x in set4):
            #return True
        #elif all(x in statement.text.split() for x in set6):
            #return True
        #elif all(x in statement.text.split() for x in set6):
            #return True
        else:
            return False

    def process(self, statement):
        from chatterbot.conversation import Statement

        price =0
        room =""
        BookQ = "\n When do you plan to check into the room? Pls write in format= Check In date : mm/dd/yyyy "

        if("suite" in statement.text):
            #price = 200
            room = "Suite"
            #Description = "desc here "
            No_of_rooms = ""
            global typeroom
            typeroom='suite'
            #print(chatterbotadaper.currentname)
            try:
             conn = pymysql.connect(host='localhost', port=3306, user='root', passwd='saloni', db='slackbot')
             with conn.cursor() as cursor:
                    # Create a new record
                    #sql = "UPDATE  `slackbot`.`bookings` SET `roomType` = 'delux' WHERE `id`= 01"
                    sql1 = "SELECT Description FROM slackbot.RoomType WHERE Type='suite'";
                    cursor.execute(sql1)
                    Description = cursor.fetchone()
                    print(type(Description))
                    #sql = "SELECT NoOfRooms FROM slackbot.RoomType WHERE Type='delux'";
                    #cursor.execute(sql)
                    #No_of_rooms = cursor.fetchone()
                    sql2 = "SELECT RentPerNight FROM slackbot.RoomType WHERE Type='suite'";
                    cursor.execute(sql2)
                    price = cursor.fetchone()[0]
                    price1 = str(price)
                    #typeroom = 'suite'
             conn.commit()
            except:
                print("SQL error !")


            str11 = "  * The rent per night is " + str(price) + ".*"
            response_statement = Statement("Please refer to the details of suite room-" + ". \n" + ''.join(Description)
                                 + ". \n " + "The price per night is - " + ''.join(price1) + "USD" + BookQ + " :smile: ")
            response_statement.confidence = 1
            print(response_statement.confidence)
            return response_statement
            

        elif("deluxe" in statement.text):
            #price = 200
            room = "deluxe"
            conn = pymysql.connect(host='localhost', port=3306, user='root', passwd='saloni', db='slackbot')
            #Description = "desc here "
            No_of_rooms = ""
            #global typeroom
            typeroom='deluxe'
            try:
                with conn.cursor() as cursor:
                    # Create a new record
                    #sql = "UPDATE  `slackbot`.`bookings` SET `roomType` = 'delux' WHERE `id`= 01"
                    sql1 = "SELECT Description FROM slackbot.RoomType WHERE Type='deluxe'";
                    cursor.execute(sql1)
                    Description = cursor.fetchone()
                    #sql = "SELECT NoOfRooms FROM slackbot.RoomType WHERE Type='delux'";
                    #cursor.execute(sql)
                    #No_of_rooms = cursor.fetchone()
                    sql2 = "SELECT RentPerNight FROM slackbot.RoomType WHERE Type='deluxe'";
                    cursor.execute(sql2)
                    price = cursor.fetchone()[0]
                    price1 = str(price)
                    #typeroom='deluxe'
                conn.commit()
            except:
                print("SQL error !")


            #str11 = "  * The rent per night is " + str(price[0]) + ".*"
            response_statement = Statement("Please refer to the details of deluxe room-" + ". \n" + ''.join(Description)
                                 + ". \n " + "The price per night is - " + ''.join(price1) + "USD" + BookQ + " :smile: ")
            response_statement.confidence = 1
            print(response_statement.confidence)
            return response_statement
             
        elif("condo" in statement.text):
            price = 200
            room = "Suite"
            conn = pymysql.connect(host='localhost', port=3306, user='root', passwd='saloni', db='slackbot')
            #Description = "desc here "
            No_of_rooms = ""
            #global typeroom
            typeroom="condo"
            try:
                with conn.cursor() as cursor:
                    # Create a new record
                    #sql = "UPDATE  `slackbot`.`bookings` SET `roomType` = 'delux' WHERE `id`= 01"
                    sql1 = "SELECT Description FROM slackbot.RoomType WHERE Type='condo'";
                    cursor.execute(sql1)
                    Description = cursor.fetchone()
                    #sql = "SELECT NoOfRooms FROM slackbot.RoomType WHERE Type='delux'";
                    #cursor.execute(sql)
                    #No_of_rooms = cursor.fetchone()
                    sql2 = "SELECT RentPerNight FROM slackbot.RoomType WHERE Type='condo'";
                    cursor.execute(sql2)
                    price = cursor.fetchone()[0]
                    price1= str(price)
                    #typeroom='condo'
                conn.commit()
            except:
                print("SQL error !")


            #str11 = "  * The rent per night is " + str(price[0]) + ".*"
            response_statement = Statement("Please refer to the details of condo room-" + ". \n" + ''.join(Description)
                                 + ". \n " + "The price per night is-" + ''.join(price1)  + "USD" + BookQ + " :smile: ")
            response_statement.confidence = 1
            print(response_statement.confidence)
            return response_statement
