# initializing variables
meterPerSecond = 300000000  # light base rate (299,792,458 rounded up)
seconds = 60
inMinutes = 60  # seconds in minutes
inHours = 60  # minutes in hours
inDays = 24  # hours in days
inYears = 365  # days in years

distance = meterPerSecond * seconds * inMinutes * inDays * inYears

print("Light travels", distance, "meters in a year.")
