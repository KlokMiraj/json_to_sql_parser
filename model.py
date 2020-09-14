
import json
import sys
import argparse
import os
import pandas
import numpy
from sklearn import preprocessing
from singleton import Singleton


class Phrase(Singleton):
    def __init__(self, path_file,database_name):
        readf(path_file)
        # writef(database_name)
        Singleton(database_name,readf(path_file))

def readf(path_file):

    try:
        with open(path_file[0]) as datafile:
            CONFIG_PROPERTIES=json.load(datafile)

            df=pandas.DataFrame(CONFIG_PROPERTIES)
            df.head
            return df
    except IOError as e:
        print(e)

def writef(database_name):
    database_name=database_name[0]

    if os.path.exists(os.path.join(database_name,'.db')==False):
        with open(database_name+".db",'wb') as fi:

                for item,value in count.items():

                        #execute('INSERT INTO file VALUES(?,?)',(item,value))
                        return 0

praser=argparse.ArgumentParser(prog="jsonparser",prefix_chars="--")
praser.add_argument('--path', nargs=1)
praser.add_argument('--dbname', nargs=1)
praser.parse_args((sys.argv[1:]))
dbname=sys.argv[4:]
path_file=sys.argv[2:3]

obj=Phrase(path_file,dbname)
