
from chatterbot.logic import LogicAdapter
import pymysql.cursors
import pymysql
from config import *


current_user_id = 0
current_name = ""
class MyLogicAdapter(LogicAdapter):
    def can_process(self, statement):
        """
        Return true if the input statement contains
        'what' and 'is' and 'temperature'.
        """
        set1 = ['i', 'am']
        set2 = ['my', 'name']

        if all(x in statement.text.split() for x in set1):
            words = statement.text.split()
            try:
                with conn.cursor() as cursor:
                    # Create a new record
                    sql = "UPDATE  `slackbot`.`currentuser` SET `username` = %s WHERE `id`= 01"
                    cursor.execute(sql, (words[-1]))
                conn.commit()
            except:
                print("This is an sql error message!")
            return True
        elif all(x in statement.text.split() for x in set2):
            words = statement.text.split()
            try:
                with conn.cursor() as cursor:
                    sql = "UPDATE  `currentuser` SET `username` = %s WHERE `id`= 01"
                    cursor.execute(sql, (words[-1]))
                conn.commit()
            except:
                print("This is an sql error message!")
            return True
        else:
            return False

    def process(self, statement):
        from chatterbot.conversation import Statement
        words = statement.text.split()
        response_statement = Statement('Welcome '+ words[-1] +'! Which room do you want')
        global current_name
        current_name  = words[-1]
        print("=================i am printing current_name" + current_name)
        global current_user_id
        current_user_id = 789 
        response_statement.confidence = 1
        print(response_statement.confidence)
        return response_statement