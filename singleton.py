import sqlite3
import os
import pandas

class Singleton():
    def __init__(self,database_name,df):
        print(df.columns)
    
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
    print("Please Enter The Start Year:")
    start_year=input()
    print("PLease Enter the end year:")
    end_year=input()
    print("Please Enter the Product Name [NAME_OPTIONS:'Petrol','Diesel','Kerosene'...... etc]:")
    product=input()
    rep=create_view(database_name,start_year,end_year,product)
    print(" \t Year-Interval \t\t Min  \t Max \t \t Avg")
    print(product,"\t"+start_year+"-"+end_year+"\t",rep[0],rep[1],rep[2])
