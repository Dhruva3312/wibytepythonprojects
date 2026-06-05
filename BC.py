import datetime as dt
import time

#COLOR DEFINITIONS (Bonus Idea 5)
RESET = "\033[0m"
GREEN = "\033[32m"
CYAN = "\033[36m"
YELLOW = "\033[33m"
MAGENTA = "\033[35m"

print(f"{CYAN}Welcome to your birthday countdown{RESET}")

year = int(input('Which year were you born in?\n'))
month = int(input('Which month (1 for Jan, 2 for Feb, and so on)?\n'))
day = int(input('Which day in that month?\n'))

date_birth = dt.datetime(year, month, day)

weekday_names = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
weekday_num = date_birth.weekday()
print('You may have forgotten which day of the week it was ...')
print('But I can tell you ... it was a ...', end = ' ')
print(f"{MAGENTA}{weekday_names[weekday_num]}{RESET}")


current_time = dt.datetime.now()
thisyear = current_time.year

#USE OF REPLACE METHOD (Bonus Idea 3)
# We use date_birth.replace() to change only the year, keeping month and day intact
thisyear_bday = date_birth.replace(year=thisyear)

if thisyear_bday > current_time:
    next_bday = thisyear_bday
else:
    # Updating the year dynamically using .replace() instead of creating a brand new object
    next_bday = thisyear_bday.replace(year=thisyear + 1)
    
print('Your next birthday will be on ...', end = ' ')
print(f"{GREEN}{next_bday}{RESET}")
print()
print('That will be a ...', end = ' ')
weekday_num = next_bday.weekday()
print(f"{MAGENTA}{weekday_names[weekday_num]}{RESET}")

print()
print()

# Wait for user input to start the loop
print("Press Enter to start the live countdown...")
input()

while next_bday > current_time:
    current_time = dt.datetime.now()
    dd = next_bday - current_time
    days_left = dd.days
    total_seconds_left = dd.seconds

    # Converting seconds to HRS, MIN, SEC
    total_mins_left, seconds_left = divmod(total_seconds_left, 60)
    hrs_left, minutes_left = divmod(total_mins_left, 60)

    # Added color (YELLOW) to the live ticking countdown string
    print(f'Your next birthday is {YELLOW}{days_left}{RESET} days {YELLOW}{hrs_left}{RESET} hrs {YELLOW}{minutes_left}{RESET} mins {YELLOW}{seconds_left}{RESET} secs away.', end = '\r')

    time.sleep(1)











