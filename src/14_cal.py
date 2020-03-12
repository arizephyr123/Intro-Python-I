"""
The Python standard library's 'calendar' module allows you to
render a calendar to your terminal.
https://docs.python.org/3.6/library/calendar.html

Write a program that accepts user input of the form
  `14_cal.py [month] [year]`
and does the following:
 - If the user doesn't specify any input, your program should
   print the calendar for the current month. The 'datetime'
   module may be helpful for this.
 - If the user specifies one argument, assume they passed in a
   month and render the calendar for that month of the current year.
 - If the user specifies two arguments, assume they passed in
   both the month and the year. Render the calendar for that
   month and year.
 - Otherwise, print a usage statement to the terminal indicating
   the format that your program expects arguments to be given.
   Then exit the program.

Note: the user should provide argument input (in the initial call to run the file) and not 
prompted input. Also, the brackets around year are to denote that the argument is
optional, as this is a common convention in documentation.

This would mean that from the command line you would call `python3 14_cal.py 4 2015` to 
print out a calendar for April in 2015, but if you omit either the year or both values, 
it should use today’s date to get the month and year.
"""

import sys
import calendar
from datetime import datetime
# or would have to use by datetime.datetime

# 14_cal.py [month] [year]
args = sys.argv
print(args)
# Read arg values

# default to current month and year
month = datetime.now().month
year = datetime.now().year
# print error message if not 1-12
if month < 1 or month > 12:
    print("ERROR: Invalid Month")
    exit(0)

# 1 arg shouold set the month and year
if len(args) == 1:
    pass
elif len(args) == 2:
    month = int(args[1])
# 2 args should set the month
elif len(args) == 3:
    month = int(args[1])
    year = int(args[2])


print(calendar.month(year, month))
# tc = calendar.TextCalendar()
# tc = calendar.TextCalendar()
# Print calendar for given month and year
# tc.prmonth(year, month)


# otherwise, print error and usage message
elif:
    print("ERROR: Should be in format '14_cal.py [month] [year]'")
    exit(0)
