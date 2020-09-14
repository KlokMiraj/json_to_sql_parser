import sys
import argparse

parser=argparse.ArgumentParser(prog="milk profit calculator",description="program to calculate profit of milk \n usages: \n use as python Nines.py --lmilk [the milk you produced today]")
parser.add_argument('--lmilk',nargs=1)
parser.parse_args(sys.argv[1:])
mipro=sys.argv[2:]
Nines(mipro)

class Nines(self):
    def __init__(mipro):
        mipro=mipro
        print(mipro)
        calcmilk(mipro)
        costcalc(mipro)
        totprofit(mipro)
            # tocalculate the total amount of milk in leters

        def calcmilk(mipro):
            # number of carton needed to hold the mipro
            totcar=mipro/3.78
            totcar=round(totcar)
            print(totcar+"is the total amount of carton you make")
            return totcar

            # to calculate tthe total cost associated
        def costcalc(mipro):
            totliters=calcmilk(mipro)*0.38
            print(totliters+"is total amount of cost associated")

            # t calculate the total profit
        def totprofit(mipro):
            totcar=calcmilk(mipro)
            proftot=totcar*27
            print(proftot+"is the total amount of profit you make")
