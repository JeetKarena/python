import calendar as ca;

month=int(input("Enter month : "))
year=int(input("Enter Year : "))
# printing a calendar in python using a calendor module
print(f"{month} of {year} is ",ca.month(year,month))

# cheaking wheather a given year is leap year or not

year=int(input("Enter year you want to cheack for leap year : "))
print(f"{year} is a leap year ? Ans :  ",ca.isleap(year))