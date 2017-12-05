from chatterbot.logic import LogicAdapter
import pymysql.cursors
import pymysql
from config import *
import chatterbotadaper

resp_str = ""
class UpdateAdapter(LogicAdapter):
    def can_process(self, statement):
        from chatterbot.conversation import Statement
        """
        Return true if the input statement contains
        Update.
        """
        global words
        global resp_str
        newRoomType=""

        set1 = ['yes','update','room']
        set2 = ['yes','update', 'check','in']

        if all(x in statement.text.split() for x in set1):
            words = statement.text.split()
            print("i am in update adapter")
            newRoomType = (words[-1])
            print("new room type = "+ newRoomType)
            print("current name in room update =" + chatterbotadaper.currentname123)
            UpdateName= chatterbotadaper.currentname123
            try:
                with conn.cursor() as cursor:
                    newRoomType = (words[-1])
                    print("new room type = "+ newRoomType)
                    updateRoom = "UPDATE  slackbot.bookings SET roomType = (%s) WHERE username = (%s)"
                    cursor.execute(updateRoom, (newRoomType, UpdateName) )
                    newPrice = "SELECT RentPerNight FROM slackbot.RoomType WHERE Type=(%s)";
                    cursor.execute(newPrice,(newRoomType))
                    price = cursor.fetchone()

                    resp_str = ("Now, your room price per day is " + str(price[0]) + " USD")
                    #"  * The rent per night is " + str(price[0]) + ".*"
                    conn.commit()
            except:
                print("SQL error !")
            return True
        if all(x in statement.text.split() for x in set2):
            words = statement.text.split()
            print("i am in update adapter")
            newRoomType = (words[-1])
            print("new room type = "+ newRoomType)
            print("current name in ckeckIn update =" + chatterbotadaper.currentname123)
            UpdateName= chatterbotadaper.currentname123
            try:
                with conn.cursor() as cursor:
                    newCheckIn = (words[-1])
                    print("new room type = "+ newCheckIn)
                    #print("current name in update =" + currentname)
                    updateCheckIn = "UPDATE  slackbot.bookings SET checkIn = (%s) WHERE username = (%s)"
                    cursor.execute(updateCheckIn, (newCheckIn, UpdateName) )
                    resp_str = ("Check-In date has been modified. ")
                    conn.commit()
            except:
                print("SQL error !")
            return True
        else:
            return False


    def process(self, statement):
        global resp_str
        from chatterbot.conversation import Statement

        response_statement = Statement("Update completed ! \n" + resp_str )

        response_statement.confidence = 1
        print(response_statement.confidence)

        return response_statement
