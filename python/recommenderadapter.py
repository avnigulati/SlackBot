from chatterbot.logic import LogicAdapter
import pymysql.cursors
import pymysql
from config import *
import chatterbotadaper

rec_room =""
Description = ""
class RecommenderAdapter(LogicAdapter):
    def can_process(self, statement):
        from chatterbot.conversation import Statement
        """
        Return true if the input statement contains
        Update.
        """
        global words
        global Description
        global rec_room
        newRoomType=""

        set1 = ['spacious','room','inexpensive','two','sea'] #deluxe
        set2 = ['couple','luxurious', 'sea'] #suite
        set3 = ['family','fire','place','dining','kitchen'] #condo

        if all(x in statement.text.split() for x in set1):
            words = statement.text.split()
            print("i am in delux recommender adapter")
            # newRoomType = (words[-1])
            # print("new room type = "+ newRoomType)
            # print("current name in room update =" + chatterbotadaper.currentname123)
            # UpdateName= chatterbotadaper.currentname123
            rec_room= "deluxe"
            try:
                with conn.cursor() as cursor:


                    sql1 = "SELECT Description FROM slackbot.roomtype WHERE Type='deluxe'";
                    cursor.execute(sql1)
                    Description = cursor.fetchone()
                    #"  * The rent per night is " + str(price[0]) + ".*"
                    conn.commit()
            except:
                print("SQL error !")
            return True
        if all(x in statement.text.split() for x in set2):
            words = statement.text.split()
            print("i am in suite recommender adapter")
            # newRoomType = (words[-1])
            # print("new room type = "+ newRoomType)
            # print("current name in room update =" + chatterbotadaper.currentname123)
            # UpdateName= chatterbotadaper.currentname123
            rec_room= "suite"
            try:
                with conn.cursor() as cursor:


                    sql1 = "SELECT Description FROM slackbot.roomtype WHERE Type='suite'";
                    cursor.execute(sql1)
                    Description = cursor.fetchone()
                    #"  * The rent per night is " + str(price[0]) + ".*"
                    conn.commit()
            except:
                print("SQL error !")
            return True
        if all(x in statement.text.split() for x in set3):
            words = statement.text.split()
            print("i am in condo recommender adapter")
            # newRoomType = (words[-1])
            # print("new room type = "+ newRoomType)
            # print("current name in room update =" + chatterbotadaper.currentname123)
            # UpdateName= chatterbotadaper.currentname123
            rec_room= "condo"
            try:
                with conn.cursor() as cursor:


                    sql1 = "SELECT Description FROM slackbot.roomtype WHERE Type='condo'";
                    cursor.execute(sql1)
                    Description = cursor.fetchone()
                    #"  * The rent per night is " + str(price[0]) + ".*"
                    conn.commit()
            except:
                print("SQL error !")
            return True

        else:
            return False


    def process(self, statement):
        global rec_room
        global Description
        from chatterbot.conversation import Statement

        response_statement = Statement("We would recommend you to opt for our "+ rec_room + "` rooms \n" +"Please refer to the details of the room: "+ ''.join(Description)+'\n Would you like to book a room?' )

        response_statement.confidence = 1
        print(response_statement.confidence)

        return response_statement
