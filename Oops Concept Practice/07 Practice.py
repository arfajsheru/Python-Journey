# Write a python script to display the various Date Time Fromrate 
# A)Current Date and Time 
# b) Current year 
# c) moth of year 
# d) Week number of the year 
# e)Weekday of the week 


from datetime import datetime


Current_datetime = datetime.now()
print(f"Current Date and Time: {Current_datetime}")

Current_year = Current_datetime.year
print(f"Current year: {Current_year}")

Current_month  = Current_datetime.strftime("%B")
print(f"Month of the year: {Current_month}")

Week_no = Current_datetime.strftime("%U")
print(f"Week number of the year: {Week_no}")

Weekday_name = Current_datetime.strftime("%A")
print(f"Weekday of the week: {Weekday_name}")