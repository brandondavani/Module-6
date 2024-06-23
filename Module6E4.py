from datetime import datetime
import sys

datetime_object = datetime.now()
print(datetime_object)
print('Type:- ',type(datetime_object))

def measure(f, i):
    print(f"On this day and time, {datetime_object}, you are {f} feet and {i} inches tall.")

print("How tall are you? (Feet,Inches): ")

for line in sys.stdin:
    data = line.strip().split(",")
    if len(data) == 2:
        feet, inches = data
        measure(feet, inches)

