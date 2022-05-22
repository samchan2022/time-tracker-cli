from datetime import datetime, timedelta
from config import config
from utils import time_util

class Timer():
    def __init__(self, con):
        self.con = con

    # Create table
    def init_timer(self):
        cur = self.con.cursor()
        cur.execute('''CREATE TABLE IF NOT EXISTS TIMER
                       (
                            ID INTEGER PRIMARY KEY AUTOINCREMENT,
                            START_TIME         DATE      NOT NULL,
                            END_TIME           DATE      ,
                            NAME               TEXT UNIQUE,
                            MESSAGE            CHAR(50),
                            NO_OF_SECOND       real NOT NULL,
                            TIMER_STATUS       BOOLEAN NOT NULL,
                            CREATE_DATE        DATE,
                            UPDATE_DATE        DATE
                        )''')
        self.con.commit()
    
    def start_timer(self, name, msg):
        cur = self.con.cursor()
        # insert timer entry if not exists
    
        cur.execute(f"SELECT  * FROM TIMER WHERE name = '{name}'")
    
        data = cur.fetchone()
        # if has data
        if data:
            if data['TIMER_STATUS'] == False:
                cur.execute(f"UPDATE TIMER SET TIMER_STATUS = True, START_TIME = '{datetime.now()}', END_TIME = null, UPDATE_DATE = '{ datetime.now() }' where name='{name}'")
                self.con.commit()
                print(f"Restart the timer {name}")
            else:
                print(f"The timer {name} has been stared.")
        else:
            print(f"Adding a new timer: {name}")
            cur.execute(f"INSERT INTO TIMER (NAME, START_TIME, MESSAGE, NO_OF_SECOND, TIMER_STATUS, CREATE_DATE ) VALUES ( '{ name }', '{ datetime.now() }', '{msg}',0 ,True, '{ datetime.now() }')")
            self.con.commit()
    
    def stop_timer(self, name):
        cur = self.con.cursor()
        cur.execute(f"SELECT  * FROM TIMER WHERE name = '{name}'")
        data = cur.fetchone()
        if data:
            if data['TIMER_STATUS'] == True:
                print(f"Stopping timer: {name}")
                s_time = datetime.strptime(data['START_TIME'] , config.DATE_FORMAT)
                now = datetime.now()
                # Accumulate the no of second
                no_of_second = data["NO_OF_SECOND"] + (now - s_time ).total_seconds()
                cur.execute(f"UPDATE TIMER SET TIMER_STATUS = False, END_TIME = '{datetime.now()}', NO_OF_SECOND = {no_of_second} where name='{name}'")
                self.con.commit()
            else:
                print(f"Timer {name} has already been stopped.")
        else:
            print(f"Timer {name} is not found.")
    
    def update_msg(self, name, msg):
        cur = self.con.cursor()
        cur.execute(f"UPDATE TIMER SET MESSAGE = '{msg}' where name = '{name}'")
        print(f"The message for Timer {name} is updated to {msg}.")
        self.con.commit()
    
    def get_all_timers(self):
        cur = self.con.cursor()
        cur.execute("SELECT * FROM TIMER" )
        records = cur.fetchall()
        print("Number of timers:", len(records))
        for row in records:
            s_time = datetime.strptime( row["START_TIME"], config.DATE_FORMAT)
            e_time = datetime.now()
            if row['END_TIME']:
                e_time = datetime.strptime(row['END_TIME'], config.DATE_FORMAT)
            name = row['name']
            msg = row['message']
            no_of_second = row['no_of_second']
            d_diff = (e_time - s_time).total_seconds() + no_of_second
            d, h, m ,s = time_util.seconds_to_dhms(d_diff)

            details = f"{name}: {d:.0f}day {h:.0f}hour {m:.0f}min {s:.0f}sec" 
            if not (msg == None or msg == "None"):
                details = details + " " + msg

            print(details)
    
    def delete_timer(self, name):
        cur = self.con.cursor()
        cur.execute(f"DELETE FROM TIMER where name = '{name}'")
        print(f"The timer {name} has been deleted.")
        self.con.commit()

