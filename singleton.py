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
        select_report(database_name)


database_name=""
try:
    con=sqlite3.connect(database_name+".db")
except IOError as err:
    print(err)

def cone():
    kursor=con.cursor()
    return kursor

def create_view(database_name,start_year,end_year,petroleum_product):
        query_max=cone().execute("SELECT MAX(sale) FROM "+database_name+" WHERE  year BETWEEN {} and {} AND petroleum_product=='{}'".format(start_year,end_year,petroleum_product))
        record1=query_max.fetchall()
        query_min=cone().execute("SELECT MIN(sale) FROM "+database_name+" WHERE  year BETWEEN {} and {} AND petroleum_product=='{}'".format(start_year,end_year,petroleum_product))
        record2=query_min.fetchall()
        query_avg=cone().execute("SELECT AVG(sale) FROM "+database_name+" WHERE  year BETWEEN {} and {} AND petroleum_product=='{}'".format(start_year,end_year,petroleum_product))
        record3=query_avg.fetchall()

        return record1, record2, record3

def select_report(database_name):
    rep=create_view(database_name,'2005','2010','Petrol')
