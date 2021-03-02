
#change name from any case to title case(first letter in capital)

def format_name(fname,lname):
    fname = fname.title()
    lname = lname.title()
    return f"{fname} {lname}"


fname = input("What is your first name?")
lname = input("What is your last name?")

print(format_name(fname,lname))


# USE THE LEAP YEAR CALENDAR FROM THE PREVIOUS EXERCISE AND CREATE PROGRAM WHERE IT GIVE YOU DAY OF THE MONTH IF THE YEAR IS PROVIDED

# copied the program from day3

#check leap year program



#if the number is divisible by 4 except for the number which is divisible by 100 unless it is also divisible by 400
def check_leap(year):

    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                return True
            else:
                return False
        else:
            return True
    else:
        return False

def days_in_month(year,month):
    month_days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    if check_leap(year):
        month_days[1] = 29

    days = month_days[month-1]

    return days

year = int(input("Enter a year: "))
month = int(input("Enter a month: "))
days = days_in_month(year, month)
print(f"There are {days} days in that month")


