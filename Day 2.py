import math
import os
import random
import re
import sys

# Complete the solve function below.
#def solve(meal_cost, tip_percent, tax_percent):
#def solve(meal_cost, tip_percent, tax_percent):
if __name__ == '__main__':

    meal_cost = float(input().strip())
    tax_percent = int(input().strip())
    tip_percent = int(input().strip())
    tip_percent=meal_cost*tip_percent/100
    tax_percent=meal_cost*tax_percent/100
    totalcost=meal_cost+tip_percent+tax_percent
    print(round(totalcost))
