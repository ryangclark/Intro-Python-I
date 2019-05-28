"""
The Python standard library's 'calendar' module allows you to 
render a calendar to your terminal.
https://docs.python.org/3.6/library/calendar.html

Write a program that accepts user input of the form
  `calendar.py month [year]`
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
"""

import sys
import calendar
from datetime import datetime

def calendario(month=None, year=None, **args):
    '''Returns a calendar for the current month if no arguments passed;
        If one argument passed, returns a calendar for that argument;
        If two arguments passed, returns a calendar for the month and year.
        '''
    if args.items():
        return '''Returns a calendar for the current month if no arguments passed;
        If one argument passed, returns a calendar for that argument;
        If two arguments passed, returns a calendar for the month and year.
        '''
    if month and year:
        return calendar.TextCalendar.prmonth(year, month)
    if month:
        return calendar.TextCalendar.prmonth(datetime.date.today().year, month)
    return calendar.TextCalendar.prmonth(datetime.date.today().year, datetime.date.today().month)

calendario();
