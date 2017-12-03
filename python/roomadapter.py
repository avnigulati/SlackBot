
from chatterbot.logic import LogicAdapter
import pymysql.cursors
import pymysql
from config import *


class RoomAdapter(LogicAdapter):
    def can_process(self, statement):
        """
        Return true if the input statement contains
        'what' and 'is' and 'temperature'.
        """

        set1 = ['book','sweet', 'room']
        set2 = ['book','delux', 'room']
        set3 = ['book','condo', 'room']

        if all(x in statement.text.split() for x in set1):
            return True
        elif all(x in statement.text.split() for x in set2):
            return True
        elif all(x in statement.text.split() for x in set3):
            return True
        else:
            return False

    def process(self, statement):
        from chatterbot.conversation import Statement

        price =0
        room =""
        BookQ = "\n When do you plan to check into the room? Pls write in format= Check In : mm/dd/yyyy "

        if("sweet" in statement.text):
            price = 200
            room = "Sweet"


        elif("delux" in statement.text):
            price =100
            room = "Delux"
            conn = pymysql.connect(host='localhost', port=3306, user='root', passwd='avni123', db='slackbot')
            Description = "desc here "
            No_of_rooms = ""

            try:
                with conn.cursor() as cursor:
                    # Create a new record
                    sql = "UPDATE  `slackbot`.`bookings` SET `roomType` = 'delux' WHERE `id`= 01"
                    sql = "SELECT Description FROM slackbot.RoomType WHERE Type='delux'";
                    cursor.execute(sql)
                    Description = cursor.fetchone()
                    sql = "SELECT NoOfRooms FROM slackbot.RoomType WHERE Type='delux'";
                    cursor.execute(sql)
                    No_of_rooms = cursor.fetchone()
                    sql = "SELECT RentPerNight FROM slackbot.RoomType WHERE Type='delux'";
                    cursor.execute(sql)
                    price = cursor.fetchone()
                conn.commit()
            except:
                print("SQL error !")


            str11 = "  * The rent per night is " + str(price[0]) + ".*"
            response_statement = Statement("Delux `room` _is_ added ~to~ database \n" + ''.join(Description)
                                 + "\n " + str(No_of_rooms[0]) + ". \n " + str11 + " :smile: " + BookQ)
            response_statement.confidence = 1
            print(response_statement.confidence)
            return response_statement
        elif("condo" in statement.text):
            price = 150
            room = "Condo"


        response_statement = Statement(room + " room price per day is " + str(price) + " USD")

        response_statement.confidence = 1
        print(response_statement.confidence)

        return response_statement
