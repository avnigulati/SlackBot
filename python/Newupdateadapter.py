from chatterbot.logic import LogicAdapter
import pymysql.cursors
import pymysql
from config import *
import chatterbotadaper

global BookQ
global CurrentUsername
class UpdateAdapter(LogicAdapter):
    def can_process(self, statement):
        from chatterbot.conversation import Statement
        """
        Return true if the input statement contains
        Update.
        """
        global words
        # global namewords
        # global username
        newRoomType=""

        set1 = ['want','update','room','suite','deluxe','condo']
        #set2 = ['change','room','suite','deluxe','condo']
        set3 = ['update', 'check','in','date']

        if all(x in statement.text.split() for x in set1):
            words = statement.text.split()
            print("i am in update adapter")


            print(" I am in room update ")
            newRoomType = (words[-1])
            print("new room type = "+ newRoomType)
            print("current name in update =" + chatterbotadaper.currentname123)
            #conn = pymysql.connect(host='localhost', port=3306, user='root', passwd='avni123', db='slackbot')
            try:
                with conn.cursor() as cursor:

                # sql = ("SELECT roomType FROM slackbot.bookings WHERE 'username' ='avni'")
                # cursor.execute(sql)
                # oldRoomtype = cursor.fetchone()
                    newRoomType = (words[-1])
                    print("new room type = "+ newRoomType)
                    #print("current name in update =" + currentname)
                    updateRoom = "UPDATE  slackbot.bookings SET roomType = (%s) WHERE username = 'avni'"
                    cursor.execute(updateRoom, (newRoomType) )

                    conn.commit()
            except:
                print("SQL error !")
            return True
        elif all(x in statement.text.split() for x in set3):
            words = statement.text.split()
            print("i am in update check in adapter")
            newCheckIn = (words[-1])
            print("new room type = "+ newCheckIn)
            #print("current name in update =" + currentname)
            #conn = pymysql.connect(host='localhost', port=3306, user='root', passwd='avni123', db='slackbot')
            try:
                with conn.cursor() as cursor:

                    newCheckIn = (words[-1])
                    print("new room type = "+ newCheckIn)
                    #print("current name in update =" + currentname)
                    updateCheckIn = "UPDATE  slackbot.bookings SET checkin = (%s) WHERE username = 'avni'"
                    cursor.execute(updateCheckIn, (newRoomType) )

                    conn.commit()
            except:
                print("SQL error !")
            return True
        else:
            return False
        # elif all(x in statement.text.split() for x in set2):
        #
        #     print("i am in update adapter")
        #     return True
        # elif all(x in statement.text.split() for x in set3):
        #
        #     print("i am in update adapter")
        #     return True


        # if("update" in statement.text):
            # if("room" in statement.text):



            # response_statement = Statement("Room updated to " + newRoomType)
            # response_statement.confidence = 1
            # print(response_statement.confidence)
            # return response_statement


    def process(self, statement):
        from chatterbot.conversation import Statement

        response_statement = Statement("Update completed !")

        response_statement.confidence = 1
        print(response_statement.confidence)

        return response_statement
