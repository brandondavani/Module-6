import sys
from datetime import datetime

print("What is the store, item, cost, and payment?")
time = datetime.now()

for line in sys.stdin:
    data = line.strip().split(",")
    if len(data) == 4:
        store, item, cost, payment = data
        print("Date/Time: {0}\tItem: {1}\tCost: {2}".format(time, item, cost))
        
