from datetime import *
import pytz


PO = pytz.timezone('US/Pacific')

NY = pytz.timezone('US/Eastern')

LO = pytz.timezone('Europe/London')

d = datetime.now()

POtime = d.astimezone(PO)

NYtime = d.astimezone(NY)

LOtime = d.astimezone(LO)

print("Is the portland store open?")
if (POtime.hour >= 9 and POtime.hour <= 17):
    print("The Tech Academy is open!")
else:
    print("The Tech Academy is closed!")


if (NYtime.hour >= 9 and NYtime.hour <= 17):
    print("The Tech Academy is open!")
else:
    print("The Tech Academy is closed!")
    

if (LOtime.hour >= 9 and LOtime.hour <= 17):
    print("The Tech Academy is open!")
else:
    print("The Tech Academy is closed!")
    






