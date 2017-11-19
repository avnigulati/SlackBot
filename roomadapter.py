
from chatterbot.logic import LogicAdapter
import pymysql.cursors
import pymysql


class RoomAdapter(LogicAdapter):
    def can_process(self, statement):
        """
        Return true if the input statement contains
        'what' and 'is' and 'temperature'.
        """
        set1 = ['sweet', 'room']
        set2 = ['delux', 'room']
        set3 = ['condo', 'room']

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

        if("sweet" in statement.text):
            price = 200
            room = "Sweet"
        elif("delux" in statement.text):
            price =100
            room = "Delux"
        elif("condo" in statement.text):
            price = 150
            room = "Condo"

        response_statement = Statement(""+room+" room price per day is "+str(price)+" dollars")

        response_statement.confidence = 1
        print(response_statement.confidence)

        return response_statement