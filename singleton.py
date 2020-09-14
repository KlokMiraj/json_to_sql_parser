import sqlite3
import os
import pandas


class Singleton():
    def __init__(self,database_name,df):
        print(df.columns)
        print(database_name)

        database_name=database_name[0]
        if (os.path.exists(database_name[0]+".db")):
                print("Database "+"'"+database_name[0]+"'"+" Already Exists")
                print("Please choose another database name if you'd like to work on different database")
        df.to_sql(database_name,con,if_exists="replace")
        # ddprint(create_view())
        for records in create_view(database_name):
            (records)

database_name=""
try:
    con=sqlite3.connect(database_name+".db")
except IOError as err:
    print(err)



def cone():
    kursor=con.cursor()
    return kursor

def create_view(database_name):
        count=2005
        query=cone().execute("SELECT * FROM "+database_name+"WHERE year="+sum(count,5)+";")
        count=count+5
        record=query.fetchall()
        if record:
            return record
