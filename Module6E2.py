from datetime import datetime, timedelta

print()
print(f"The current date and time is: {datetime.now()}")
print()
print(f"The date and time for exactly one day from now is: {datetime.now() + timedelta(days=1)}")
print()
print(f"The date and time 1 minute ago is: {datetime.now() - timedelta(seconds=60)}")
print()
print(f"The date and time exactly two years from now is: {datetime.now() + timedelta(days=730)}")
