
from chatterbot.logic import LogicAdapter
import pymysql.cursors
import pymysql
from config import * 


class CheckOutAdapter(LogicAdapter):
    def can_process(self, statement):
        """
        Return true if the input statement contains
        Check In.
        """
        global words 
        words = statement.text.split()

        # User should write in this format= Check In : mm/dd/yyyy
        set111 = ['check', 'out']
        

        if all(x in statement.text.split() for x in set111):
            words = statement.text.split()
            print("i am in check in adapter true part ")
            return True
        else:
            print("i am in check in adapter false part ")
            return False

    def process(self, statement):
        from chatterbot.conversation import Statement
        print("i am in check out adapter process part ")    

        try:
            with conn.cursor() as cursor:
                #update bookings table with check in date at id 01 
                sql = "UPDATE  `slackbot`.`bookings` SET `check_out` = %s WHERE `id`= 02"
                cursor.execute(sql, (words[-1]))
            conn.commit()
        except:
            print("SQL error !")
        
        response_statement = Statement("The check out  date is updated \n")
        response_statement.confidence = 1
        print(response_statement.confidence)
        return response_statement
        
        
        