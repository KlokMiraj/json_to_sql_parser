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
        write_sql(df)
        # print(create_view())

database_name=""
con=sqlite3.connect(database_name+".db")


def cone(database_name):
    kursor=con.cursor()
    return kursor

def create_view():
        query=cone(database_name).execute("select * from "+"table_"+database_name+" ")
        record=cone(database_name).fetchall()
        return record

def write_sql(df):
    # df.to_sql("table_"+database_name,con,if_exists='append')
    return 0
    # def tpoint(df,con):
    #     print(con)
    #     print(df)
    #     if(con==False):
    #             print(database_name)
    #             print(con)
    #             try:
    #                 con.cursor().execute("SQLite3 "+ database_name[0] +".db")
    #             except IOError as e:
    #                     print(e)
    # tpoint(df,con)
    # def __con__(database_name):
    #     print(database_name)
